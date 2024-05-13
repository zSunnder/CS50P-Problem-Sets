def main():
    user = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    match user:
        case "42" | "Forty Two" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()
