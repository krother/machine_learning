import flappy_bird_gymnasium
import gymnasium
env = gymnasium.make("FlappyBird-v0", render_mode="human", use_lidar=True)

obs, _ = env.reset()
while True:
    # action: 0 nothing, 1 flap
    action = env.action_space.sample()

    # Processing:
    obs, reward, terminated, _, info = env.step(action)
    print(reward, obs.shape)
    
    # Checking if the player is still alive
    if terminated:
        break

env.close()