"""This is a modified Used car pricing module, data is already clean!
now we will use Data analysis"""
import pandas as pd
import numpy as np

url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(url, header = None)
df.to_csv("Clean_Used_car_prices.csv", index=False)
