import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        number = re.search(r"^(\w+)\.(\w+)\.(\w+)\.(\w+)$", ip)
        if number:
            number1 = int(number.group(1))
            number2 = int(number.group(2))
            number3 = int(number.group(3))
            number4 = int(number.group(4))
            if 0 <= number1 < 256 and 0 <= number2 < 256 and 0 <= number3 < 256 and 0 <= number4 < 256:
                return True
            else:
                return False

        else:
            return False



    except ValueError:
        return False



if __name__ == "__main__":
    main()
