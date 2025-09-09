# 12345 -> 34512
def Left_rotation(d, arr):
    n = len(arr)
    #arrn = [0]*n
    arr[0:n-d%n] , arr[n-d%n:n] = arr[d%n:n] , arr[0:d%n]
    return arr

arr = list(map(int,input().split()))
d = int(input())

print("The Array Rotated for ",d," times: ", Left_rotation(d,arr))