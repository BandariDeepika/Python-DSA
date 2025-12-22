
#merge sorting

'''def merge(arr,low,mid,high):
    p1=low
    p2=mid+1
    new_arr=[]
    while p1<=mid and p2<=high:
        if arr[p1]<=arr[p2]:
            new_arr.append(arr[p1])
            p1=p1+1
        else:
            new_arr.append(arr[p2])    
            p2=p2+1
    while p1<=mid:
       new_arr.append(arr[p1])
       p1=p1+1
    while p2<=high:
       new_arr.append(arr[p2])
       p2=p2+1
    idx=low
    for i in range(len(new_arr)):
        arr[idx]=new_arr[i]
        idx=idx+1
def divide(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2     
    divide(arr,low,mid)
    divide(arr,mid+1,high)
    merge(arr,low,mid,high)
arr=[21,42,44,49,23,23,0,-1,17]
print(arr)
divide(arr,0,len(arr)-1)
print(arr)'''
       
       
'''def merge(arr,low,mid,high):
    p1=low
    p2=mid+1
    new_arr=[]
    while p1<=mid and p2<=high:
        if arr[p1]<=arr[p2]:
            new_arr.append(arr[p1])
            p1=p1+1
        else:
            new_arr.append(arr[p2])
            p2=p2+1
    while p1<=mid:
        new_arr.append(arr[p1])
        p1=p1+1
    while p2<=high:
        new_arr.append(arr[p2])
        p2=p2+1
    idx=low
    for i in range(len(new_arr)):
        arr[idx]=new_arr[i]
        idx=idx+1
def divide(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    divide(arr,low,mid)
    divide(arr,mid+1,high)
    merge(arr,low,mid,high)
arr=[21,42,44,49,23,23,0,-1,17]
print(arr)
divide(arr,0,len(arr)-1)
print(arr)'''


'''
