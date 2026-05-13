#1 
temperature = int(input("Enter temperature: "))

try:
    if temperature > 40:
        raise ValueError("Temperature is too high")
    print("Weather is normal")

except ValueError as error:
    print("Error:", error)

finally:
    print("Program ended successfully")
   #2 
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 % num2

except ValueError:
    print("Error: Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Modulo by zero is not allowed.")

else:
    print("Result =", result)

finally:
    print("Program execution completed.")


#Output:
#Enter temperature: 34
#Weather is normal
#Program ended successfully
#Enter first number: 35
#Enter second number: 67
#Result = 35
#Program execution completed.






