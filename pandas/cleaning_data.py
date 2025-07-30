# Cleaning Empty cells, Wrong Format, Wrong Data, Removing Duplicate Data

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

# Notice in the result that some rows have been removed that contain empty cell.

#------------------------------------------------------------------------------------------------------------------------------------------------->

# If you want to change the original DataFrame, use the inplace = True argument.
# The dropna(inplace = True) will remove all row that containing null values.

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

#------------------------------------------------------------------------------------------------------------------------------------------------->
# empty cells got the value 130.

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

print(df.to_string())

# Fill value in spesific column.

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)