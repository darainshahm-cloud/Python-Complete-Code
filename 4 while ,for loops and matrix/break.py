num=int(input("Enter the number "))
i=0
while i<=num:
    if i==6:
        break       # immediately stop the loops and exit
    i+=1
    print(i," ")


value=int(input("Enter the value "))
for i in range (1,value):
    if i==10:
        break
    print(i)