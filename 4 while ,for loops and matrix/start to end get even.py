start=int(input("Enter the start value "))
end=int(input("Enter the end value "))
i=start
print("Even numbers are ")
while i<=end:
    if i%2==0:
        print(i)
    i+=1