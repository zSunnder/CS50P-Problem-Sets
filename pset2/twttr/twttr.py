def main():
    tweet()

def tweet():
    twt = input("Input: ").strip()
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    output = ""
    for char in twt:
        if char not in vowels:
            output += char
    print(f"Output: {output}")

main()
