import numpy as np

array = np.array([1, 2 , 3])
arrayfloat = np.array([1.01, 2.30, 3.40, 4.70, 5.90])

# scalar math
print("\n+1 to each array: ", array+1)
print("\n-1 to each array: ", array-1)
print("\n*2 to each array: ", array*2)
print("\n/2 to each array: ", array/2)
print("\npow2 to each array: ", array**2)


#vectorized math 
print(np.sqrt(array))
print(np.round(arrayfloat))
print(np.floor(arrayfloat))
print(np.ceil(arrayfloat))
print(np.pi * array ** 2)

#comparison
scores = np.array([91, 55, 100, 73, 82, 64])


print(scores == 100)
print(scores >= 100)
#select adnd return elenets that are less then 60 and assing em zero 
scores[scores < 60] = 0
print(scores)
