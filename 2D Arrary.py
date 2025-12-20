#To Print 2D Array
arr2D=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,3,]]
print(len(arr2D))
for row in range(len(arr2D)):
    for col in range(len(arr2D[row])):
        print(arr2D[row][col],end=" ")
    print()
#Sum of Each Element in given Array
arr2D=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,3,]]
for row in range(len(arr2D)):
    res=0
    for col in range(len(arr2D[row])):
        res=res+arr2D[row][col]
    print(res)
  
