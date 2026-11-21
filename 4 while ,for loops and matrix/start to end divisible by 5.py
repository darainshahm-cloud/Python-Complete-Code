start=int(input("enter the num1 "))
end=int(input("enter the num2 "))
i=start
print("Numbers divisible by 5 ")
while i<=end:
    if i%5==0:
        print(i," ")
    i+=1