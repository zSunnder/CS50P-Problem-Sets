def main():
    calculator()

def calculator():
    x,y,z = (input("Expression: ")).split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        print(f"{x+z:.1f}")
    elif y == "-":
        print(f"{x-z:.1f}")
    if y == "*":
        print(f"{x*z:.1f}")
    if y == "/":
        print(f"{x/z:.1f}")

main()

