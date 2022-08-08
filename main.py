import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt


def run(df, rooms):
    x = df.loc[data['rooms'] == rooms][['month', 'district', 'area']]
    y = df.loc[data['rooms'] == rooms]['price_usd']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    # выведем корень среднеквадратической ошибки
    # сравним тестовые и прогнозные значения цен на жилье
    print('Root Mean Squared Error (RMSE):', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print('R2:', np.round(metrics.r2_score(y_test, y_pred), 2))

    plt.figure(figsize=(10, 6))
    plt.plot(list(range(1, len(y_pred) + 1)), y_pred, label="Predicted")
    plt.plot(list(range(1, len(y_test) + 1)), y_test, label="Test values")
    plt.legend()
    plt.show()


def normalize(df):
    # implement normalization
    return df


data = pd.read_csv("dataframe.csv")
data = normalize(data)

run(4)
run(3)
run(2)
run(1)
