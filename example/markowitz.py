import pandas as pd
import numpy as np
import statsmodels.api as sm
import scipy.stats as scs
import matplotlib.pyplot as plt
import tushare

stock = ['000651格力电器', '000725京东方A', '600036招商银行', '600519贵州茅台', '601318中国平安']
noa = len(stock)
start_date = '2017-01-01'
end_date = '2017-10-27'

df1 = tushare.get_hist_data('000651', start_date, end_date, 'D')
df2 = tushare.get_hist_data('000725', start_date, end_date, 'D')
df3 = tushare.get_hist_data('600036', start_date, end_date, 'D')
df4 = tushare.get_hist_data('600519', start_date, end_date, 'D')
df5 = tushare.get_hist_data('601318', start_date, end_date, 'D')
data = pd.Panel({'000651格力电器': df1, '000725京东方A': df2, '600036招商银行': df3, '600519贵州茅台': df4, '601318中国平安': df5})
data = data.swapaxes(0, 2)
data = data['close']
returns = np.log(data / data.shift(1))

# print(data.head())
# print(data.tail())

# (data / data.ix[0] * 100).plot(figsize=(8, 6))
# plt.show()

print(returns.head())
# print(returns.mean())

# print(returns.mean() * 252)
# covs = returns.cov() * 252
# print(covs)

# weights = np.random.random(noa)
# weights /= np.sum(weights)
# mean = np.sum(returns.mean() * weights) * 252
# variance = np.dot(weights.T, np.dot(returns.cov() * 252, weights))
# standard_deviation = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
# for i in range(5):
#     print('%s\t%s%%' % (stock[i], weights[i] * 100))
# print('均值：%s\n方差：%s\n标准差：%s' % (mean, variance, standard_deviation))


port_returns = []
port_variance = []
for p in range(5000):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    port_returns.append(np.sum(returns.mean() * 252 * weights))
    port_variance.append(np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights))))

port_returns = np.array(port_returns)
port_variance = np.array(port_variance)

risk_free = 0.04


#
#
# plt.figure(figsize=(8, 4))
# plt.scatter(port_variance, port_returns, c=(port_returns - risk_free) / port_variance, marker='o')
# plt.grid(True)
# plt.xlabel('Standard Deviation')
# plt.ylabel('Expected Return')
# plt.colorbar(label='Sharpe')
# plt.show()
#
#
def statistics(weights):
    weights = np.array(weights)
    port_returns = np.sum(returns.mean() * weights) * 252
    port_variance = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    return np.array([port_returns, port_variance, port_returns / port_variance])


import scipy.optimize as sco


def min_sharpe(weights):
    return -statistics(weights)[2]


cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

bnds = tuple((0, 1) for x in range(noa))

opts = sco.minimize(min_sharpe, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)
print(opts)


def min_variance(weights):
    return statistics(weights)[1]


optv = sco.minimize(min_variance, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)
print(optv)

target_returns = np.linspace(0.65, 0.85, 50)
target_variance = []
for tar in target_returns:
    cons = ({'type': 'eq', 'fun': lambda x: statistics(x)[0] - tar}, {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    res = sco.minimize(min_variance, noa * [1. / noa, ], method='SLSQP', bounds=bnds, constraints=cons)
    target_variance.append(res['fun'])

target_variance = np.array(target_variance)

plt.figure(figsize=(8, 4))
plt.scatter(port_variance, port_returns, c=(port_returns - risk_free) / port_variance, marker='o')
plt.scatter(target_variance, target_returns, c=target_returns / target_variance, marker='x')
plt.plot(statistics(opts['x'])[1], statistics(opts['x'])[0], 'r*', markersize=15.0)
# plt.plot(statistics(optv['x'])[1], statistics(optv['x'])[0], 'y*', markersize=15.0)
plt.grid(True)
plt.xlabel('Standard Deviation')
plt.ylabel('Expected Return')
plt.colorbar(label='Sharpe')
plt.show()