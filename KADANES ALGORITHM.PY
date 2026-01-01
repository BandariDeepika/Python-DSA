#KADANES ALGORITHAM
#maximum element in ana array using subarray
'''arr=[10,20,30,-40]
maxi=arr[0]
curr=0
for i in range(len(arr)):
    curr=curr+arr[i]
    if maxi<curr:
        maxi=curr
    if curr<0:
        curr=0
print(maxi)'''

#maximum length of subarray 
'''arr=[-2,-1,0,1,2]
maxlength=0
k=3
for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):
        sum=sum+arr[j]
        if sum<=k:
            if maxlength<j-i+1:
                maxlength=j-i+1    
print(maxlength)'''
