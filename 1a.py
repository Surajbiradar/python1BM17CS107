list1=[]
list2=[]
a = int(input("enter numbers to add"))
for i in range(a):
    b= int(input("enter number"))
    list1.append(b)

for i in list1:
    if i%2==0:
       list2.append(i)
print(list2)
    
