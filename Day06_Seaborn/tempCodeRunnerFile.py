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