def main():
    file()

def file():
    user = input("File name: ")
    user_input = user.strip().lower().split(".")
    extension = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }
    if user_input[1] in extension:
        print(extension[user_input[1]])
    else:
        print("application/octet-stream")


main()
