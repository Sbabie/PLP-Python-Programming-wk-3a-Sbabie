import tkinter as tk
from tkinter import messagebox

def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount of 20% or more."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def apply_discount():
    try:
        price = float(entry_price.get())
        discount = float(entry_discount.get())
        final_price = calculate_discount(price, discount)

        if discount >= 20:
            result = f"Discount applied. Final price: ${final_price:.2f}"
        else:
            result = f"No discount applied. Final price: ${final_price:.2f}"

        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Discount Calculator")

tk.Label(root, text="Original Price:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_price = tk.Entry(root)
entry_price.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Discount Percent:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_discount = tk.Entry(root)
entry_discount.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate", command=apply_discount).grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()


