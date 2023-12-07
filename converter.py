import requests
import json

API_KEY = 'fca_live_e186I1zpfQRcxn9NsZGyM3Q0jRmemCd4bDkC9j4C'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD","CAD","EUR","AUD","BRL"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid entry.")
        return None

while True:
    base = input("Type the base currency (q for quit): ").upper()
    if base == "Q":
        break
    qttBase = int(input("Type the quantity for conversion: "))
    currency = input("In witch currency? ").upper()

    data = convert_currency(base)

    if not data:
        continue

    print(f"{qttBase} {base}'s is equal to {round(qttBase * data[currency], 2)} {currency}'s")