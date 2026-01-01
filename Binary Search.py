#binart search
#without function

'''arr=[-1,0,17,21,23,42,44,49]
k=23
lo=0
high=len(arr)-1
while lo<=high:

    mid=(lo+high)//2
    if arr[mid]==k:
        print("element found")
        break # to end if it is not use it will itertate
    elif arr[mid]<k:
        lo=mid+1
    elif arr[mid]>k:
        high=mid-1
else:
    print("element not found")'''
    
    
#using functions

'''def binary(arr):
    lo=0
    high=len(arr)-1
    while lo<=high:
        mid=(lo+high)//2 #index vlaue
    if arr[mid]==k:
        print("element found")
    elif k<arr[mid]:
        high=mid+1
    elif k>arr[mid]:
        lo=mid-1
        print("element not found")
arr=[-1,0,17,21,23,42,44,49]
k=12
binary(arr)'''


# using recursion
'''def binary(arr,lo,high,k):
    if lo>high:
        return -1
    mid=(lo+high)//2
    if arr[mid]==k:
        return mid
    elif arr[mid]<k:
        return binary(arr,mid+1,high,k)
    elif arr[mid]>k:
        return binary(arr,lo,mid-1,k)
arr=[-1,0,17,21,23,42,44,49]
k=44
print(binary(arr,0,len(arr)-1,k))'''
