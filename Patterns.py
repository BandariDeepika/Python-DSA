#1
#2 3
#4 5
#7 8 9 10
n=4
num=1
for row in range(1,n+1):
  for col in range(1,row+1):
    print(num=,end=" ")
    num=num+1
  print()
#1
#1 2
#1 2 3
#1 2 3 4
n=4
num=1
for rows in range(1,n+1):
    rows=rows+1
    for col in range(1,rows+1):
        print(col,end=" ")
        col=col+1
print()

#*
#* *
#* * *
#* * * *
n=4    
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print("*",end=" ")
    print()

#* * * *
#* * *
#* *
#*
n=4
for rows in range(n,0,-1):
    for col in range(rows,0,-1):
        print("*",end=" ")
    print()
#TIME COMPLEXICITY IS O(n)square
# to reduced time complexity
n=4
for i in range(1,n+1):
        print("*"*i)
#TIME COMPLEXICITY IS O(n)
#* * * *
*     *
*     *
*     *
* * * *
n=4
for row in range(n):
    for col in range(n):
        if row ==  0 or row== n-1 or col== 0 or col== n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#Another way 
n=4
for row in range(n):
    for col in range(n):
        if row == 0 or row==n-1 or col==n-row-1 or row+col == n-1:
            print("*",end=" ")
        
            print(" ",end=" ")
    print()

