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

values = np.random.randint(40,100,(4,4))
rows = ["Tanawat","Ice","Point","Dmn4t"]
cols = ["mid1","mid2","final1","final2"]
df = pd.DataFrame(values, rows, cols)
print(df)
#sns.barplot(x=df.index,y="mid1",data=df)
sns.scatterplot(x="mid1",y=df.index,data=df)
plt.show()
