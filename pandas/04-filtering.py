import pandas as pd

df = pd.read_csv("dataset/pokemon.csv")
# print(csv)


# strong = df[df["Total"] >= 600]
# print(strong)

# rare = df[df["Legendary"] == True]
# print(rare)
# #spefic col only
# rare = df.loc[df["Legendary"], ["Name", "HP"]]
# print(rare)
# water = df.loc[(df["Type 1"] == "Water") | (df["Type 2"] == "Water"), "Name"]
# print(water)

### AGREGATE FUNCTIONS 
# #operations on numerics
# print("Mean fo all numeric columns: \n", df.mean(numeric_only=True))
# print(df.count())
# #operation on single col, mean of this col
# print("Mean of single columns: \n", df["HP"].mean())

# #GRoupBy a functions that groups or filters rows that have some value common in cols
# #eg Pokemon type: fire, water, grass etc, we can make groups of each types
group = df.groupby("Type 1")
print(group["Total"].mean())
