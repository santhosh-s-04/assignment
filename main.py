import headercode as hd
i=0
z=int(input("Enter the file path choice you want to choose: (1)user file path location (2)default file path location:"))
hd.crd.path(z)

while(i!=4):
    i=int(input("Enter the crd operation choice: (1)create (2)read (3)delete (4)exit: "))
    if(i==1):
        key=input("Enter the key:")
        value=input("enter the value:")
        hd.crd.create(key,value)
    elif(i==2):
        key=input("Enter the key:")
        hd.crd.read(key)
    elif(i==3):
        key=input("Enter the key:")
        hd.crd.delete(key)
    elif(i==4):
        print("program has been exited!!!!")
    else:
        print("enter the correct option")
