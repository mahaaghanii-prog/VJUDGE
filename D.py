b = int(input())
arr = list(map(int,input().split()))
unique = set(arr)
sort= sorted(unique)
second_last=len(sort)-2
last=len(sort)
# array=[2,3,4,4,5]   
# 3:4:1
print(sort[-2])  #[5]