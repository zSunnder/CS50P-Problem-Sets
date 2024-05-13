def main():
    camelcase()

def camelcase():
    camel = input("camelCase: ").lower().strip()
    camels = {
        "name": "name",
        "firstname": "first_name",
        "preferredfirstname": "preferred_first_name"
    }
    if camel in camels:
        print(f"snake_case: {camels[camel]}")
    else:
        print("Invalid camelCase input. Please try again.")

main()
