import numpy as np

def zerostocentre(arr):
  '''
  a Fucntion to move all zeros to center of an array
  '''
  n = arr.count(0)
  arr = list(filter(lambda a: a != 0, arr))
  return arr[:len(arr)//2] + list(np.zeros(n, dtype=int)) + arr[len(arr)//2:]


arr = [0,0,1,2,3,4,5,6,0,0,0]
print(zerostocentre(arr))
