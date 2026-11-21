#implicit Python automatically converts one data type to another data type. This is called implicit type conversion or coercion.

num1=100
num2=200.0

print(num1+num2)

num3="100"
num4="20"
print(num3+num4) # concatenation of strings

print(int(num3)+int(num4)) #explicit type conversion or type casting

a=3.7
print(int(a))