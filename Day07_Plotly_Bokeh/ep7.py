import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import os

pd.set_option('display.max_rows', None, 'display.max_columns', None)

#---------------------------------------- QUIZ1 ----------------------------------------#
rows = ['A', 'B', 'C', 'D', 'E']
cols = ['2016', '2017', '2018', '2019', '2020']

value_2020 = [10000, 20000, 30000, 40000, 60000]
values = []
for i in range(0, len(rows)):
    v_rows = []
    for j in range(0, len(cols)):
        salary = value_2020[i]/(1.07**(len(cols)-1-j))
        v_rows.append(salary)
    values.append(v_rows)
df = pd.DataFrame(values, rows, cols)
print(df)

#---------------------------------------- QUIZ2 ----------------------------------------#
df2 = pd.DataFrame.copy(df)
df2['2017'] = df2['2017']*2
fig = px.bar(df2, x=df2['2017'], y=df2.index)
fig.update_layout(xaxis_tickangle=-45)
fig.show()

#---------------------------------------- QUIZ3 ----------------------------------------#
cols = ['2016', '2017', '2018', '2019', '2020','mean']
df3 = pd.DataFrame.copy(df)
df3['mean'] = df3.mean(axis=1)
df3['2017'] = df3['2017']*2
fig = px.bar(df3, x=df3['2017'], y=df3.index, hover_data=cols, labels={'index':'ชื่อ','2017':'เงินเดือนปี 2017 x 2'},color='2016')
fig.update_layout(xaxis_tickangle=-45)
fig.show()

#---------------------------------------- QUIZ4 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.dropna(subset=['Age'])
df = df.groupby('Age').mean()
fig = px.line(df, x=df.index, y='Fare',title='Average Fare group by Age', labels={'Age':'Age','Fare':'Avg Fare'})
fig.show()

#---------------------------------------- QUIZ5 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.groupby('Pclass').mean()
fig = px.line(df, x=df.index, y='Fare',title='Average Fare group by Pclass', labels={'Pclass':'Pclass','Fare':'Avg Fare'})
fig.show()

#---------------------------------------- QUIZ6 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.dropna(subset=['Age'])
df = df.groupby('Age').sum()
fig = px.pie(df, values='Fare', names=df.index)

#---------------------------------------- QUIZ7 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.dropna(subset=['Age'])
df = df.groupby('Age').mean()
fig = px.pie(df, values='Fare', names=df.index)

#---------------------------------------- QUIZ8 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
sr_lastname = df['Name'].apply(lambda x: x.split(',')[0])
df['Lastname'] = sr_lastname
df = df.groupby('Lastname').describe()
df = df['Fare']
df = df[df['count']>1]
fig = px.pie(df, values='mean', names=df.index)
fig.show()

#---------------------------------------- QUIZ9 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
sr_lastname = df['Name'].apply(lambda x: x.split(',')[0])
df['Lastname'] = sr_lastname
df = df.groupby('Lastname').describe()
df = df['Age']
df = df[df['count']>1]
print(df)
fig = px.pie(df, values='mean', names=df.index, title='Fare\'s Mean of Duplicate Lastname', color_discrete_sequence=px.colors.sequential.Purp)
fig.show()

#---------------------------------------- QUIZ10 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.groupby('Embarked').mean()

titles = list(df.columns)
labels = list(df.index)
values = list(df['Fare'].values)
num_graph = len(df.columns)

tmp = []
domains = []
for i in range(0, len(df.columns)):
    tmp.append({'type': 'domain'})
    domains.append({'x': [0.0+0.14*i, 0.33], 'y': [0.0, 0.33]})
specs = []
specs.append(tmp)

fig = make_subplots(rows=1, cols=num_graph, specs=specs, subplot_titles=titles)
for i in range(0, len(titles)):
    values = list(df[titles[i]].values)
    fig.add_trace(go.Pie(labels=labels, values=values, scalegroup='one',
                         name=titles[i]), 1, i+1)
fig.show()

#---------------------------------------- QUIZ11 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.groupby('Age').mean()
fig = px.scatter(df, x=df.index, y='Fare', size='SibSp', color_discrete_sequence=px.colors.cyclical.HSV, color='Pclass',
                 labels={'Age': 'อายุ', 'Fare': 'ราคาเฉลี่ย', 'SibSp': 'พี่น้อง/คู่สมรส'}, title='ราคาเฉลี่ย แยกตามอายุ ขนาดตาม พี่น้อง/คู่สมรส')
fig.show()

#---------------------------------------- QUIZ12 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
fig = px.box(df, x='Sex',y='Fare')
fig.show()

#---------------------------------------- QUIZ13 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
fig = px.box(df, x='Pclass',y='Fare')
fig.show()

#---------------------------------------- QUIZ14 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
fig = px.box(df, x='Pclass',y='Age', points='all')
fig.show()

#---------------------------------------- QUIZ15 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
fig = px.box(df, x='Survived',y='Age',color_discrete_sequence=px.colors.cyclical.HSV, color='Sex')
fig.show()

#---------------------------------------- QUIZ16 ----------------------------------------#
# โจทย์ ถามหาจุดหมายปลายทางซึ่งไม่มีใน data เลยใส่ ข้อมูล Embarked ขึ้นเรื่อจากท่า แทน
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.groupby('Embarked').std()
fig = px.bar(df, x=df.index,y='Fare')
fig.show()

#---------------------------------------- QUIZ17 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df = df.groupby('Pclass').mean()
fig = px.bar(df, x=df.index,y='Age')
fig.show()

#---------------------------------------- QUIZ18 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df2 = df.pivot_table(index='Pclass', columns='Sex', values='Fare')
fig = go.Figure(data=go.Heatmap(z=df2,x=df2.columns,y=df2.index, colorscale='Picnic'))
fig.show()

#---------------------------------------- QUIZ19 ----------------------------------------#
df = pd.read_csv(
    'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/train.csv')
df2 = df.corr()
fig = go.Figure(data=go.Heatmap(z=df2,x=df2.index,y=df2.index, colorscale='Picnic'))
fig.show()

#---------------------------------------- QUIZ20 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
df.head()
for col in df.columns:
    df[col] = df[col].astype(str)
df['text'] = df['state'] + '<br>'\
    +'total exports ' + df['total exports'] + '<br>'\
    +'total fruits ' + df['total fruits'] + '<br>'\
    +'total veggies ' + df['total veggies']
fig = go.Figure(data=go.Choropleth(
    locations=df['code']
    , z= df['cotton']
    , locationmode = 'USA-states'
    , colorscale = 'Picnic'
    , colorbar_title = 'Millions USD'
    , text=df['text']
))
fig.update_layout(title_text='2011 US exports',geo_scope='usa')
fig.show()

#---------------------------------------- QUIZ21 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
df['beef:pork'] = round(df['beef']/df['pork'],2)
for col in df.columns:
    df[col] = df[col].astype(str)
df['text'] = df['state'] + '<br>'\
    +'beef:pork ' + df['beef:pork']

fig = go.Figure(data=go.Choropleth(
    locations=df['code']
    , z= df['total veggies']
    , locationmode = 'USA-states'
    , colorscale = 'Picnic'
    , colorbar_title = 'Millions USD'
    , text=df['text']
))
fig.update_layout(title_text='2011 US exports',geo_scope='usa')
fig.show()

#---------------------------------------- QUIZ22 ----------------------------------------#
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
df = df.sample(n=10)
df['cotton:wheat'] = df['cotton']/df['wheat']
df['cotton:wheat'] = df['cotton:wheat'].fillna(value=0)
fig = px.bar(df, x=df['state'], y='total exports', color='cotton:wheat', labels={
             'state': 'รัฐ', 'total exports': 'ยอดส่งออกรวม'})
fig.update_layout(xaxis_tickangle=-45)
fig.show()