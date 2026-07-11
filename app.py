# Get the two numbers from the user
A = float(input("Enter value for A: "))
B = float(input("Enter value for B: "))

# Ask the user to choose the operation
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
choice = input("Enter your choice (1, 2, or 3): ")

# Perform the calculation based on the choice
if choice == '1':
    result = A + B
    print(f"\nResult: {A} + {B} = {result}")
elif choice == '2':
    result = A - B
    print(f"\nResult: {A} - {B} = {result}")
elif choice == '3':
    result = A * B
    print(f"\nResult: {A} * {B} = {result}")
else:
    print("\nInvalid choice! Please run the program again and select 1, 2, or 3.")