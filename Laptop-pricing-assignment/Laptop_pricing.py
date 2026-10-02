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



