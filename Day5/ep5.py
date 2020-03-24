import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------- QUIZ1 ----------------------------------------#
x = np.arange(0,20)
y = x**2
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("Y")
plt.title("Title")
plt.show()

#---------------------------------------- QUIZ2 ----------------------------------------#
x = np.arange(0,20)
y = np.sin(x)
plt.plot(x,y, c="pink")
plt.xlabel("x")
plt.ylabel("Y")
plt.title("Title")
plt.show()

#---------------------------------------- QUIZ3 ----------------------------------------#
x = np.arange(0,20)
y = np.sqrt(x)
plt.plot(x,y, c="#96FF33")
plt.xlabel("x")
plt.ylabel("Y")
plt.title("Title")
plt.show()

#---------------------------------------- QUIZ4 ----------------------------------------#
x = np.arange(0,20)
y = np.cos(x)
plt.plot(x,y, c="r",linestyle="--")
plt.xlabel("x")
plt.ylabel("Y")
plt.title("Title")
plt.show()

#---------------------------------------- QUIZ5 ----------------------------------------#
x = np.arange(0,20)
y1 = x**2
y2 = x**3
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.95,0.85], xlabel="x", ylabel="y1")
ax1.plot(x,y1,c="r",marker="o")
ax2 = fig.add_axes([0.2,0.5,0.4,0.4], xlabel="x", ylabel="y2")
ax2.plot(x,y2,c="b",marker="^")
plt.show()

#---------------------------------------- QUIZ6 ----------------------------------------#
x = np.arange(0,20)
y1 = x**2
x2 = y1**2
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.95,0.85], xlabel="x", ylabel="y1")
ax1.plot(x,y1,c="r",marker="o")
ax1.grid()
ax1.legend(["legend1"])
ax2 = fig.add_axes([0.2,0.45,0.4,0.4], xlabel="x", ylabel="y2")
ax2.plot(x2,y1,c="b",marker="^")
ax2.grid()
ax2.legend(["legend2"])
plt.show()

#---------------------------------------- QUIZ7 ----------------------------------------#
y = np.arange(0,20)
x = y**2+(4*y)
plt.plot(x,y, c="#F3FF33")
plt.xlabel("x")
plt.ylabel("Y")
plt.title("Title")
plt.xlim([0,400])
plt.ylim([0,20])
plt.show()

#---------------------------------------- QUIZ8 ----------------------------------------#
y = np.arange(0,20)
x = y**3
y2 = x**2+2
fig = plt.figure(figsize=[10,10])
ax1 = fig.add_axes([0.1,0.1,0.95,0.85], xlabel="x", ylabel="y1")
ax1.plot(x,y,c="r",marker="o")
ax1.grid()
ax1.legend(["legend1"])
ax2 = fig.add_axes([0.4,0.2,0.4,0.4], xlabel="x", ylabel="y2")
ax2.plot(x,y2,c="b",marker="^")
ax2.grid()
ax2.legend(["legend2"])
plt.show()

#---------------------------------------- QUIZ9 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
gb_pclass = df.groupby(['Pclass']).count()
gb_pclass = gb_pclass['PassengerId']
plt.figure(figsize=[5,5])
label = gb_pclass.index
plt.pie(gb_pclass.values,labels=label)
plt.show()

#---------------------------------------- QUIZ10 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
gb_pclass = df.groupby(['Embarked']).count()
gb_pclass = gb_pclass['PassengerId']
plt.figure(figsize=[5,5])
label = gb_pclass.index
explode = [0,0.15,0]
plt.pie(gb_pclass.values,labels=label,explode=explode)
plt.show()

#---------------------------------------- QUIZ11 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
plt.hist(df['Fare'].values)
plt.show()

#---------------------------------------- QUIZ12 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
avg = df['Age'].mean()
df['Age'].fillna(value=avg, inplace=True)
plt.scatter(df['Age'].values, df['Fare'].values)
plt.show()

#---------------------------------------- QUIZ13 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
gb_pclass = df.groupby(['Pclass']).mean()
gb_pclass = gb_pclass['Fare']
print(gb_pclass)
plt.bar(gb_pclass.index, gb_pclass.values)
plt.xticks(gb_pclass.index, gb_pclass.index)
plt.show()

#---------------------------------------- QUIZ14 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
clean_age = df[df['Age']<1]['Age'].apply(lambda x: x*100)
avg = df['Age'].mean()
df['Age'].fillna(value=avg, inplace=True)
df.update(clean_age)
gb_pclass = df.groupby(['Age']).mean()
gb_pclass = gb_pclass['Fare']
plt.bar(gb_pclass.index, gb_pclass.values)
plt.xticks(gb_pclass.index, np.round(gb_pclass.index,2))
plt.show()

#---------------------------------------- QUIZ15 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
sr_lastname = df['Name'].apply(lambda x: x.split(',')[0])
df['Lastname'] = sr_lastname
df = df.groupby(['Lastname']).count()
output = df[df['Name']>1]['Name']
print(output)
plt.bar(output.index, output.values)
plt.xticks(output.index, output.index)
plt.show()

#---------------------------------------- QUIZ16 ----------------------------------------#
fig = plt.figure()
fig.subplots_adjust(hspace=1,wspace=0)

ax1 = fig.add_subplot(131,title="Age Scatter",xlabel="Age",ylabel="Fare")
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
avg = df['Age'].mean()
df['Age'].fillna(value=avg, inplace=True)
ax1.scatter(df['Age'].values, df['Fare'].values)

ax2 = fig.add_subplot(222,title="Fare Histogram",xlabel="Fare",ylabel="Fare")
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
ax2.hist(df['Fare'].values)
ax2.plot(y,x,c="r")

ax3 = fig.add_subplot(224,title="Embarked Pie")
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/Day4/train.csv')
gb_pclass = df.groupby(['Embarked']).count()
gb_pclass = gb_pclass['PassengerId']
label = gb_pclass.index
explode = [0,0.15,0]
ax3.pie(gb_pclass.values,labels=label,explode=explode)
ax3.plot(x,y)

plt.tight_layout()
plt.show()