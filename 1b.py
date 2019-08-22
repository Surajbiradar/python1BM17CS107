def func(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return func(n-1)+func(n-2)
n=int(input("Enter the number:"))
for i in range (0,n):
    print(func(i))
