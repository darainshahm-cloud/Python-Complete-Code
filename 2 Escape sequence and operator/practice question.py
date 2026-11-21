# Q 01
#two numbers from user and print the sum , differnce , product and remainder.
"""
num1=int(input("Enter first number: "))
num2=int(input("Enter the second number: "))
sum=num1+num2
diff=num1-num2
product=num1*num2
remainder=num1%num2

print("Sum:", sum)
print("Difference:", diff)
print("Product:", product)
print("Remainder:", remainder)
"""
"""
#Q 2 even or odd check
num=int(input("Enter the number "))
print(num%2==0)

"""

# Q # 03 Check the person is eligible for voting or not age>=18 and age>=60 senior citizen
"""
age=int(input("Enter your age: "))
print("Eligible for voting:", age>=18) or print("Senior citizen:", age>=60)

"""

# Q 04 3 subjects marks and print total , average using f string
"""
subj1=int(input("Enter marks for subject 1: "))
subj2=int(input("Enter marks for subject 2: "))
subj3=int(input("Enter marks for subject 3: "))
total =subj1+subj2+subj3
avg=total/3
print(f"total marks {total} and average marks {avg}")
"""
# Q # 05 result of number raised to the powe of 3 and print // and % for that number

"""
num=int(input("Enter the number: "))
result=num**3
print("the result of number to the power 3 is ",result)
print(num//3)
print(num%4)
"""

# Q # 06 find product without using * operator
a=int(input("Enter the number 1 "))
b=int(input("Enter the number 2 "))
product=(a//1)+(a//1)+(a//1)+(a//1)+(a//1)
print(product)