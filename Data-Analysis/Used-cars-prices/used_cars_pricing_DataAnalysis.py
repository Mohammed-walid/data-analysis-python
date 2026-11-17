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
print("The data type of peak-rom is: \n", df["peak-rpm"].dtypes)

#Correlation tells us how two variables are related
numeric_df = df.select_dtypes(include=['float64', 'int64'])
print("Correlation between Data types \n", numeric_df.corr())

print("Correlation between columns \n", df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())
#"int64" or "float64". A great way to visualize these variables is by using scatterplots with fitted lines.
#regplot plots the scatterplot plus the fitted regression line for the data
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.show()
print("correlation between 'engine-size' and 'price' \n", df[["engine-size", "price"]].corr())
print("correlation between 'highway-mpg' and 'price' \n", df[['highway-mpg', 'price']].corr())
print("Correlation between 'peak-rpm' and 'price' \n", df[['peak-rpm','price']].corr()) #weak -ve relationship

sns.regplot(x="stroke", y="price", data=df) #Week relationship
plt.show()

#The categorical variables can have the type "object" or "int64".
#A good way to visualize categorical variables is by using boxplots.
sns.boxplot(x="body-style", y="price", data=df)
plt.show()
sns.boxplot(x="engine-location", y="price", data=df)
plt.show()
sns.boxplot(x="drive-wheels", y="price", data=df)
plt.show()

print("Descriptive Statistical Analysis \n", df.describe())

#since describe() skips datatype of type object we will use this to describe data of object types
print("Data of object types using Describe() \n", df.describe(include=['object']))
#Value counts is a good way of understanding how many units of each characteristic/variable we have
