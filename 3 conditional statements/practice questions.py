# Q 7 take number as input check whether it is positive , negative or zero
"""
num=int(input("Enter the number "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

    """
"""
# Q 8 check the greater number and print equal if they are
num1=int(input("Enter the number 1 "))
num2=int(input("Enter the number 2 "))
if num1>num2:
    print(num1, " is greater")
elif num2>num1:
    print(num2 , " is greater ")
else:
    print("Both are equal")
"""

# Q 9 student marks as input and print grade according to the marks
"""
90 and above A
75-89 B
60-74 C
40-59 D
below 40 F

marks=int(input("Enter the marks "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=75 and marks<=89:
    print("Grade B")
elif marks>=60 and marks<=74:
    print("Grade C")
elif marks>=40 and marks<=59:
    print("Grade D")
else:   
    print("Fail")
    """

# Q 10 take a year as input and check whether it is leap year or not
year=int(input("Enter the year "))
if year%4==0 and year%100!=0 or year%400==0:
    print(year, "is a leap year ")
else:
    print(year ," is not a leap year")
