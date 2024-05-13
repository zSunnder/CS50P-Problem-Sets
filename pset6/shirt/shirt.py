import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 3:

    name1,ext1 = sys.argv[1].split(".")
    name2,ext2 = sys.argv[2].split(".")
    ext = ["png", "jpg", "jpeg"]
    if ext1 and ext2 in ext:

        if ext1 == ext2:
            pass

        else:
            sys.exit("Input and output have different extensions")

    else:
        sys.exit("Invalid output")

else:
    sys.exit("Too few command-line arguments")

#shirt
try:
    shirt = Image.open("shirt.png")
    size = shirt.size
    with Image.open(sys.argv[1]) as im:
        user = ImageOps.fit(image= im, size= size)
        user.paste(shirt, shirt)
        user.save(sys.argv[2])


except FileNotFoundError:
    sys.exit("Input does not exist")
