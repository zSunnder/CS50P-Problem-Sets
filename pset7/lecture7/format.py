import re


name = input("whats your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    first = matches.group(2)
    last = matches.group(1)
    name = f"{first} {last}"

print(f"hello, {name}")
