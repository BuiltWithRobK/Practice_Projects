import requests

def get_crypto_price(crypto_id="bitcoin"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": crypto_id, "vs_currencies": "usd"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        price = data.get(crypto_id, {}).get("usd", "N/A")
        return f"The current price of {crypto_id.capitalize()} is ${price}"
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    while True:
        crypto = input("\nEnter a cryptocurrency (e.g., bitcoin, ethereum, dogecoin) or 'exit' to quit: ").lower()
        if crypto == "exit":
            print("Goodbye!")
            break
        print(get_crypto_price(crypto))
