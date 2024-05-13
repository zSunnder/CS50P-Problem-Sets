def main():
    amountDue = 50

    while amountDue > 0:
        user = int(input("Insert coin: "))

        if user == 25:
            amountDue -= user
        elif user == 10:
            amountDue -= user
        elif user == 5:
            amountDue -= user
        else:
            print("Invalid coin. Please insert a valid coin.")

        if amountDue > 0:
            print(f"Amount Due: {amountDue}")
        else:
            print(f"Change Owed: {-amountDue}")

main()
