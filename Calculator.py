First_Number = int(input("Enter First Number : "))
print("+\n-\n*\n/")
Operation = input("Pick an Operation : ")
Second_Number = int(input("Enter Second Number : "))
if Operation == "+":
    Total = First_Number + Second_Number
    print(f"{First_Number} + {Second_Number} = {Total}")
elif Operation == "-":
    Total = First_Number - Second_Number
    print(f"{First_Number} - {Second_Number} = {Total}")
elif Operation == "*":
    Total = First_Number * Second_Number
    print(f"{First_Number} * {Second_Number} = {Total}")
elif Operation == "/":
    Total = First_Number / Second_Number
    print(f"{First_Number} / {Second_Number} = {Total}")
print(f"Enter 'y' to continue calculation with {Total} or 'n' to start new calculation or 'x' to exit ;")
Choice_Need = input()

while Choice_Need != "x":

    if Choice_Need == "y":
        Operation = input("Pick an Operation : ")
        Second_Number = int(input("Enter Second Number : "))
        if Operation == "+":
            print(f"{Total} + {Second_Number} = {Total+Second_Number}")
            Total = Total + Second_Number
        elif Operation == "-":
            print(f"{Total} - {Second_Number} = {Total-Second_Number}")
            Total = Total - Second_Number
        elif Operation == "*":
            print(f"{Total} * {Second_Number} = {Total*Second_Number}")
            Total = Total * Second_Number
        elif Operation == "/":
            print(f"{Total} / {Second_Number} = {Total/Second_Number}")
            Total = Total / Second_Number
    elif Choice_Need == "n":
        First_Number = int(input("Enter First Number : "))
        print("+\n-\n*\n/")
        Operation = input("Pick an Operation : ")
        Second_Number = int(input("Enter Second Number : "))
        if Operation == "+":
            Total = First_Number + Second_Number
            print(f"{First_Number} + {Second_Number} = {Total}")
        elif Operation == "-":
            Total = First_Number - Second_Number
            print(f"{First_Number} - {Second_Number} = {Total}")
        elif Operation == "*":
            Total = First_Number * Second_Number
            print(f"{First_Number} * {Second_Number} = {Total}")
        elif Operation == "/":
            Total = First_Number / Second_Number
            print(f"{First_Number} / {Second_Number} = {Total}")
    print(f"Enter 'y' to continue calculation with {Total} or 'n' to start new calculation or 'x' to exit ;")
    Choice_Need = input()
    if Choice_Need == "x":
        break
        