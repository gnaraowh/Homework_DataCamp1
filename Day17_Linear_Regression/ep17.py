import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

pd.set_option('display.max_rows', None, 'display.max_columns', None)

df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/kc_house_data.csv')
# print(df.head(10))
# print(df.info())
# print(df.describe())
# print(df['bedrooms'].value_counts())
# print(df['grade'].value_counts())
# print(df['floors'].value_counts())

fig = plt.figure(figsize=(12,10))
# sns.distplot(df['price'])
#sns.boxplot(df['price'], orient='v')
# sns.countplot(df['bedrooms'])
# sns.countplot(df['grade'])
#fig = plt.figure(figsize=(30,20))
# plt.title('house price by sqft living')
# plt.xlabel('sqft living')
# plt.ylabel('house price')
# plt.legend()
# sns.barplot(x='grade',y='price',data=df)
# sns.barplot(x='floors',y='price',data=df)
# print(df.groupby('floors').mean()['price'])
# sns.pairplot(df)
# df_corr = df[['price', 'bedrooms', 'bathrooms',
#               'sqft_living', 'floors', 'grade']]
# sns.pairplot(df_corr)
# df_corr = df_corr.corr()
# sns.heatmap(df_corr)
# plt.show()

# print('Mean', df['sqft_living'].mean()) #Average
# print('Mode', df['sqft_living'].mode()[0]) #Most Sqft use
# print('Median', df['sqft_living'].median()) #Middle Value of all

# print('Mean', df['price'].mean()) #Average
# print('Mode', df['price'].mode()[0]) #Most Sqft use
# print('Median', df['price'].median()) #Middle Value of all

# x = df['sqft_living']
# y = df['price']
# x_train, x_test, y_train, y_test = train_test_split(
#     x, y, test_size=0.2, random_state=100)
# print(len(x_test))
# print(len(df))
# print(x_train)
# x_train = np.array(x_train).reshape(-1, 1)
# print(x_train)
#x_test = np.array(x_test).reshape(-1,1)

# print(y_train)
# y_train = np.array(y_train).reshape(-1, 1)
# print(y_train)
#y_test = np.array(y_test).reshape(-1,1)

# lm = LinearRegression()
# lm.fit(x_train, y_train)

# if sqft = 0 , price of house is -42628.9765151 usd (No house with 0 sqft )
# print(lm.intercept_)
# print(lm.coef_)  # Slope of Graph (+ Is Strong has high slope)

# print(['price'])
# coef_df = pd.DataFrame(lm.coef_, ['price'], columns=['slope'])
# print(coef_df)

# x_test_reshape = np.array(x_test).reshape(-1,1)
# predicted = lm.predict(x_test_reshape)
#print(predicted)


#plt.scatter(y_test, predicted)
#sns.distplot(y_test-predicted, bins=50)
#plt.show()

# mae = metrics.mean_absolute_error(y_test, predicted)
# mse = metrics.mean_squared_error(y_test, predicted)
# rmse = np.sqrt(metrics.mean_squared_error(y_test, predicted)) #meanning is error of house price is about $255511
# print(rmse)

#-------------- Result of Prediction --------------#
# lm.coef_ --> meanning is "Price per 1 sqft unit is 280 usd ($)"
# rmse --> meanning is "Error of model is 255511 usd ($) "

# dict_compare = {'price': y_test.tolist(), 'pridiceted price': predicted.tolist() }
# df_predicted = pd.DataFrame(dict_compare)
# print(df_predicted)

# sns.scatterplot(x_test, y_test, color='blue', label='real data')
# plt.plot(x_test, predicted, color='red', label='predicted regression price')
# plt.xlim([0,7500])
# plt.ylim([0,3500000])
# plt.show()

# print(lm.predict([[3000]]))

x = df['grade']
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=100)

x_train_re = np.array(x_train).reshape(-1,1)
x_test_re = np.array(x_test).reshape(-1,1)

y_train_re = np.array(y_train).reshape(-1,1)
y_test_re = np.array(y_test).reshape(-1,1)

lm2 = LinearRegression()
lm2.fit(x_train_re, y_train)

print(lm2.intercept_)
print(lm2.coef_)

predicted = lm2.predict(x_test_re)
print(predicted)
#sns.distplot((y_test-predicted), bins=50)
#plt.show()

mae = metrics.mean_absolute_error(y_test, predicted)
mse = metrics.mean_squared_error(y_test, predicted)
rmse = np.sqrt(metrics.mean_squared_error(y_test, predicted)) 

print('MAE:', mae)
print('MSE:', mse)
print('RMSE:', rmse)

sns.scatterplot(x_test, y_test, color='blue', label='real data')
plt.plot(x_test, predicted, color='red', label='predicted regression price')
# plt.xlim([0,7500])
# plt.ylim([0,3500000])
plt.show()