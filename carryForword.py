arr=[23,24,10,61,7,12,14,96]
carry=[]
maxi=arr[0]
for i in range(len(arr)):
  if maxi<arr[i]:
    maxi=arr[i]
    carry.append(maxi)
  else:
    carry.append(maxi)
  print(carry)
