import numpy as np

array = np.array('A')
print(array)
print(array.ndim)
print(array.shape)
print("\n\n")

array = np.array(['A', 'B'])
print(array)
print(array.ndim)
print(array.shape)
print("\n\n")

array = np.array(
    [
        ['A', 'B'], 
        ['C', 'D']
    ]
)
print(array)
print(array.ndim)
print(array.shape) #(rows, cols)
print("\n\n")

array = np.array(
    [
        [
            ['A', 'B'], 
            ['C', 'D']
        ],
        [
            ['E', 'F'], 
            ['G', 'H']
        ],
    ]
)
print(array)
print(array.ndim)
print(array.shape) #(layers, rows, cols)
print("Chain indexing: ", array[0][0][0])
print("multidimentional indexing: ", array[0, 0, 0]) # faster

