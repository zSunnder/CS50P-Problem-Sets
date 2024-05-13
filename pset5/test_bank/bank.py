def main():
    user = input("greeting: ").lower().replace(",","").split()
    print(value(user))


def value(greeting):
    if greeting [0] == "hello":
        money = int(0)
        return money
    elif greeting[0][0] == "h":
        money = int(20)
        return money
    else:
        money = int(100)
        return money


if __name__ == "__main__":
    main()
