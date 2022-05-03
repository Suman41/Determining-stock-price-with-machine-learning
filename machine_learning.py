import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error as MAE, \
    mean_squared_error as MSE

column_names = ['Number Of Shares', 'EPS', 'Book Value', 'Bonus']


class MachineLearning:

    def __init__(self, data):
        self.X = data[column_names]
        self.y = data['Price']
        self.predicted_list = []

    def find_price_regression(self, to_predict, method):
        if method == 'linear':
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3)
            lm = LinearRegression().fit(X_train, y_train)

            # # To check the accuracy of the test
            # predictions = lm.predict(X_test)
            # print(y_test)
            # print(predictions)
            # print(self.y.mean())
            # print(MAE(y_test, predictions))
            # print(MSE(y_test, predictions))
            # print(np.sqrt(MSE(y_test, predictions)))

            predicted_price = lm.predict(to_predict)
            print(f'linear: {predicted_price}')
            predictions = lm.predict(X_test)
            print(f'RMSE = {np.sqrt(MSE(y_test, predictions))}')
            self.predicted_list.append(predicted_price)

        # Ridge was giving much better results than linear
        if method == 'ridge':
            from sklearn.linear_model import Ridge
            model = Ridge(alpha=1.0)
            model.fit(self.X, self.y)
            predicted_price = model.predict(to_predict)
            print(f'ridge: {predicted_price}')

            from sklearn.model_selection import cross_val_score
            from sklearn.model_selection import RepeatedKFold
            cv = RepeatedKFold(n_splits=10, n_repeats=3)
            scores = cross_val_score(model, self.X, self.y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
            print(f'MAE: {np.std(scores)}')
            self.predicted_list.append(predicted_price)

