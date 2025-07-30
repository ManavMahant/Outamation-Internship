import pandas as pd

df = pd.read_csv('Marks.csv')

# use to_string() to print the entire DataFrame.

print(df.to_string())

# to print max row
print(pd.options.display.max_rows)
