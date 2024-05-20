import numpy as np

arr = np.array([
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
], dtype=int)

def traverseArray(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            print(arr[i][j], end="")
            print(" ",end="")
        print("")
traverseArray(arr)