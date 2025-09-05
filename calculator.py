import math

def welcome():
    print("===================================")
    print(" ************  Welcome to Python Calculator ************    ")
    print("   Supports Scientific Functions   ")
    print("===================================\n")

def show_menu():
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√)")
    print("7. Factorial (!)")
    print("8. Logarithm (log base 10)")
    print("9. Natural Log (ln)")
    print("10. Sine (sin)")
    print("11. Cosine (cos)")
    print("12. Tangent (tan)")
    print("13. Exit")

def calculator():
    welcome()

    while True:
        show_menu()
        choice = input("\nEnter choice (1-13): ")

        if choice == '13':
            print("\nThank you for using Python Calculator 😊")
            break

        try:
            if choice in ['1','2','3','4','5']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if choice == '1':
                    print("Result:", x + y)
                elif choice == '2':
                    print("Result:", x - y)
                elif choice == '3':
                    print("Result:", x * y)
                elif choice == '4':
                    if y != 0:
                        print("Result:", x / y)
                    else:
                        print("Error: Division by zero!")
                elif choice == '5':
                    print("Result:", x ** y)

            elif choice == '6':
                x = float(input("Enter number: "))
                print("Result:", math.sqrt(x))

            elif choice == '7':
                x = int(input("Enter integer: "))
                print("Result:", math.factorial(x))

            elif choice == '8':
                x = float(input("Enter number: "))
                print("Result:", math.log10(x))

            elif choice == '9':
                x = float(input("Enter number: "))
                print("Result:", math.log(x))

            elif choice == '10':
                angle = float(input("Enter angle in degrees: "))
                print("Result:", math.sin(math.radians(angle)))

            elif choice == '11':
                angle = float(input("Enter angle in degrees: "))
                print("Result:", math.cos(math.radians(angle)))

            elif choice == '12':
                angle = float(input("Enter angle in degrees: "))
                print("Result:", math.tan(math.radians(angle)))

            else:
                print("Invalid choice, try again!")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()