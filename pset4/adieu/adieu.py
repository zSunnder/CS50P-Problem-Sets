import inflect
i = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ").capitalize().strip()
        names.append(name)

    except EOFError:
            print()
            break
n = i.join(names)
print(f"Adieu, adieu, to {n}")
