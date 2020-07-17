import pandas as pd
import numpy as np

#------------------------------------ QUIZ1 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
print(df)
#------------------------------------ QUIZ2 ------------------------------------
print(df.head(10))
print(df.tail(10))
print(df.sample(10))
#------------------------------------ QUIZ3 ------------------------------------
print(df.dropna(subset=['Embarked']))
#------------------------------------ QUIZ4 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
avg = df['Age'].mean()
df['Age'].fillna(value=avg, inplace=True)
print(df)
#------------------------------------ QUIZ5 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df['Age'].fillna(value=0, inplace=True)
print(df)
#------------------------------------ QUIZ6 ------------------------------------
print(df.dropna(subset=['Age']))
#------------------------------------ QUIZ7 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
cnt_male = df[df['Sex']=="male"]['Sex'].value_counts()
cnt_female = df[df['Sex']=="female"]['Sex'].value_counts()
ratio_fm = cnt_female[0]/cnt_male[0]
print(ratio_fm)
#------------------------------------ QUIZ8 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
cnt_male   = df[ (df['Sex']=='male') & (df['Survived']==1) ]
cnt_female   = df[ (df['Sex']=='female') & (df['Survived']==1) ]
print("Survived Male:Female is {}:{}".format(len(cnt_male),len(cnt_female) ))
#------------------------------------ QUIZ9 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
cnt_people = len(df)
cnt_male   = len(df[ (df['Sex']=='male') & (df['Survived']==1) ])
cnt_female   = len(df[ (df['Sex']=='female') & (df['Survived']==1) ])
cnt_male_all = df[df['Sex']=="male"]['Sex'].value_counts()[0]
cnt_female_all = df[df['Sex']=="female"]['Sex'].value_counts()[0]
print("Survived Male = {}%, Female = {}% of All People".format(cnt_male*100/cnt_people, cnt_female*100/cnt_people))
print("Survived Male = {}%, Female = {}% of There Sex".format(cnt_male*100/cnt_male_all, cnt_female*100/cnt_female_all))
#------------------------------------ QUIZ10 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df.loc[df['Sex']=='female','Sex']=1
df.loc[df['Sex']=='male','Sex']=0
print(df)
#------------------------------------ QUIZ11 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
focus_cond = df['Age'].max()
person = df[df['Age']==focus_cond].iloc[0]
print("Name is {}, Age = {}, Embarked at {}".format(person['Name'],person['Age'],person['Embarked']))
#------------------------------------ QUIZ12 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
focus_cond = df['Age'].min()
person = df[df['Age']==focus_cond].iloc[0]
print("Name is {}, Age = {}, Embarked at {}".format(person['Name'],person['Age'],person['Embarked']))
#------------------------------------ QUIZ13 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
focus_cond = df['Fare'].max()
person = df[df['Fare']==focus_cond].iloc[0]
print("Name is {}, Age = {}, Survived = {}".format(person['Name'],person['Age'],bool(person['Survived'])))
#------------------------------------ QUIZ14 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
focus_cond = df['Fare'].min()
person = df[df['Fare']==focus_cond].iloc[0]
print("Name is {}, Age = {}, Survived = {}".format(person['Name'],person['Age'],bool(person['Survived'])))
#------------------------------------ QUIZ15 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
gb_pclass = df.groupby(['Pclass']).count()
gb_pclass = gb_pclass['PassengerId']
print(gb_pclass)
#------------------------------------ QUIZ16 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
gb_pclass = df.groupby(['Pclass']).mean()
gb_pclass = gb_pclass['Fare']
print(gb_pclass)
#------------------------------------ QUIZ17 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
survived_50 = df[(df['Age'] > 50) & (df['Survived']==1)]
print(len(survived_50))
#------------------------------------ QUIZ18 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
gb_pclass = df.groupby(['Pclass'])
print(gb_pclass.describe())
#------------------------------------ QUIZ19 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
gb_pclass = df.groupby(['Pclass'])['Fare'].max()
print(gb_pclass)
#------------------------------------ QUIZ20 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
age_max = df['Age'].max()+1
age_range = np.arange(0,age_max,10)
cnt_survived = df['Survived'].sum()
df = df.groupby(pd.cut(df['Age'],age_range)).sum()
survived_ratio = df['Survived'].apply(lambda x: x/cnt_survived*100)
print(survived_ratio)
#------------------------------------ QUIZ21 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.sort_values(by=['Fare'])
print(df)
df = df[::-1]
print(df)
#------------------------------------ QUIZ22 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
sr_lastname = df['Name'].apply(lambda x: x.split(',')[0])
df['Lastname'] = sr_lastname
df = df.groupby(['Lastname']).count()
print(df[df['Name']>1]['Name'])
#------------------------------------ QUIZ23 ------------------------------------
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
sr_lastname = df['Name'].apply(lambda x: x.split(',')[0])
df['Lastname'] = sr_lastname
df = df.groupby(['Lastname']).count()
print(df[df['Name']==1]['Name'])