while True:
    print('\n○●○●○●○●basic calculator●○●○●○●○\n')
    try:
        a = float(input('            Enter Number_ '))
        b = float(input('            Enter Number_ '))
    except ValueError:
        print("\n    Error: please enter numbers only!")
        continue

    print("\n          Choose an operation:")
    print("            type-1 to (+)")
    print("            type-2 to (-)")
    print("            type-3 to (/)")
    print("            type-4 to (*)")

    while True:
        try:
            c = int(input('          Enter Your Choice_ '))
            if c in [1, 2, 3, 4]:
                break
            else:
                print('\n            type 1-4 only!\n')
        except ValueError:
            print("\nError:please enter choice as number (1-4)!\n")

    if c==1:
        print(f'\n              Result: {a+b:.2f}')
    elif c==2:
        print(f'\n              Result: {a-b:.2f}')
    elif c==3:
        if b == 0:
            print("\n    Error: cannot divide by zero")
        else:
            print(f'\n              Result: {a/b:.2f}')
    elif c==4:
        print(f'\n              Result: {a*b:.2f}')
    else:
        print('\n        invalid')

    print()

    
    while True:
        again = input("\n        Want to continue? (y/n): ").lower()
        if again in ["y", "n"]:
            break
        else:
            print("\n      Please enter only 'y' or 'n'.")

    if again == "n":
        break