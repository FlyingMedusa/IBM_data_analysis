# Import pandas libra
import pandas as pd
import numpy as np

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)

print("The last 10 rows of the dataframe\n")
df.tail(10)

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

#--------------
df.columns = headers
df.head(10)

# replace the "?" symbol with NaN so the dropna() can remove the missing values 
df1=df.replace('?', np.NaN)
df=df1.dropna(subset=["price"], axis=0)
df.head(20)

# Find the name of the columns of the dataframe
print(df.columns)

# df.to_csv("automobile.csv", index=False)

# check the data type of data frame "df" by .dtypes
print(df.dtypes)

# various summary statistics, excluding NaN (Not a Number) values
df.describe()

# all the columns including those that are of type object
df.describe(include = "all")

df[['length','compression-ratio']].describe()

df.info()
