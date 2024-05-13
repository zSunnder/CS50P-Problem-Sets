def main():
    einstein_calc()

def einstein_calc():
    user = int(input("M: "))
    c = 300000000
    print("E:", user * pow(c, 2))

if __name__ == "__main__":
    main()
