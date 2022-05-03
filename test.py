# data = '1,234'
# data_split = data.split(',')
# print(data_split)
# value = ''.join(data_split)
# print(value)

import pandas as pd
import numpy as np

# data2 = []
# for item in data2:
#     print('It works')
# data = [[1, 3, 5, 7, None]]
# # x = np.array(data)
# # np.reshape(x, (1, 5))
# data1 = [3, 5, 8, 9, 7]
# df = pd.DataFrame(data)
# print(df)
# df.dropna(inplace=True)
# print(df)
# data2.append(data)
# data2.append(data1)
# print(data2)
# count = 0
# while count != 5:
#     count += 1
#     if count == 4:
#         continue
#     else:
#         print(count)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# import os
#
# s = Service('C:\Development\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
# driver.get('https://merolagani.com/CompanyDetail.aspx?symbol=BNHC')
# share_string = driver.find_element(By.XPATH, '//*[@id="accordion"]/tbody[2]/tr/td').text
# print(type(share_string))
#
# driver.quit()

# data = None
# value = float(data)

x = 2
y = 3
print(x + y)

# def find_price_principal_component_analysis(self):
#     self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3)
#     y_train_list = list(self.y_train)
#     self.X_train['Price'] = y_train_list
#
#     from sklearn.preprocessing import StandardScaler
#     scaler = StandardScaler()
#     scaler.fit(self.X_train)
#     scaled_data = scaler.transform(self.X_train)
#
#     from sklearn.decomposition import PCA
#     pca = PCA(n_components=1)
#     pca.fit(scaled_data)
#     x_pca = pca.transform(scaled_data)
#     df_comp = pd.DataFrame(pca.components_, columns=column_names)
#     self.y_train = df_comp['Price']
#     self.X_train = df_comp.drop('Price', axis=1)
#     print(f'{self.X_train}\n{self.y_train}')
#
#     self.find_price_linear_regression()

# if method == 'ANN':
#     from sklearn.preprocessing import StandardScaler
#
#     X = self.X.values
#     y = [self.y.values]
#     # Standardization of data
#     XScaler = StandardScaler()
#     yScaler = StandardScaler()
#
#     # Storing the fit object for later reference
#     XScalerFit = XScaler.fit(X)
#     yScalerFit = yScaler.fit(y)
#
#     # Generating the standardized values of X and y
#     X = XScalerFit.transform(X)
#     y = yScalerFit.transform(y)
#     X_train, X_test, y_train, y_test = train_test_split(X, self.y, test_size=0.3)
#
#     # importing the libraries
#     from keras.models import Sequential
#     from keras.layers import Dense
#
#     # create ANN model
#     model = Sequential()
#
#     # Defining the Input layer and FIRST hidden layer, both are same!
#     model.add(Dense(units=3, input_dim=4, kernel_initializer='normal', activation='relu'))
#
#     # Defining the Second layer of the model
#     # after the first layer we don't have to specify input_dim as keras configure it automatically
#     model.add(Dense(units=3, kernel_initializer='normal', activation='tanh'))
#
#     # The output neuron is a single fully connected node
#     # Since we will be predicting a single number
#     model.add(Dense(1, kernel_initializer='normal'))
#
#     # Compiling the model
#     model.compile(loss='mean_squared_error', optimizer='adam')
#
#     # Fitting the ANN to the Training set
#     model.fit(X_train, y_train, batch_size=4, epochs=10, verbose=1)
#     Predictions = model.predict(X_test)
#
#     # Scaling the predicted Price data back to original price scale
#     Predictions = yScalerFit.inverse_transform(Predictions)
#
#     # Scaling the y_test Price data back to original price scale
#     y_test_orig = yScalerFit.inverse_transform(y_test)
#
#     # Scaling the test data back to original scale
#     Test_Data = XScalerFit.inverse_transform(X_test)
#
#     TestingData = pd.DataFrame(data=Test_Data, columns=column_names)
#     TestingData['Price'] = y_test_orig
#     TestingData['PredictedPrice'] = Predictions
#     print(TestingData.head())
