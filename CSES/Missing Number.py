num = int(input())
list = [int(num) for num in input().split(" ", num-1)]
sum =  (num*(num+1))/2
sum_1 = 0
for i in list:
   sum_1 += i
print(int(sum - sum_1))