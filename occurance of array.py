#find the first ocuurance of give array
arr=[-1,0,17,21,23,42,42,42,44,49]
target=42
low=0
high=len(arr)-1
indx= -1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        indx=mid
        high=mid-1  #ekkada high update change cheyale - cheyali
    elif arr[mid]<target:
        low=mid+1
    elif arr[mid]>target:
        high=mid-1
print(indx)

#find the last ocuurance of give array
arr=[-1,0,17,21,23,42,42,42,44,49]
target=42
low=0
high=len(arr)-1
indx= -1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        indx=mid
        low=mid+1 #ekkada high update change cheyale + chyali
    elif arr[mid]<target:
        low=mid+1
    elif arr[mid]>target:
        high=mid-1
print(indx)
#if it print both values first and last ocurrane value
arr=[-1,0,17,21,23,42,42,42,44,49]
target=42
low=0
high=len(arr)-1
indx= -1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        indx=mid
        low=mid+1#ekkada high update change cheyale + chyali
    elif arr[mid]<target:
        low=mid+1
    elif arr[mid]>target:
        high=mid-1
print(indx)
target=42
low=0
high=len(arr)-1
indx= -1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        indx=mid
        high=mid-1#ekkada high update change cheyale + chyali
    elif arr[mid]<target:
        low=mid+1
    elif arr[mid]>target:
        high=mid-1
print(indx)
