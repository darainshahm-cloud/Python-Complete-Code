#age >=18
#certificate ->true

age=int(input("Enter your age "))
certificate=input("Enter the bool value true or false for the certificate ")
if age>=18:
    if certificate=="true":
        print("you are hired")
    else:
        print("can not hire due to no certificate ")
else:
    print("can not hired because your age is less than 18 ")