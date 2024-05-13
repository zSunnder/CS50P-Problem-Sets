def main():
    face()

def face():
    emoji = {
        ":)": "🙂",
        ":(": "🙁"
    }
    output = ""
    user = input().split()
    for word in user:
        output += emoji.get(word, word) + " "
    print(output.strip())

main()


