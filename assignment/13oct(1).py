num1=int(input("enter num1\n"))
num2=int(input("enter num2\n"))
num3=int(input("enter num3\n"))
max = num1 if (num1>num2 and num1>num3) else (num2 if num2>num3 else num3)
print(max)

