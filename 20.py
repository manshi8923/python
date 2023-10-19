#python program to remove the duplicate no of the list
num=[2,2,4,6,3,4,6,1]
unique=[]
for n in num:
    if n not in unique:
        unique.append(n)
print(unique)