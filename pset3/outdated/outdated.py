def main():
    outdate()

def outdate():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            user_input = input("Date: ").strip()
            month, day, year = user_input.split("/")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except:
            try:
                month2, day2, year = user_input.split(" ")
                for i in range(len(months)):
                    if month2 == months[i]:
                        month = i + 1
                        day = day2.replace(",", "")
                        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                            break
            except:
                pass

    print(f"{year}-{int(month):02}-{int(day):02}")   # Formato de salida: YYYY-MM-DD

main()
