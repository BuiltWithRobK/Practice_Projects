import tkinter as tk
from tkinter import messagebox
import requests

def get_crypto_price():
    crypto_id = entry.get().lower()
    if not crypto_id:
        messagebox.showwarning("Input Error", "Please enter a cryptocurrency name.")
        return

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": crypto_id, "vs_currencies": "usd"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        data = response.json()
        price = data.get(crypto_id, {}).get("usd", "N/A")

        if price == "N/A":
            messagebox.showerror("Error", "Invalid cryptocurrency name. Try again.")
        else:
            result_label.config(text=f"The price of {crypto_id.capitalize()} is ${price}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")

# Create the main window
root = tk.Tk()
root.title("Crypto Price Checker")
root.geometry("400x300")

# GUI Elements
tk.Label(root, text="Enter Cryptocurrency:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Price", font=("Arial", 12), command=get_crypto_price)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()

