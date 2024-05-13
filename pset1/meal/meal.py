def main():
    time = input("What time is it? ")
    times = convert(time)

    if times >= 7.0 and times <= 8.0:
        print("breakfast time")
    elif times >= 12.0 and times <= 13.0:
        print("lunch time")
    elif times >= 18.0 and times <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)
    hours = float(hours)
    times = hours + minutes/60
    return times


if __name__ == "__main__":
    main()
