def add(a,b):
    print("Addition:",a+b)
def sub(a,b):
    print("Subtraction:",a-b)
def mul(a,b):
    print("Multiplication:",a*b)
def div(a,b):
    print("Division:",a/b)
def mod(a,b):
    print("Modulus:",a%b)
def power(a,b):
    print("Power:",a**b)

while True:
    print("\n Select your choice")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.Exit")

    choice = int(input("Enter choice: "))
    if choice >= 1 and choice <= 7:
        a = int(input("Enter a value: "))
        b = int(input("Enter b value: "))
        if choice == 1:
            add(a,b)
        elif choice == 2:
            sub(a,b)
        elif choice == 3:
            mul(a,b)
        elif choice == 4:
            div(a,b)
        elif choice == 5:
            mod(a,b)
        elif choice == 6:
            power(a,b)
        elif choice == 7:
            break
        else:
            print("Invalid Choice...")
