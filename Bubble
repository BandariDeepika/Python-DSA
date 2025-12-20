arr=[21,42,44,49,23,0,-1,17]
    [21,42,44,23,0,-1,17,49]
    [21,42,23,0,-1,17,44,49]
    [21,23,0,-1,17,42,44,49]
    [21,0,-1,17,23,42,44,49]
    [0,-1,17,21,23,42,44,49]
    [-1,0,17,21,23,42,44,49]
    [-1,0,17,21,23,42,44,49]
#sorting of array
arr=[21,42,44,49,23,0,-1,17]
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            new=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=new
print(arr,end=" ")
# using functions
def sorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                new=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=new
arr=[21,42,44,49,23,0,-1,17]
sorting(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
#ascending order to desecending 
def sorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]<arr[j+1]:
                new=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=new
arr=[21,42,44,49,23,0,-1,17]
sorting(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
