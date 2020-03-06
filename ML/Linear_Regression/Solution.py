#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
def main():
    data = pd.read_csv('Ecommerce Customers.csv')
    print(data.describe())
    # sns.jointplot(x = 'Time on Website', y = 'Yearly Amount Spent', data = data)
    # sns.jointplot(x = 'Time on App', y = 'Yearly Amount Spent', data = data)
    # sns.jointplot(x = 'Time on App', y = 'Length of Membership', data = data, kind = 'hex' )
    # sns.pairplot(data = data)
    # sns.lmplot(x = 'Yearly Amount Spent', y = 'Length of Membership', data = data)
    column = data.columns
    x = data[column[3 : 7]]
    y = data[column[7]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, train_size = 0.7, random_state = 101)
    lm = LinearRegression()
    lm.fit(x_train, y_train)
    predictions = lm.predict(x_test)
    print("coeff = ", lm.coef_)
    # plt.scatter(y_test, predictions)
    sns.distplot((y_test - predictions))
    print('MAE:', metrics.mean_absolute_error(y_test, predictions))
    print('MSE:', metrics.mean_squared_error(y_test, predictions))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
    coeffecients = pd.DataFrame(lm.coef_,X.columns)
    coeffecients.columns = ['Coeffecient']
    coeffecients
    plt.show()
if(__name__ == '__main__'):
    main()

# %%
