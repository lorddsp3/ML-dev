import numpy as np 

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
#array[start:end:step]

print("first row: ", array[0])

print(array[0:3], "\n") # :end is inclusive so its like up until this insex so till 2
print(array[0:], "\n") # until end, from 0 to end
print(array[::], "\n") # print from start to end
print(array[::2], "\n") # print from start to end with step 2
print(array[::-1], "\n") # print from start to end in reverse

# comma means row, layer or column so
print(array[:, 2], "\n") # print 2 col of all rows
print(array[::2, 2], "\n") # print 2 col of all row with step 2
print(array[:, 0:4:2], "\n") # print cols from 0 to 4 with step 2 from all rows
#experimental
print(array[0:2, 2:4], "\n")
print(array[3, 2:4], "\n")
print(array[:, ], "\n")
print(array.diagonal())  # diagonal









