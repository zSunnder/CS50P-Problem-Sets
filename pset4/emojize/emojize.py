import emoji
user = input("Input: ")
emoji = emoji.emojize(user, language="alias")
print(f"Output: {emoji}")
