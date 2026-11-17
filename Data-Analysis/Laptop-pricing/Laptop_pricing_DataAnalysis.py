"""This is a modified Laptop pricing module, data is already clean!
now we will use Data analysis"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(url)
df.to_csv("Cleaned laptop pricing.csv", index = False)

#checking first five rows
print(df.head())

price = df["Price"]
weight_pounds = df["Weight_pounds"]
screen_size_inch = df["Screen_Size_inch"]
CPU_frequency = df["CPU_frequency"]
sns.regplot(x = weight_pounds, y = price)
plt.show()
sns.regplot(x = screen_size_inch, y = price)
plt.show()
sns.regplot(x = CPU_frequency, y = price)
plt.show()

