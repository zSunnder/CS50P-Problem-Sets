import csv
import sys

def main():
    get_length()
    get_line()



def get_length():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

def get_line():
    try:
        students = []

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                names = row["name"].replace(" ", "").split(",")
                students.append({"last": names[0], "first": names[1], "house": row["house"]})


        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

            writer.writeheader()
            for row in students:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()




