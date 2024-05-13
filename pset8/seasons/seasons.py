from datetime import date
import inflect
import re
import sys

class Time:
    def __init__(self, birth):
        self.birth = birth
        self.today = date.today()

    def __str__(self):
        p = inflect.engine()
        time = self.today - self.birth
        minutes = int(time.days)*24*60
        words = p.number_to_words(minutes, andword="").capitalize()
        return f"{words} minutes"

    @classmethod
    def get(cls):
        birth = input("Birth: ")
        valid = re.search(r"^([0-9]{4})([0-9]+)-([0-9]+)$", birth)
        if valid:
            birth = date(int(valid.group(1)), int(valid.group(2)), int(valid.group(3)))
            return cls(birth)
        else:
            sys.exit("Invalid Date")


def main():
    birth = Time.get()
    print(birth)


if __name__ == "__main__":
    main()
