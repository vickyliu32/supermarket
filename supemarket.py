from statistics import median
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

store = pd.read_csv("supermarket_dataset.csv")

store.head()
print(store.head())

#basic statistics
print(store.describe())

#indicate correation between different variables
correlations = store.corr()
print(correlations)

#create visulization
plt.figure(figsize=(10,6))
sns.scatterplot(x = 'Store_Area', y ='Store_Sales', data = store)
plt.title('Store Area vs Store Sales')
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(correlations, annot =True, cmap='coolwarm')
plt.title('Correalation Heatmap')
plt.show()