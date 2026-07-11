<<<<<<< HEAD
=======
while True:
    # Get three numbers from the user
    A = float(input("Enter value for A: "))
    B = float(input("Enter value for B: "))
    C = float(input("Enter value for C: "))

    # Ask the user to choose the operation
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    choice = input("Enter your choice (1, 2, or 3): ")

    # Perform the calculation based on the choice
    if choice == '1':
        result = A + B + C
        print(f"\nResult: {A} + {B} + {C} = {result}")
    elif choice == '2':
        result = A - B - C
        print(f"\nResult: {A} - {B} - {C} = {result}")
    elif choice == '3':
        result = A * B * C
        print(f"\nResult: {A} * {B} * {C} = {result}")
    else:
        print("\nInvalid choice! Please select 1, 2, or 3.")

    # Ask the user if they want to perform another operation
    print("\n" + "-"*30)
    repeat = input("Do you want to perform another operation? (yes/no): ").strip().lower()
    print("-"*30 + "\n")
    
    # If the user says anything other than 'yes' or 'y', break the loop and exit
    if repeat not in ['yes', 'y']:
        print("Goodbye!")
        break
>>>>>>> aa0548c7aad5a9a38ab00082e533e0aa316e1293
