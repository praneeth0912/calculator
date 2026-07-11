while True:
    # Get the two numbers from the user
    A = float(input("Enter value for A: "))
    B = float(input("Enter value for B: "))

    # Ask the user to choose the operation
    print("\nChoose an operation:")
    print("1. Subtraction (-)")
    print("2. Subtraction (*)")
    choice = input("Enter your choice (1 or 2): ")

    # Perform the calculation based on the choice
    if choice == '1':
        result = A - B
        print(f"\nResult: {A} - {B} = {result}")
    elif choice == '2':
        result = A * B
        print(f"\nResult: {A} * {B} = {result}")
    else:
        print("\nInvalid choice! Please select 1 or 2.")

    # Ask the user if they want to perform another operation
    print("\n" + "-"*30)
    repeat = input("Do you want to perform another operation? (yes/no): ").strip().lower()
    print("-"*30 + "\n")
    
    # If the user says anything other than 'yes' or 'y', break the loop and exit
    if repeat not in ['yes', 'y']:
        print("Goodbye!")
        break