import sys
import requests

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = r.json()
    amount = sys.argv[1]
    amount = float(amount)
    if amount >= 1:
        value = float(r["bpi"]["USD"]["rate_float"])
        n = amount * value
        print(f"${n:,.4f}")
        sys.exit()
except requests.RequestException:
    sys.exit("Missing command-line argument")
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
