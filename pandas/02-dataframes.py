import pandas as pd

data = {
    "name": ["aa", "bb", "cc", "dd"],
    "age": [11, 22, 33, 44],
}

df = pd.DataFrame(data)
print(df)
print("find by label: \n", df.loc[3])

#add new column
df["gender"] = [True, False, True, False]
print(df)


#add new row
nr = pd.DataFrame([
    {"name": "ee", "age": 55, "gender": True},
    {"name": "ff", "age": 66, "gender": False}
                   ])
df = pd.concat([df, nr])
df = pd.concat([df, nr], ignore_index=True)
print(df)