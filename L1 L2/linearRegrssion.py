import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import numpy as np
import seaborn as sns

df: DataFrame = pd.read_csv(filepath_or_buffer=r"D:\Python\IBM Data Analyst Professional Certificate\Data Analysis with Python\clean_cars_df.csv")

print(df.columns)

d_types_list: Series = df.dtypes

print(type(d_types_list))

def gradient_decent(b0, b1, points, learning_rate):
    b0_gradient = 0
    b1_gradient = 0
    
    #length of the data 
    N = len(points)
    
    for i in range(N):
        x = points["highway-L/100km"].iloc[i]
        y = points["price"].iloc[i]
        
        y_pred = b0 + b1 * x
        
        # derivatives equations for b0 and b1
        b0_gradient += -(2/N) * (y - y_pred)
        b1_gradient += -(2/N) * x * (y - y_pred)
    
    # update b0 and b1
    b0 = b0 - learning_rate * b0_gradient
    b1 = b1 - learning_rate * b1_gradient
    
    return b0, b1

b0 = 0
b1 = 0
learning_rate = 0.01
epochs = 10000 # number of iterations
for i in range(epochs):
    if i % 2000 == 0:
        print(f"epochs: {i}")
    b0, b1 = gradient_decent(b0=b0,b1=b1,points=df, learning_rate=learning_rate)
print(b0, b1)

x_values = np.linspace(min(df["highway-L/100km"]), max(df["highway-L/100km"]), 100)
y_values = b0 + b1 * x_values

plt.figure(figsize=(13,5))
plt.subplot(1,2,1)
plt.scatter(df["highway-L/100km"], df["price"], color="black")
plt.plot(x_values, y_values, lw=1, color="red")
plt.title(label="Gradient decent function".title(), fontsize=14)
plt.subplot(1,2,2)
sns.regplot(x=df["highway-L/100km"], y=df["price"])
plt.title(label="seaborn regression plot".title(), fontsize=14)
sns.set_style(style="darkgrid")
plt.tight_layout()
plt.show()
