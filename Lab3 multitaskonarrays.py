n=int(input("enter the size of the array"))
a=['0']*n
b=['0']*n
for i in range(n):
    c=int(input("enter a element"))
    a[i]=c
print("copying elements from a to b array")    
for j in range(n):
    b[j]=a[j]
print(b)    
print("removing duplicates")
print("before removing duplicates")
print(a)
print("after removing duplicates")
res = [] 
[res.append(a[x]) for x in range(len(a)) if a[x] not in res]
print(res)
k=int(input("enter the position of number to be removed"))
a.remove(res[k])
print(res)
print("enter a number to be searched")
s=int(input())
for i in range(len(res)):
    if res[i]==s:
        print("number found at",i)
print(res)        
#copy
#remove duplicates
#delete at kth element
#search an item
#display contents
