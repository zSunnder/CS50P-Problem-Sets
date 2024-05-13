import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'<iframe(?:.*)? src="(https?://(?:www\.)?youtube\.com/embed/xvFZjo5PgG0)"(?:.*)?></iframe>', s)
    if url:
        link = url.group(1)
        #re.sub creo no se aqui el link https://www.youtube.com/embed/xvFZjo5PgG0 y ya
        result = re.sub(r"https?://(?:www\.)?youtube\.com/embed/xvFZjo5PgG0", "https://youtu.be/xvFZjo5PgG0", link)
        return result
    else:
        return None


if __name__ == "__main__":
    main()
