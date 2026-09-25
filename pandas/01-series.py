import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['a','b','c','d', 'e'])
print(series)
print(series.info())
print(series.shape)



# # .loc means find data label
# print("loc: ", series.loc['a'])

# # can also update by loc
# # series.loc["a"] = 100
# # print(series)

# #use .iloc to get from integer location || like index

# #basic filtering data
# print("filter: ", series[series >= 30])



# mapp = {"a1": 101, "a2": 202, "a3": 303, "a4": 404, "a5": 505}

# sr = pd.Series(mapp)
# print(sr)
# print(sr[sr>= 404])
