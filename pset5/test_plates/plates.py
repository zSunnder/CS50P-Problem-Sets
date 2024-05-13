def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #debe tener 6 caracteres y minimo 2
    #debe tener 2 letras al comienzo
    #numero debe ser en el final como aaa333 y no puede comenzar con 0
    #no punto coma y eso
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
if __name__ == "__main__":
    main()
