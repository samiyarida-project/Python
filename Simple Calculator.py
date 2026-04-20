#Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation")


choice = input("Enter choice (1,2,3,4,5,6): ")

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error!Cannot divide by zero")
elif choice == "5":
   print("Result:", num1 % num2)
elif choice == "6":
   print("Result:", num1 ** num2)        

else:
    print("Invalid choice")


#Output:
#Enter first number: 6789
#Enter second number: 9876
#Choose operation:
#1. Addition
#2  Subtraction    
#3. Multiplication
#4. Division
#5. Modulus
#6. Exponentiation
#Enter choice (1,2,3,4,5,6): 3
#Result: 67048164.0

   
