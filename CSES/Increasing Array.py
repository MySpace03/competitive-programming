n = int(input())
arr = list(map(int,input().split()))
s = 0
for i in range(1,n,1):
    t = arr[i] - arr[i-1]
    if t<0:
        s += (-1*t) 
        arr[i] = arr[i-1]
print(s)