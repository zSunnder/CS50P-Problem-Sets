from validator_collection import validators, checkers, errors
import sys

def main():
    user = input("What's your email addres? ")
    try:
        email = validators.email(user)
        if email:
            print("Valid")
        else:
            print("Invalid")
    except errors.EmptyValueError:
        print("Invalid")
    except errors.InvalidEmailError:
        print("Invalid")


if __name__ == "__main__":
    main()
