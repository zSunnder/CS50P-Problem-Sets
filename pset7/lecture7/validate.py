import re

email = input("wat email ")

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("valid")

else:
    print("invalid")
