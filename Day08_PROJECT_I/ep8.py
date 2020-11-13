import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os
# #===================================================== Part 1 Basic Logic =====================================================#
# # --------------------------------------- Quiz1 ---------------------------------------#
# cnt = 0
# sum = 0
# while True:
#     try:
#         inp = float(input())
#         if inp == 0.0:
#             break
#         sum += inp
#         cnt += 1
#     except Exception as e:
#         print("Please input Number not String")
# mean = sum/cnt
# print("Mean= ", mean)
# print("Result= ",mean*cnt)
# # --------------------------------------- Quiz2 ---------------------------------------#
# prime_list = [2,3,5,7,11,13]
# try:
#     s_input = int(input("input start number "))
#     e_input = int(input("input end number "))
#     for i in range(s_input, e_input):
#         if i > 1:
#             for j in range(2, i):
#                 if i%j == 0:
#                     break
#             else:
#                 print("result=",i)
# except Exception as e:
#     print("some input is not a number, try again")

# #===================================================== Part 2 Game's Sales =====================================================#
# # --------------------------------------- Quiz1 ---------------------------------------#
# df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/vgsales.csv')
# # --------------------------------------- Quiz2 ---------------------------------------#
# df.head(5)
# df.tail(10)
# df.sample(10)
# # --------------------------------------- Quiz3 ---------------------------------------#
# df['Platform'].value_counts().head(10)
# # --------------------------------------- Quiz4 ---------------------------------------#
# df['Platform'].value_counts().tail(10)
# # --------------------------------------- Quiz5 ---------------------------------------#
# df['Genre'].value_counts().head(10)
# # --------------------------------------- Quiz6 ---------------------------------------#
# df['Genre'].value_counts().tail(10)
# # --------------------------------------- Quiz7 ---------------------------------------#
# df[df['Name']=='Grand Theft Auto V']
# # --------------------------------------- Quiz8 ---------------------------------------#
# df[df['Name'].duplicated(keep=False)]
# # --------------------------------------- Quiz9 ---------------------------------------#
# df[df[['Name','Platform']].duplicated(keep=False)]
# # --------------------------------------- Quiz10 ---------------------------------------#
# df = df.drop(df.index[[16127,14999,4145]])
# # --------------------------------------- Quiz11 ---------------------------------------#
# df2 = df.groupby('Name').sum().reset_index()
# result = df2[df2['Name']=='FIFA 15']['Global_Sales'].values[0]
# # --------------------------------------- Quiz12 ---------------------------------------#
# df2 = df[df['Name']=='Grand Theft Auto V'].groupby('Name').sum().reset_index()
# result = df2['JP_Sales'].values[0]
# # --------------------------------------- Quiz13 ---------------------------------------#
# df2 = df['Name'].value_counts()
# df2 = pd.DataFrame(df2)
# df2 = df2[df2['Name'] > 1]
# df2 = df2.rename(columns={'Name':'Count'})
# # --------------------------------------- Quiz14 ---------------------------------------#
# df2 = df.groupby('Publisher').sum().sort_values('Global_Sales')[::-1]
# # --------------------------------------- Quiz15 ---------------------------------------#
# df2 = df[df['Name'].str.contains('Call of Duty')]
# # --------------------------------------- Quiz16 ---------------------------------------#
# df2 = df[df['Name'].str.contains('Call of Duty')]
# df3 = df2[df2['Platform'] == 'PC'].sort_values('EU_Sales')[::-1].head(5)
# # --------------------------------------- Quiz17 ---------------------------------------#
# df2 = df.groupby('Platform').sum().reset_index().sort_values('EU_Sales')[::-1]
# result = df2['Platform'].iloc[0]
# # --------------------------------------- Quiz18 ---------------------------------------#
# df2 = df.groupby('Genre').mean().sort_values('Global_Sales')[::-1]
# # --------------------------------------- Quiz19 ---------------------------------------#
# fig = plt.figure(figsize=(12,12))
# sns.barplot(data=df,x='Platform',y='Global_Sales')
# plt.show()
# # --------------------------------------- Quiz20 ---------------------------------------#
# df2 = df.groupby('Publisher').sum().reset_index().sort_values('Global_Sales')[::-1].head(5)
# fig = px.pie(df2,names=df2['Publisher'],values=df2['Global_Sales'])
# fig.show()
# # --------------------------------------- Quiz21 ---------------------------------------#
# fig = plt.figure(figsize=(12,12))
# sns.countplot(x='Genre',data=df)
# plt.show()
# # --------------------------------------- Quiz22 ---------------------------------------#
# df2 = df[df['Name'].str.contains('Call of Duty')]
# df3 = df2[df['Platform']=='X360'].head(5)
# sns.barplot(data=df3,x='Name',y='Global_Sales')
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()
# # --------------------------------------- Quiz23 ---------------------------------------#
# df2 = df.groupby('Year').sum()
# fig = px.line(df2,x=df2.index, y='NA_Sales',title="Sales of NA")
# fig.show()
# # --------------------------------------- Quiz24 ---------------------------------------#
# fig = plt.figure(figsize=(12,12))
# fig = sns.stripplot(data=df,x='Genre',y='Global_Sales')
# fig.set(ylim=(0,15))
# plt.show()
# # --------------------------------------- Quiz25 ---------------------------------------#
# fig = plt.figure(figsize=(12,12))
# fig = sns.distplot(df['Year'])
# plt.show()
# # --------------------------------------- Quiz26 ---------------------------------------#
# df2 = df.groupby('Year').sum()
# df2.index = df2.index.astype(int)
# fig = plt.figure(figsize=(12,12))
# fig = sns.barplot(data=df2,x=df2.index,y='JP_Sales')
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()

# #===================================================== Part 2 Airbnb =====================================================#