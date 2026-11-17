"""This is a modified Laptop pricing module, data is already clean!
now we will use Data analysis"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from narwhals import Object
from scipy import stats

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(url)
df.to_csv("Cleaned laptop pricing.csv", index = False)

#checking first five rows
print(df.head())

#Regression plot
price = df["Price"]
weight_pounds = df["Weight_pounds"]
screen_size_inch = df["Screen_Size_inch"]
CPU_frequency = df["CPU_frequency"]
sns.regplot(x = weight_pounds, y = price)
#plt.show()
sns.regplot(x = screen_size_inch, y = price)
#plt.show()
sns.regplot(x = CPU_frequency, y = price)
#plt.show()

for i in ["Weight_pounds", "Screen_Size_inch", "CPU_frequency"]:
    print(f"The Correlation of price and {i} is \n", df[[i,"Price"]].corr())

#Box plot
sns.boxplot(x = "Category", y = "Price", data = df)
#plt.show()
sns.boxplot(x = "GPU", y = "Price", data = df)
#plt.show()
sns.boxplot(x = "OS", y = "Price", data = df)
#plt.show()
sns.boxplot(x = "CPU_core", y = "Price", data = df)
#plt.show()
sns.boxplot(x = "RAM_GB", y = "Price", data = df)
#plt.show()
sns.boxplot(x = "Storage_GB_SSD", y = "Price", data = df)
#plt.show()

print("Descriptive Statistical Analysis \n", df.describe())
print("Descriptive Statistical Analysis With Object DataType Included \n", df.describe(include = ["object"]))

df_test = df[["GPU","CPU_core","Price"]]
grouped_test = df_test.groupby(["GPU","CPU_core"], as_index = False).mean()
print(grouped_test)
grouped_pivot = grouped_test.pivot(index='GPU',columns='CPU_core')
print(grouped_pivot)

fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

fig.colorbar(im)
