
def zerostocentre(arr):
    n = arr.count(0)
    a = []
    for _ in range(n):
        arr.remove(0)
        a.append(0)
    return arr[:len(arr)//2] + a + arr[len(arr)//2:]


arr = [0,0,1,2,3,4,5,6,0,0,0]
print(zerostocentre(arr))