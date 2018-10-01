from abupy import ABuSymbolPd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels import regression

kl_pd = ABuSymbolPd.make_kl_df('601318', n_folds=30)
print(kl_pd.tail())
print(kl_pd.shape)




# sb.set_context(rc={'figure.figsize': (14, 7)})
# sb.regplot(x=np.arange(0, kl_pd.shape[0]), y=kl_pd.close.values, marker='.')
# plt.show()
def calc_regress_deg(y_arr, show=True):
    x = np.arange(0, len(y_arr))
    zoom_factor = x.max() / y_arr.max()
    y_arr = zoom_factor * y_arr

    x = sm.add_constant(x)
    model = regression.linear_model.OLS(y_arr, x).fit()
    rad = model.params[1]
    deg = np.rad2deg(rad)
    if show:
        intercept = model.params[0]
        reg_y_fit = x * rad + intercept
        plt.plot(x, y_arr)
        plt.plot(x, reg_y_fit)
        plt.title('deg = ' + str(deg))
        plt.show()
    return deg

deg = calc_regress_deg(kl_pd.close.values[2490:2500],show=True)
print(str(deg))