"""A small assignment on Importing Datasets"""

import pandas as pd
import numpy as np
import requests
from matplotlib import pyplot as plt

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"

response = requests.get(file_path)
if response.status_code == 200:
    with open("Laptop-pricing.csv", "wb") as f:
        f.write(response.content)


#TASK 1: Load the dataset to a pandas dataframe named 'df'
df = pd.read_csv("Laptop-pricing.csv", header = None)
print(df.head())

#TASK 2: Add headers to the dataframe
df.columns =  ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_cm", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
print(df.head())

#Task 3: Replace '?' with 'NaN'
df.replace('?',np.nan, inplace = True)

#Task 4: Print the data types of the dataframe columns
print(df.dtypes)

#Task 5: Print the statistical description of the dataset, including that of 'object' data types
print(df.describe(include="all"))

#Task #6: Print the summary information of the dataset.
print(df.info())

df[['Screen_Size_cm']] = np.round(df[['Screen_Size_cm']],2)
df.head()

missing_data = df.isnull()
print(missing_data.head())
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

avg_weight=df['Weight_kg'].astype('float').mean(axis=0)
df["Weight_kg"].replace(np.nan, avg_weight, inplace=True)

#Replace with the most frequent value
common_screen_size = df['Screen_Size_cm'].value_counts().idxmax()
df["Screen_Size_cm"].replace(np.nan, common_screen_size, inplace=True)

df[["Weight_kg","Screen_Size_cm"]] = df[["Weight_kg","Screen_Size_cm"]].astype("float")

df["Weight_kg"] = df["Weight_kg"]*2.205
df.rename(columns={'Weight_kg':'Weight_pounds'}, inplace=True)
df["Screen_Size_cm"] = df["Screen_Size_cm"]/2.54
df.rename(columns={'Screen_Size_cm':'Screen_Size_inch'}, inplace=True)

df['CPU_frequency'] = df['CPU_frequency']/df['CPU_frequency'].max()

bins = np.linspace(min(df["Price"]), max(df["Price"]), 4)
group_names = ['Low', 'Medium', 'High']
df['Price-binned'] = pd.cut(df['Price'], bins, labels=group_names, include_lowest=True )
plt.bar(group_names, df["Price-binned"].value_counts())
plt.xlabel("Price")
plt.ylabel("count")
plt.title("Price bins")
plt.show()

dummy_variable_1 = pd.get_dummies(df["Screen"])
dummy_variable_1.rename(columns={'IPS Panel':'Screen-IPS_panel', 'Full HD':'Screen-Full_HD'}, inplace=True)
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "Screen" from "df"
df.drop("Screen", axis = 1, inplace=True)

print(df.head())
