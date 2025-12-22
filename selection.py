# selection minimum element in an array
arr=[21,42,44,49,23,0,-1,17]
    [-1,42,44,49,23,0,21,17]
    [-1,0,44,49,23,42,21,17]
    [-1,0,17,49,23,42,21,17]
    [-1,0,17,21,23,42,49,44]
    [-1,0,17,21,23,42,44,49]
arr=[21,42,44,49,23,0,-1,17]
for i in range(len(arr)-1):
    mini=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[mini]:
            mini=j
    new=arr[mini]
    arr[mini]=arr[i]
    arr[i]=new
print(arr,end=" ")
###############################
arr=list(map(int,input().split()))
target=67
p1=0
p2=len(arr)-1
arr[p1]+arr[p2]
while p1<p2:
    if target==arr[p1]+arr[p2]:
        print(arr[p1],arr[p2])
        p1=p1+1
        p2=p2-1
    elif target>arr[p1]+arr[p2]:
        p1=p1+1  
    elif target<arr[p1]+arr[p2]:
        p2=p2-1
