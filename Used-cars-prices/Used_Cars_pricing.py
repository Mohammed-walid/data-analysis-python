"""working with data module and applied and pre-processing data"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header = None)
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height",
           "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore",
           "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
df.columns = headers
df.to_csv("used_car_prices.csv", index=False)

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
print(df.head())

# isnull() replaces each element in the table to true if null and false if not null
missing_values_table = df.isnull()

#now we will count the number of missing values
for column in missing_values_table.columns.values.tolist(): #columns.values.tolist() get the name of all columnns and puts it into a list
    print(column)
    print(missing_values_table[column].value_counts()) #Selects one column from the DataFrame.
    #Counts how many times each value appears.
    print("")

#replace data to mean
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis = 0)
#axis = 0 means calculate the operation vertically (down the columns)
#if axis = 1 means calculate horizontally across rows
print("Average of normalized-losses:", avg_norm_loss)
df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg_norm_loss)

avg_bore = df["bore"].astype("float").mean(axis = 0)
print("average of bore column:", avg_bore)
df["bore"] = df["bore"].replace(np.nan, avg_bore)

avg_stroke = df["stroke"].astype("float").mean(axis = 0)
print("average of stroke: ",avg_bore)
df["stroke"] = df["stroke"].replace(np.nan, avg_stroke)

avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'] = df['peak-rpm'].replace(np.nan, avg_peakrpm)


print(df['num-of-doors'].value_counts())
print(df['num-of-doors'].value_counts().idxmax())
df["num-of-doors"] = df["num-of-doors"].replace(np.nan, "four")

#another way to replace
df["horsepower"].replace(
    np.nan,
    df["horsepower"].astype("float").mean(),
    inplace=True
)

df.dropna(subset = ["price"],axis = 0, inplace = True)
df.reset_index(drop = True, inplace = True) #reset_index() Resets the row numbering after deleting rows

print(df.head())

#Data  type correction
print(df.dtypes)
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
print(df.dtypes)

#Data Standardization
df["highway-mpg"] = 235/df["highway-mpg"]
df.rename(columns = {"highway-mpg": "high-way-L/100km"}, inplace = True)
df.head()

#Data normalization
df['height'] = df['height']/df['height'].max()
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df[["length","width","height"]].head()

#Binging
df["horsepower"]=df["horsepower"].astype(int, copy=True)
plt.hist(df["horsepower"])

# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
print(bins)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

df["horsepower-binned"].value_counts()
plt.bar(group_names, df["horsepower-binned"].value_counts().reindex(group_names))

# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()

# draw histogram of attribute "horsepower" with bins = 3
plt.hist(df["horsepower"], bins=3)

# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()

#Indicator variable
dummy_variable_1 = pd.get_dummies(df["fuel-type"], dtype=int)
dummy_variable_1.head()
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
dummy_variable_1.head()
# merge data frame "df" and "dummy_variable_1"
df = pd.concat([df, dummy_variable_1], axis=1)
# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)
print(df.head())

dummy_variable_2 = pd.get_dummies(df['aspiration'], dtype=int)
# changing column names for clarity
dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
print(dummy_variable_2.head())

#Merging the new dataframe to the original dataframe, and dropping the column 'aspiration'.
df = pd.concat([df, dummy_variable_2], axis=1)
df.drop('aspiration', axis = 1, inplace=True)
df.to_csv('clean_df.csv', index=False)
