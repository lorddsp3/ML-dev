import pandas as pd

df = pd.read_csv("dataset/pokemon.csv", index_col="Name")

#print(df.drop_duplicates(subset="#").head().drop(columns=["Sp. Atk", "Sp. Def","Legendary","Total"]).to_string())

xyz = df[df["Total"] == 505]
print(xyz.drop(columns=["#", "Legendary"]).to_string())