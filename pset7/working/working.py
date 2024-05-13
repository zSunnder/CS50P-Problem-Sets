import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    hour = re.search(r"^([0-9]+):?([0-9]+)? (AM|PM) to ([0-9]+):?([0-9]+)? (AM|PM)$", s)
    if hour:
        hour1 = int(hour.group(1))
        minute1 = hour.group(2)
        time1 = hour.group(3)
        hour2 = int(hour.group(4))
        minute2 = hour.group(5)
        time2 = hour.group(6)

#time1 AM
        if time1 == "AM":
            if hour1 == 12:
                hour1 = hour1 - 12
            else:
                pass
#time1 PM
        elif  time1 == "PM":
            if hour1 == 12:
                pass
            else:
                hour1 = hour1 + 12
                hour1
#time 2 AM
        if time2 == "AM":
            if hour2 == 12:
                hour2 = hour2 - 12

        elif time2 == "PM":
            if hour2 == 12:
                pass
            else:
                hour2 = hour2 + 12

#convert
        if minute1:
            if minute1 == "60":
                raise ValueError
            else:
                start = f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
                return start

        else:
            return f"{hour1:02}:00 to {hour2:02}:00"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
