import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
list_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    user = input("Input: ")
    figlet.setFont(font=random.choice(list_fonts))
    print(figlet.renderText(user))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    user = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(user))
else:
    sys.exit("Invalid usage")



