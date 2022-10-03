import requests
def fetch_data():
    convert_from = input("Enter First Currency:")
    convert_into = input("Enter  Second Currency:")
    amount = float(input("Enter The Amount Which You Want To Convert:"))

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_into}&from={convert_from}&amount={amount}"
    payload = {}
    headers = {
      "apikey": "TR3zZYWW7Yegw7pAZxxU6xMopy6abRIB"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    total = float(amount*result['info']['rate'])
    print("Conversion Rate:", total)

fetch_data()
