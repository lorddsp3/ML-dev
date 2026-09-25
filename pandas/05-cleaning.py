import pandas as pd

df = pd.read_csv("dataset/pokemon.csv")

# df = df.drop(columns=["#", "Generation", "Total", "Sp. Atk", "Sp. Def"])
#print(df[0:12].to_string())

# #HAndling Missing data
#df = df.dropna(subset=["Type 2"]) #drops all row missing type 2
# df = df.fillna({"Type 2": "Chutiya"})
# print(df[0:12].to_string())

# #Fix inconsistance data
# df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS"})
# print(df.head())

# #standardize text
# df["Name"] = df["Name"].str.lower()
# print(df.head())

# #remove dups
# df = df.drop_duplicates()