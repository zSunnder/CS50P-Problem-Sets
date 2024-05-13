def main():
    cal()

def cal():
    user = input("Item: ").lower().strip()
    items = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        "kiwifruit": 90,
        "pear": 100,
    }
    if user in items:
        print(f"Calories: {items[user]}")
    elif user == "tomato":
        print()
    else:
        print("Item not found in the database.")

main()

