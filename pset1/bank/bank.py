def main():
    greeting()

def greeting():
    user = input("Greeting: ")
    greeting = user.lower().replace(",","").split()
    if greeting [0] == "hello":
        print("$0")
    elif greeting[0][0] == "h":
        print("$20")
    else:
        print("$100")










main()
