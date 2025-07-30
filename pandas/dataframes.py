import pandas as pd

marks = {
    "Name"  : ['Manav','Jay','Smit','Preet','Pratham','Sahal','Mitul','Om'],
    "Marks" : [78,80,90,75,95,79,92,90],
    "City"  : ['Anand','Himatnagar','Khambhat','Dakor','Umreth','Bhalej','Ahmedabad','Surat']
}

df = pd.DataFrame(marks)
print(df)

# refer to the row index

print(df.loc[0])
df.to_csv('Marks.csv')

print(df.head(3))
print(df.tail(2))

print(df.describe)