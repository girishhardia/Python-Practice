a = input("Write something ")
b = int(len(a))
if b % 2 == 0:
    e = int(b/2)
    print("middle letters are" , a[(e)-1] ,"and", a[e])
    
else:
     c = int((b+1)/2)
    
     print("middle letter is" , a[(c)-1])
print("first letter is " , a[0])
print("last letter is " , a[-1])
