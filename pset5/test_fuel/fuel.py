def main():
    user = input("fuel: ")
    output = convert(user)
    percent = gauge(output)
    print(percent)


def convert(fraction):
    x,y = fraction.split("/")
    x =  int(x)
    y = int(y)
    if x > y:
        raise ValueError()
    else:
        decimal = x/y
        porcentaje = decimal * 100
        return round(porcentaje)


def gauge(percentage):
    try:
        if 1 >= percentage:
            return "E"
        elif percentage >= 99:
            return "F"
        elif percentage >= 2:
            return str(percentage)+"%"

    except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
