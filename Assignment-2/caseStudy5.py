import calculator as cal

print("-"*25)
print("1. ADD\n2. Substract\n3. Multiply\n4. Divivde\n")
choice = int(input("Choose Operation from above by selecting the Option Number:  "))
num1 = float(input("Enter Value 1: "))
num2 = float(input("Enter Value 2: "))

if choice == 1:
    print("Addition of ",num1," & ",num2," is: ",cal.add(num1,num2))
elif choice == 2:
    print("Substraction of ",num1," & ",num2," is: ",cal.sub(num1,num2))
elif choice == 3:
    print("Multiplication of ",num1," & ",num2," is: ",cal.mul(num1,num2))
elif choice == 4:
    print("Division of ",num1," & ",num2," is: ",cal.div(num1,num2))
else:
    print("Enter Valid Choice!")