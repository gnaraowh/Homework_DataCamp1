import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import os


def getFilePath(file_name):
    file_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(file_path)
    root_path = os.path.dirname(dir_path)
    data_path = os.path.join(root_path, '__Data')
    ret_path = os.path.join(data_path, file_name)

    return ret_path


# rows = ['A', 'B', 'C', 'D']
# cols = ['Score1', 'Score2', 'Midterm', 'Final']
# values = np.random.randint(40, 100+1, (4, 4))
# df = pd.DataFrame(values, rows, cols)
# fig = px.bar(df, x=df.index, y='Midterm', hover_data=['Score1', 'Score2'], color='Final', labels={
#              'index': 'ชื่อนักเรียน', 'Final': R'คะแนนสอบปลายภาค'})
# fig.update_layout(xaxis_tickangle=-45)
# fig.show()
try:
    df = pd.read_csv(
        'https://raw.githubusercontent.com/gnaraowh/Homework_DataCamp1/master/__Data/Automobile_data.csv', na_values={
            'normalized-losses': ['?'],
            'strok': ['?'],
            'horsepower': ['?'],
            'num-of-doors': ['?'],
            'peak-rpm': ['?'],
            'price': ['?']
        }
    )
except Exception as e:
    df = pd.read_csv(getFilePath('Automobile_data.csv'), na_values={
        'normalized-losses': ['?'],
        'strok': ['?'],
        'horsepower': ['?'],
        'num-of-doors': ['?'],
        'peak-rpm': ['?'],
        'price': ['?']
    }
    )
df['price'] = pd.to_numeric(df['price'])
df['horsepower'] = pd.to_numeric(df['horsepower'])
# fig = px.line(df, x='horsepower', y='price',title='Avg of Horsepower')
# fig.show()

#df2 = df.groupby('horsepower').mean()
# fig = px.line(df2, x=df2.index, y='price',title='Avg of Horsepower')
# fig.show()

# df_ex = px.data.gapminder().query("continent=='Oceania'")
# fig = px.line(df_ex, x='year', y='lifeExp', color='country')
# fig.show()

# df2 = df.groupby('make').std()
# print(df2)
# fig = px.pie(df2, values='price', names=df2.index, title='Price')
# fig.show()

# df2 = df.groupby('body-style').std()
# df2.head()
# print(df2)
# fig = px.pie(df2, values='horsepower', names=df2.index, title='std Price', color_discrete_sequence=px.colors.sequential.Purp)
# fig.show()

# df2 = df.groupby('horsepower').mean()
# df2.head()
# fig = px.scatter(df2, x=df2.index, y='price', size='engine-size', color_discrete_sequence=px.colors.cyclical.HSV, color='wheel-base',
#                  labels={'horsepower': 'แรงม้า', 'price': 'ราคาเฉลี่ย', 'engine-size': 'ขนาดเครื่องยนต์'})
# fig.show()

# fig = px.box(df.dropna(), x='body-style', y='price', points='all', color='num-of-doors')
# fig.show()

# df2 = df.corr()
# fig = go.Figure(data=go.Heatmap(z=df2, x=df2.index,
#                                 y=df2.index, colorscale='Viridis'))
# fig.show()

# df3 = df.pivot_table(index='body-style',columns='drive-wheels', values='price')
# fig = go.Figure(data=go.Heatmap(z=df3, 
#                                 x=df3.columns,
#                                 y=df3.index, colorscale='Picnic'))
# fig.show()
