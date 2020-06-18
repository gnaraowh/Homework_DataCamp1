import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Score = [90,80,100,50]
# Name = ["Tanawat","Ice","Point","Dmn4t"]
# Serie1 = pd.Series(data=Score, index=Name)
# print(Serie1)

# sns.barplot(Serie1.values, Serie1.index)
# plt.show()

# values = np.random.randint(40,100,(4,4))
# rows = ["Tanawat","Ice","Point","Dmn4t"]
# cols = ["mid1","mid2","final1","final2"]
# df = pd.DataFrame(values, rows, cols)
# print(df)
# #sns.barplot(x=df.index,y="mid1",data=df)
# sns.scatterplot(x="mid1",y=df.index,data=df)
# plt.show()

# df = pd.read_csv("https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day6/Automobile_data.csv")
# #print(df)

# fig = plt.figure(figsize=(10,8))
# #sns.countplot(x="make", data=df)
# sns.countplot(x="body-style",data=df)
# fig.autofmt_xdate()
# plt.show()

# score = np.array([1,2,5,6,7,9,12,15,18,19,27]) #Student Score Max 30
# min_score = score.min() # 1
# max_score = score.max() # 27
# range_score = score.ptp()# 27-1 (Max - Min)
# median_score = np.median(score)# 9
# q1 = 5 # median(1,2,5,6,7)
# q2 = median_score
# q3 = 18 # median(12,15,18,19,27)
# iqr = q3 - q1 # 13
# arr_median = np.where(score == median_score)

# print(arr_median[0])

src = "https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day6/Automobile_data.csv"
df = pd.read_csv(src,na_values={'price':["?"]})
df['price'] = pd.to_numeric(df['price'])

fig = plt.figure(figsize=(12,8))
sns.boxplot(x='make',y='price',data=df)

fig.autofmt_xdate()
plt.show()