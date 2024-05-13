def main():
    shopping()


def shopping():
    item_dict = {}
    while True:
        try:
            item = input().lower().strip()
            if item in item_dict:
                item_dict[item] += 1
            else:
                item_dict[item] = 1
        except EOFError:
            for key in sorted(item_dict.keys()):
                print(item_dict[key], key.upper())
            break


main()
