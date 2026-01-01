#to find sum in the given range

''''def suminrange(prefix,left,right):
    if left==0:
        return prefix[right]
    else:
        return prefix[right]-prefix[left-1]
arr=[10,20,30,40,50,60]
prefix=[]
prefix.append(arr[0])
for i in range(1,len(arr)):
    prefix.append(prefix[i-1]+arr[i])
print(suminrange(prefix,0,3))
print(suminrange(prefix,1,4))
print(suminrange(prefix,2,3))
print(suminrange(prefix,1,5))'''


'''arr=[10,20,30,40,50,60]
for i in range(0,len(arr)-1):
    if arr[i]%2==0:
        print(even)'''

'''arr=[23,24,10,61,7,12,14,96]
carry=[]
maxi=arr[0]
for i in range(len(arr)):
    if maxi<arr[i]:
        maxi=arr[i]
        carry.append(maxi)
    else:
        carry.append(maxi)
print(carry) '''
