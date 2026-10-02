"""A small assignment on Importing Datasets"""

import pandas as pd
import numpy as np
import requests

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"

response = requests.get(file_path)
if response.status_code == 200:
    with open("Laptop-pricing.csv", "wb") as f:
        f.write(response.content)


#TASK 1: Load the dataset to a pandas dataframe named 'df'
df = pd.read_csv("Laptop-pricing.csv", header = None)
print(df.head())

#TASK 2: Add headers to the dataframe
df.columns =  ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
print(df.head())

#Task 3: Replace '?' with 'NaN'
df.replace('?',np.nan, inplace = True)

#Task 4: Print the data types of the dataframe columns
print(df.dtypes)

#Task 5: Print the statistical description of the dataset, including that of 'object' data types
print(df.describe(include="all"))

#Task #6: Print the summary information of the dataset.
print(df.info())



