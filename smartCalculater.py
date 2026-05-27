import numpy as np

print("="*35)
print("   WELCOME TO SMART CALCULATOR   ")
print("="*35)

while True:
    print("\n1. Addition       2. Subtraction")
    print("3. Multiplication 4. Division")
    print("5. Power          6. Modulus")
    print("7. Exit")
    
    try:
        choice = int(input("\nEnter choice (1-7): "))
    except ValueError:
        print("!! Please enter a valid option !!")
        continue

    if choice == 7:
        print("\nExiting... Thank you!")
        break

    if choice in [1, 2, 3, 4, 5, 6]:
        try:
            limit = int(input("How many numbers do you want to enter? "))
            if limit <= 0:
                print("!! Please enter at least 1 number !!")
                continue
        except ValueError:
            print("!! Invalid count !!")
            continue

        numbers = []
        print(f"\n--- Please enter your {limit} numbers ---")
        
        for i in range(limit):
            try:
                val = float(input(f"Number {i+1}: "))
                numbers.append(val)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        arr = np.array(numbers)
        print("-" * 30)

        # Operations
        if choice == 1: #Addition
            print(f"TOTAL SUM: {np.sum(arr)}")

        elif choice == 2:#Subtraction
            result = arr[0] - np.sum(arr[1:])
            print(f"TOTAL SUBTRACTION: {result}")
            
        elif choice == 3: #Multiplication
            print(f"TOTAL MULTIPLICATION: {np.prod(arr)}")
            
        elif choice == 4: #Division
            result = arr[0]
            error = False
            for num in arr[1:]:
                if num != 0:
                    result /= num
                else:
                    print("Error: Division by zero!")
                    error = True
                    break
            if not error: print(f"TOTAL DIVISION: {result}")

        elif choice == 5: #Power
            result = arr[0]
            for num in arr[1:]:
                result **= num
            print(f"TOTAL POWER: {result}")

        elif choice == 6: #Modulus
            result = arr[0]
            error = False
            for num in arr[1:]:
                if num != 0: result %= num
                else:
                    print("Error: Modulus by zero!")
                    error = True
                    break
            if not error: print(f"TOTAL MODULUS: {result}")
            
        print("-" * 30)