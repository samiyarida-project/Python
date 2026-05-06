import operations

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("+, -, *, /, **")
op = input("Enter operator: ")

if op == "+":
    print("Result:", operations.add(a, b))

elif op == "-":
    print("Result:", operations.sub(a, b))

elif op == "*":
    print("Result:", operations.mul(a, b))

elif op == "/":
    print("Result:", operations.div(a, b))


elif op == "**":
    print("Result:", operations.power(a, b))

else:
    print("Invalid operator")
