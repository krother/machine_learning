"""
Training FlappyBird using Reinforcement Learning

pip install or:
uv add torch
uv add gymnasium
uv add flappy_bird_gymnasium

run:

uv run flappy_bird_gymnasium
uv run flappy_bird_gymnasium --mode random

uses: https://gymnasium.farama.org/
"""
import json
import random
from collections import deque
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

import flappy_bird_gymnasium
import gymnasium


# ================================
#   2-Layer MLP Q-Network
# ================================
class QNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, output_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)


# ================================
#   DQN Agent
# ================================
class DQNAgent:
    def __init__(
        self,
        state_dim,
        action_dim,
        lr=1e-3,
        gamma=0.99,
        epsilon=1.0,
        epsilon_min=0.02,
        epsilon_decay=0.995,
        buffer_size=50_000,
        batch_size=64,
    ):

        self.state_dim = state_dim
        self.action_dim = action_dim
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.batch_size = batch_size

        self.memory = deque(maxlen=buffer_size)

        self.model = QNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        #self.loss_fn = nn.MSELoss()
        self.loss_fn = nn.BCEWithLogitsLoss()

    def act(self, state):
        # ε-greedy policy
        if random.random() < self.epsilon:
            return random.randint(0, self.action_dim - 1)
        with torch.no_grad():
            state = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
            q_values = self.model(state)
        return int(torch.argmax(q_values, dim=1))

    def remember(self, transition):
        self.memory.append(transition)

    def replay(self):
        if len(self.memory) < self.batch_size:
            return

        batch = random.sample(self.memory, self.batch_size)

        states = torch.tensor(np.array([b[0] for b in batch]), dtype=torch.float32)
        actions = torch.tensor([b[1] for b in batch], dtype=torch.int64)
        rewards = torch.tensor([b[2] for b in batch], dtype=torch.float32)
        next_states = torch.tensor(np.array([b[3] for b in batch]), dtype=torch.float32)
        dones = torch.tensor([b[4] for b in batch], dtype=torch.float32)

        # Q(s,a)
        q_values = self.model(states)
        q_values = q_values.gather(1, actions.unsqueeze(1)).squeeze(1)

        # Target: r + γ max Q(s',·)
        next_q_values = self.model(next_states).max(1)[0]
        targets = rewards + (1 - dones) * self.gamma * next_q_values

        loss = self.loss_fn(q_values, targets.detach())

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # decay ε
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


# ================================
#   JSON Logger
# ================================
class JSONLogger:
    def __init__(self, path="experience.json"):
        self.path = path

        # reset file
        with open(self.path, "w") as f:
            json.dump([], f)

    def log(self, transition_dict):
        with open(self.path, "r") as f:
            data = json.load(f)

        data.append(transition_dict)

        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)


# ================================
#   Training Loop
# ================================
def train_dqn(episodes=500):

    env = gymnasium.make("FlappyBird-v0", render_mode="human", use_lidar=False)

    obs, _ = env.reset()
    state_dim = obs.shape[0]
    action_dim = env.action_space.n

    agent = DQNAgent(state_dim, action_dim)
    logger = JSONLogger("flappy_experience.json")

    for ep in range(episodes):
        obs, _ = env.reset()
        total_reward = 0

        while True:
            action = agent.act(obs)
            print(action, end="")
            next_obs, reward, terminated, truncated, info = env.step(action)

            done = terminated or truncated
            total_reward += reward

            # store in replay buffer
            agent.remember((obs, action, reward, next_obs, done))

            # also store in JSON file
            logger.log({
                "state": obs.tolist(),
                "action": action,
                "reward": reward,
                "next_state": next_obs.tolist(),
                "done": done
            })

            obs = next_obs
            agent.replay()

            if done:
                print(f"Episode {ep+1} | Score: {total_reward:.2f} | Epsilon: {agent.epsilon:.3f}")
                break

    env.close()
    torch.save(agent.model.state_dict(), "dqn_flappy_model.pt")
    print("Training complete! Model saved as dqn_flappy_model.pt")


if __name__ == "__main__":
    train_dqn(episodes=200)
