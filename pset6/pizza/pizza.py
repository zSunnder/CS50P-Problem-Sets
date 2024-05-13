import csv
from tabulate import tabulate
import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) > 1:
    user = sys.argv[1]
    name,file_csv = user.split(".")
    if file_csv == "csv":
        file_csv = True
    else:
        file_csv = False
        sys.exit("Not a CSV file")

else:
    sys.exit("Too few command-line arguments")

try:
    if file_csv == True:
        if sys.argv[1] == "regular.csv":
            pizza = []

            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                table = []
                headers = list(next(reader))
                for row in reader:
                    table.append([row[0], row[1], row[2]])
                print(tabulate(table, headers, tablefmt="grid"))

        elif sys.argv[1] == "sicilian.csv":
            pizza = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                table = []
                headers = list(next(reader))
                for row in reader:
                    table.append([row[0], row[1], row[2]])
                print(tabulate(table, headers, tablefmt="grid"))

        else:
            sys.exit("File does not exist")


except FileNotFoundError:
    sys.exit("File does not exist")

