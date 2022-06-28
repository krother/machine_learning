'''
Create an ARMA process and plot it
'''

from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['figure.figsize'] = (14,6)

np.random.seed(102)

ar_coefs = [1, -0.8]
ma_coefs = [1, 0.8]

arma = ArmaProcess(ar=ar_coefs, ma=ma_coefs)

arma.isstationary
arma.isinvertible

arma_process = arma.generate_sample(132)
arma = pd.DataFrame(arma_process, columns=['remainder'])

# plt.plot(arma_process)
arma.plot()
plt.savefig('arma_process.png')

# np.savetxt('arma_process.csv', arma_process, delimiter=',')
arma.to_csv('arma_process.csv', index=False)