#subarrays
'''arr=[1,2,3,4]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            print(arr[k],end=" ")
        print()'''
#sum of subarray time complexity O(n)^3
'''arr=[1,2,3,4]
sum=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            sum=sum+arr[k]
print(sum)'''

#sum of all the subarrays of maximum elements in array
'''arr=[-15,-20,-1,-3]
maxi=arr[0]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        count=0
        for k in range(i,j+1):
            count=count+arr[k]
        if maxi<count:
            maxi=count
print(maxi)'''
 # reduce time complexity above problem
'''arr=[20,3,5,90]
maxi=arr[0]
for i in range(len(arr)):
    count=0
    for j in range(i,len(arr)):
        count=count+arr[j]
        if maxi<count:
            maxi=count
print(maxi)'''

'''arr=[20,3,5,90]
maxi=0
k=10
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum=sum+arr[j]
        if maxi<sum and sum<=k:
            maxi=sum
print(maxi)'''

#8/12/25

'''arr=[1,2,3,4]
sum=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            sum=sum+arr[k]
print(sum)'''

'''arr=[10,-2,-3,5]
maxi=0
k=3
for i in range(1,len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum=sum+arr[j]
        if maxi<sum and sum<=k:
            maxi=sum
print(maxi)'''

'''arr=[10,2,-3,5] #not get
k=0
mini=arr[0]
for i in range(1,len(arr)):
    if mini>arr[i]:
        mini=arr[i]
maxi=mini
for i in range(len(arr)):
    count=0
    for j in range(i,len(arr)):
        count=count+arr[j]
        if maxi<count and count<=k:
            mini=count
print(mini)'''
