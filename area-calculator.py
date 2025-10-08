import math

while True:
    print("=" * 18)
    print("Area Calculator 📐")
    print("=" * 18)
    print("\n1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    choice = input("\nWhich shape (1-5): ")
    print()

    if choice == '1':
        print("--- Triangle Area Calculation ---")
        base = float(input("Base: "))
        height = float(input("Height: "))

        if base > 0 and height > 0:
            area = (base * height) / 2
            print(f"\nArea: {area}")
        else:
            print("\nBase and height must be positive numbers.")

    elif choice == '2':
        print("--- Rectangle Area Calculation ---")
        length = float(input("Length: "))
        width = float(input("Width: "))

        if length > 0 and width > 0:
            area = length * width
            print(f"\nArea: {area}")
        else:
            print("\nLength and width must be positive numbers.")

    elif choice == '3':
        print("--- Square Area Calculation ---")
        side = float(input("Side: "))

        if side > 0:
            area = side ** 2
            print(f"\nArea: {area}")
        else:
            print("\nSide must be a positive number.")

    elif choice == '4':
        print("--- Circle Area Calculation ---")
        radius = float(input("Radius: "))

        if radius > 0:
            area = math.pi * (radius ** 2)
            print(f"\nArea: {area:.2f} (using π ≈ {math.pi:.4f})")
        else:
            print("\nRadius must be a positive number.")

    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break # Terminates the infinite loop

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    print("\n" + "=" * 30 + "\n")
