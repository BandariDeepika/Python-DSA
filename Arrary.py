# To Print All Elements in Given Array
array=[1,2,3,4,5]
for i in range(len(arr)):
  print(arr[i])
  
#To Find Given Elemnt in array Using Flags
#Find K in Given array
#K Not Found
#K Found
arr=[1,2,3,4,5,6]
k=int(input("enter a k value"))
if k in arr:
    print("k found at index",arr.index(k))
else:
    print("k not found at index")
arr=list(map(int,input().split()))
k=int(input('enter k value:'))
flag=False
index=-1
for i in range(len(arr)):
  if k==arr[i]:
    flag=True
    indx=i
  if flag:
    print("k found at index",indx)
  else:
    print("k is not found")

#To Find Sum of Pairs in Given Array
arr=[1,12,15,16,13,95,76]
target=25
for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    if arr[i]+arr[j]==target:
      print(arr[i],arr[j])

#Find Highest Number of One's
arr=[1,0,1,1,0,1,1,1,0,0,1,1]
count=0
maxi=0
for i in range(len(arr)):
    if arr[i]==1:
        count=count+1
        if maxi<count:
            maxi=count
    else:
        count=0
print(maxi)
# Find Second Largest Number Element
arr=[1,95,45,25,63,74,21,98]
if arr[0]>arr[1]:
    first=arr[0]
    second=arr[1]
else:
    first=arr[1]
    second=arr[0]
for i in range(2,len(arr)):
    if first<arr[i]:
        second=first
        first=arr[i]
    elif second<arr[i] and arr[i]!=first:
        second=arr[i]
print(second)
