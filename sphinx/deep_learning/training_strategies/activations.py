
from matplotlib import pyplot as plt
import numpy as np

plt.figure(figsize=(12, 6))

plt.subplots_adjust(wspace=0.4, hspace=0.4)

x = np.linspace(-5.0, 5.0, 50)

plt.subplot(2, 4, 1)
linear = x.copy()
plt.plot(x, linear)
plt.title('Linear Function')

plt.subplot(2, 4, 2)
x2 = np.hstack([x[:25], x[24:]])
step = x2.copy()
step[:25] = 0.0
step[24:] = 1.0
plt.plot(x2, step)
plt.title('Step Function')

plt.subplot(2, 4, 3)
sigmoid = 1/(1+np.exp(-x))
plt.plot(x, sigmoid)
plt.title('Sigmoid')

plt.subplot(2, 4, 4)
tanh = np.tanh(x)
plt.plot(x, tanh)
plt.title('Hyperbolic Tangent (tanh)')

plt.subplot(2, 4, 5)
relu = x.copy()
relu[relu < 0] = 0.0
plt.plot(x, relu)
plt.title('Rectified Linear Unit (ReLU)')

plt.subplot(2, 4, 6)
leaky = x.copy()
leaky[leaky < 0] = leaky[leaky < 0] * 0.05
plt.plot(x, leaky)
plt.title('Leaky ReLU')

plt.subplot(2, 4, 7)
elu = x.copy()
elu[elu < 0] = 0.2 * (np.exp(elu[elu < 0])-1)
plt.plot(x, elu)
plt.title('ELU')

plt.subplot(2, 4, 8)
softmax = [0.2, 0.1, 0.6, 0.1]
plt.bar([1,2,3,4], softmax)
plt.text(0.75, 0.45, s=r"$\frac{e^{z_i}}{\sum_je^{z_j}}$", size=22)
plt.title('Softmax')


plt.savefig('activation_functions.png', dpi=150)
