"""
90 above -> A
80 - 90 -> B
70 - 80 -> C
60 - 70 -> D
60 below -> F """

marks=int(input("Enter the marks "))
if marks>=90 and marks <=100:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")
elif marks>=60 and marks<70:
    print("D")
elif marks>=0 and marks<60:
    print("Fail")
else:
    print("invalid input")