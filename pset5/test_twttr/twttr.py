def main():
    user = input("Input: ")
    shorten(user)




def shorten(word):
    vowels = ["A", "a", "e", "E", "i", "I", "o", "O", "u", "U"]
    output = ""
    for char in word:
        if char not in vowels:
            output += char
    print(output)


if __name__ == "__main__":
    main()
