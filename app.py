while True:
    # Get the two numbers from the user
    A = float(input("\nEnter value for A: "))
    B = float(input("Enter value for B: "))

    # Ask the user to choose the operation
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter your choice (1, 2, 3, or 4): ")

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
    elif choice == '4':
        if B == 0:
            print("\nError: Cannot divide by zero!")
        else:
            result = A / B
            print(f"\nResult: {A} / {B} = {result}")
    else:
        print("\nInvalid choice!")

    # Ask the user if they want to continue
    # .strip().lower() handles spaces and uppercase letters (like 'Y' or 'yes')
    repeat = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
    
    if repeat != 'yes' and repeat != 'y':
        print("\nThank you for using the calculator! Goodbye.")
        break  # This exits the loop and ends the program
    