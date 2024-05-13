def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False

    if s[0:2].isalpha() == False:
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False


    indx = 0
    while indx < len(s):
        if s[indx].isalpha() == False:
            if s[indx] == "0":
                return False
            else:
                break
        indx += 1
    for c in s:
        marks = {'.', ' ', '!', '?'}
        if c in marks:
            return False

    return True


main()
