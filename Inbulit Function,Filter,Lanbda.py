#Withouth using for loop using Filters even numbers finding 
def even(element):
  return element%2==0:
arr=[-1,0,17,21,23,42,49,50,52,53]
new_arr=list(filter(even,arr))
print(new_arr)

#using inbulit function lamb
odd numbers finding
def odd(element):
  return element%2!==0
arr=[-1,0,17,21,23,42,49,50,52,53]
new_arr=list(filter(odd,arr))
print(new_arr)

#Using Lambda
arr=[-1,0,17,21,23,42,49,50,52,23]
new_arr=list(map(lambda element:element%2==0,arr)
             print(new_arr)
