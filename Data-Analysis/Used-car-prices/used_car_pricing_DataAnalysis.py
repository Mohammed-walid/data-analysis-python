"""This is a modified Used car pricing module, data is already clean!
now we will use Data analysis"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(url)
df.to_csv("Clean_Used_car_prices.csv", index=False)
print("First 5 rows \n", df.head())

#hen visualizing individual variables, it is important to first understand
#what type of variable you are dealing with.
#This will help us find the right visualization method for that variable

print("DataFrame types \n", df.dtypes)

