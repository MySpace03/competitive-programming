n = input()
count = 1
max_1 = 0
for i in range(0,len(n)-1,1):
    if  n[i] == n[i+1]:
        count+=1
    else:
        max_1 = max(max_1,count)
        count = 1
print(max(max_1,count))