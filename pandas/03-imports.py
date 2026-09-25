import pandas as pd

# #all this will be a dataframe

csv = pd.read_csv("dataset/pokemon.csv")
# print(csv)
# print(csv.describe())
# # to print whole
# print(csv.to_string()) 

# json = pd.read_json("dataset/periodictable.json")
# print(json)
# print(json.to_string()) 

# # SELECTION OF A COLUMN
# print("\n\n", csv['Name'])

# # SELECTION OF MANY COLUMN
# print("\n\n", csv[['Name', 'Legendary', 'Type 1']])

# # SELECTION OF A ROW
# print("\n\n", csv.loc[0])

# # ALSO YOU CAN SET INDEX OF DF BY ONE OF ITS COLS 
# csv = pd.read_csv("dataset/pokemon.csv", index_col="Name")
# print(csv)

# # NOW YOU CAN DO A SEARCH BY LABLE NAME
# print("\n\n", csv.loc["Mew"])

# GETTING ONLY REQUIRED DATA
# print("\n\n", csv.loc["Mew", ["Type 1", "HP", "Legendary"]])

# CAN ALSO SELECT RANGE OF ROWS 
# print("\n\n", csv.loc["Moltres":"Mew", ["Type 1", "HP", "Legendary"]])

# CAN ALSO SELECT RANGE OF ROWS BY INTEGER BASED LOCS, filtering of required data should be also int based
# print("\n\n", csv.iloc[0:4, 0:4])

