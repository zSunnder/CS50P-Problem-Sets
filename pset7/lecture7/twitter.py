import re

url = input("URL: ")

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url,re.IGNORECASE):
    print(f"username: ",  matches.group(1))
