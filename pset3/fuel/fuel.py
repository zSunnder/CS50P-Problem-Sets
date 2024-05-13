def main():
    x = fuel()
    if x < 1:
        print("E")
    elif x >= 99:
        print("F")
    elif x >= 2:
        print(f"{int(x)}%")

def fuel():
    while True:
        try:
            num, den = map(int, input("Fraction: ").split("/"))
            decimal = num / den
            porcentaje = decimal * 100
            return round(porcentaje)

        except (ValueError, ZeroDivisionError):
            pass

main()

