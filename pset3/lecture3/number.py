while True:
    try:
        x = int(input("What is x? "))

    except ValueError:
        print("X is no a interger")
    else:
        break
print(f"x is {x}")


