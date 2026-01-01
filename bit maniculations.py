#using sort
#arr=[21,42,49,23,0,-1,17,17,42,42,44,23]
#arr.sort()
#frq={}
#for i in range(len(arr)):
    #if arr[i] not in frq:
     #   frq[arr[i]]=1
    #elif arr[i] in frq:
     #   frq[arr[i]]+=1
#print(frq)

#duplicates using sets finfing
     
'''arr=[21,42,49,23,0,-1,17,17,42,42,44,23]
new_arr=list(set(arr))
if len(arr)==len(new_arr):
    print("good array")
else:
    print("bad array")
print(arr)'''

#bit maniculations

'''num1=5
num2=4
print(num1 |num2)
print(num1&num2)
print(num1^num2)
print(~num1)
print(num1<<2)
print(num2>>2)'''

#find even or odd using bit maniculations
'''n=int(input())
if n&1:
    print("odd")
else:
    print("even")'''
#2 power n
'''n=int(input())
print(1<<n)'''
