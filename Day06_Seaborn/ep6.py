import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None, 'display.max_columns', None)

#---------------------------------------- QUIZ1 ----------------------------------------#
idx = ['A', 'B', 'C', 'D']
col_year = np.arange(2014, 2017+1)
col_income = np.random.randint(50, 500, 4)
data = {'year': col_year, 'income': col_income}
df = pd.DataFrame(data, index=idx)

#---------------------------------------- QUIZ2 ----------------------------------------#
sns.barplot(data=df, x=df.index, y='income')
plt.show()
sns.barplot(data=df, y=df.index, x='income')
plt.show()

#---------------------------------------- QUIZ3 ----------------------------------------#
sns.scatterplot(data=df, x=df.index, y='income')
plt.show()
sns.scatterplot(data=df, y=df.index, x='income')
plt.show()

df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
#---------------------------------------- QUIZ4 ----------------------------------------#
sns.countplot(data=df, x='Embarked')
plt.show()
sns.countplot(data=df, y='Embarked')
plt.show()

#---------------------------------------- QUIZ5 ----------------------------------------#
sns.countplot(data=df, x='Pclass')
plt.show()
sns.countplot(data=df, y='Pclass')
plt.show()

#---------------------------------------- QUIZ6 ----------------------------------------#
sns.boxplot(data=df, x='Sex', y='Fare')
plt.show()

#---------------------------------------- QUIZ7 ----------------------------------------#
sns.boxplot(data=df, x='Pclass', y='Fare')
plt.show()

# #---------------------------------------- QUIZ8 ----------------------------------------#
# ข้อมูลไม่ได้ระบุจุดหมายปลายทาง มีแต่ ขึ้นเรือที่ไหน
sns.barplot(data=df, x='Embarked', y='Fare')
plt.show()

#---------------------------------------- QUIZ9 ----------------------------------------#
sns.barplot(data=df, x='Pclass', y='Age')
plt.show()

#---------------------------------------- QUIZ10 ----------------------------------------#
sns.stripplot(data=df, x='Pclass', y='Fare')
plt.show()

#---------------------------------------- QUIZ11 ----------------------------------------#
sns.stripplot(data=df, x='Survived', y='Age', hue='Sex')
plt.show()

#---------------------------------------- QUIZ12 ----------------------------------------#
sns.swarmplot(data=df, x='Sex', y='Age')
plt.show()

#---------------------------------------- QUIZ13 ----------------------------------------#
check = pd.crosstab(df['Pclass'], df['Sex'])
sns.heatmap(check, cmap='coolwarm', annot=True)
plt.show()

#---------------------------------------- QUIZ14 ----------------------------------------#
check = pd.pivot_table(data=df, index='Pclass', columns=['Sex'], values='Fare')
sns.heatmap(check, cmap='coolwarm', annot=True)
plt.show()

#---------------------------------------- QUIZ15 ----------------------------------------#
check = pd.pivot_table(data=df, index='Pclass', columns=['Sex'], values='Fare')
sns.heatmap(check, cmap='coolwarm', annot=True, linecolor='white', linewidth=2)
plt.show()

df = df.drop(['PassengerId'], axis=1)
#---------------------------------------- QUIZ16 ----------------------------------------#
df_corr = df.corr()
sns.heatmap(df_corr, cmap='coolwarm', annot=True)
plt.show()

#---------------------------------------- QUIZ17 ----------------------------------------#
df_corr = df.corr()
sns.clustermap(df_corr, cmap='coolwarm', annot=True)
plt.show()

#---------------------------------------- QUIZ18 ----------------------------------------#
sns.scatterplot(data=df_corr, x='SibSp', y='Parch')
plt.show()

#---------------------------------------- QUIZ19 ----------------------------------------#
sns.scatterplot(data=df, x='Pclass', y='Fare', hue='Sex')
plt.show()

#---------------------------------------- QUIZ20 ----------------------------------------#
sns.distplot(df['Fare'])
plt.show()
sns.distplot(df['Age'])
plt.show()

#---------------------------------------- QUIZ21 ----------------------------------------#
sns.pairplot(df)
plt.show()
