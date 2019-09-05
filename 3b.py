import random
l=12
s=" "
for i in range(0,12):
    if(i<=2):
       s=s+chr(random.randrange(97,123))
    elif(i>2 and i<=5):
        s=s+chr(random.randrange(65,91))
    elif(i>5 and i<=8):
        s=s+str(random.randrange(0,10))
    else:
        s=s+chr(random.randrange(33,48))
print(s)

