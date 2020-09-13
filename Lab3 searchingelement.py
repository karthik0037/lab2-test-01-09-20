def searching(a,s):
    flag=1
    for i in range(len(a)):
        if a[i]==s:
            flag=0
            break
    if flag==0:
        return i
    else:
        return "not found"
x=int(input("enter the size of array"))
a=['0']*x
for i in range(x):
      b=int(input("enter a element"))
      a[i]=b
y=int(input("enter the number to be searched"))
h=searching(a,y)
print(y,"found at index",h)
