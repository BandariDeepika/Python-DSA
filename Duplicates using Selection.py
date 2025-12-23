#printing Duplicates using selection
arr=[21,42,44,49,23,0,-1,17,49]
for i in range(len(arr)-1):
    mini=i
    for j in range(i+1,len(arr)):
        if arr[j]>arr[mini]:
           mini=j
    new=arr[mini]
    arr[mini]=arr[i]
    arr[i]=new
    flag=True
for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        flag=False                
if flag:
    print("good array")
else:
        print("bad array")
