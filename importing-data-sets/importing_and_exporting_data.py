"""working with data module"""
import pandas as pd
import numpy as np
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header = None)
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height",
           "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore",
           "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers
df.to_csv("automobile_dataset_with_headers.csv", index=False)

print(df.tail(2))

print(df.head(3))
print("\n checking the Dataflow type \n")
print(df.dtypes)
print("\n checking statistical summary \n")
print(df.describe())
print("\n concise summary of the data frame \n")
print(df.info())
print("\n Full summary \n")
print(df.describe(include = "all"))

print(df[['length', 'compression-ratio']].describe())

#To drop missing values with will use dropna, since missing values can be Nan, or ? or blank
df.replace("?", np.nan, inplace=True) # we replaced all ? values to nan
df.dropna(axis = 0, inplace = True)
print(df)

#instead of deleting missing values we will replace them using the mean
df["horsepower"].replace(
    np.nan,
    df["horsepower"].mean(),
    inplace=True
)

print("\n Full summary modified\n")
print(df.describe(include = "all"))