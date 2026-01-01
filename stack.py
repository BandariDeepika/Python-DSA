#stacks -1 is always top will print
'''stck=[]
stck.append(10)
stck.append(20)
stck.append(30)
stck.append(40)
while stck:
    print(stck[-1])
    stck.pop()
else:
    print("no element")'''

#palindron using queues
'''str=input("enter the string:")
stck=[]
for i in str:
    stck.append(i)
rev=""
while stck:
    
    rev=rev+stck[-1]
    stck.pop()
if str==rev:
    print("palindron")
else:
    print("not palindron")'''


'''string="[{()}]"
stck=[]
stck=[]
hashmap={')':'(','}':'{',']':'['}
flag=True
for i in range(len(string)):
    if string[i] in "({[":
        stck.append(string[i])
    else:
        if not stck or stck[-1]!=hashmap[string[i]]:
            flag=False
            break
        stck.pop()
if flag and stck==[]:
    print("vaild")
else:
    print("not vaild")'''
