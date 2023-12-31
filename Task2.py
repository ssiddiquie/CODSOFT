while True:
    print("Calculator")
    print("Operations:")
    print("1- Add")
    print("2- Multiply")
    print("3- Division")
    print("4- Subtract")

    x = input("Press button 1-4 based on the desired operation\n")

    if x not in ['1', '2', '3', '4']:
        print("Invalid")
    else:
        a = float(input("Enter 1st number\n"))
        b = float(input("Enter 2nd number:\n"))

        if x == '1':
            result = a + b
        elif x == '2':
            result = a * b
        elif x == '3':
            if b == 0:
                print("Error: It cannot be divided by 0")
                exit()
            else:
                result = a / b
        else:
            result = a - b

        print(f"Result = {result}")
        print("Press 1 to continue")
        print("Press 2 to exit")
        ans = input()

        if ans == '1':
            continue
        elif ans == '2':
            exit()
        else:
            print("Invalid choice. Exiting.")
            exit()
