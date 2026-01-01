'''hashmap={
    "rollno":1202,
    "branch":"ECE",
    "year":2027
}
print(hashmap)
print(hashmap["rollno"])
hashmap["rollno"]=1203
print(hashmap["rollno"])'''

        

'''hashmap={
    "rollno":1789,
    "branch":"ECE",
    "year":2027
}
print(hashmap)
print(hashmap["rollno"])
hashmap["rollno"]=1203 # not get
hashmap["branch"]=EEE
print(hashmap["rollno"])
print(hashmap["Branch"])'''

#hashmap
'''hashmap={
    "rollno":1789,
    "branch":"ECE",
    "year":2027
}
print(hashmap)
print(hashmap["rollno"])
hashmap["rollno"]=1203
print(hashmap["rollno"])
print(hashmap.get("year"))
hashmap.pop("year")
print(hashmap)
hashmap.clear()
print(hashmap)'''

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
