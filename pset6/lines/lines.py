import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if len(sys.argv) > 1:
    user = sys.argv[1]
    argv = user.split(".")
    if argv[1] == "py":
        argv = True
    elif argv[1] != "py":
        sys.exit("Not a Python file")

else:
    sys.exit("Too few command-line arguments")

try:
    if argv == True:
        with open(user) as file:
            line = 0
            for lines in file:
                if not lines.lstrip().startswith("#") and lines.lstrip() != "":
                    line += 1
            print(line)
    elif argv == False:
        sys.exit("Not a Python file")


except FileNotFoundError:
    sys.exit("File does not exist")
