import tkinter as tk
from tkinter import messagebox

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def calculate_price(self):
        shipping_cost = self.weight * 2
        return super().calculate_price() + shipping_cost

    def __str__(self):
        return f"{self.name} (Physical) - ${self.calculate_price():.2f}"

class DigitalProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def calculate_price(self):
        return super().calculate_price()

    def __str__(self):
        return f"{self.name} (Digital) - ${self.calculate_price():.2f}"

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product):
        if product in self.cart:
            self.cart.remove(product)

    def calculate_total_price(self):
        total_price = sum(product.calculate_price() for product in self.cart)
        return total_price

    def check_out(self):
        total_price = self.calculate_total_price()
        self.cart.clear()
        return f"Thank you for your purchase! Total Price: ${total_price:.2f}"

class ShoppingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart")
        
        self.cart = ShoppingCart()
        self.product_list = [
            PhysicalProduct("Laptop", 800, 5),
            DigitalProduct("Ebook", 10, 2),
            PhysicalProduct("Phone", 500, 2),
        ]
        self.selected_product = tk.StringVar(value=self.product_list[0].name)

        # Create and configure GUI elements
        tk.Label(root, text="Select a product:").pack()
        self.product_menu = tk.OptionMenu(root, self.selected_product, *[
            product.name for product in self.product_list
        ])
        self.product_menu.pack()
        tk.Button(root, text="Add to Cart", command=self.add_to_cart).pack()
        tk.Button(root, text="Remove from Cart", command=self.remove_from_cart).pack()
        tk.Button(root, text="Check Out", command=self.checkout).pack()
        self.cart_contents_label = tk.Label(root, text="Cart Contents:")
        self.cart_contents_label.pack()
        self.cart_contents_text = tk.Text(root, height=10, width=40)
        self.cart_contents_text.pack()
        self.clear_screen_button = tk.Button(root, text="Clear Screen", command=self.clear_screen)
        self.clear_screen_button.pack()
        self.update_cart_contents()

    def add_to_cart(self):
        product_name = self.selected_product.get()
        selected_product = next(
            (product for product in self.product_list if product.name == product_name),
            None
        )
        if selected_product:
            self.cart.add_product(selected_product)
            self.update_cart_contents()

    def remove_from_cart(self):
        product_name = self.selected_product.get()
        selected_product = next(
            (product for product in self.product_list if product.name == product_name),
            None
        )
        if selected_product:
            self.cart.remove_product(selected_product)
            self.update_cart_contents()

    def checkout(self):
        receipt = self.cart.check_out()
        self.update_cart_contents()
        messagebox.showinfo("Checkout", receipt)

    def update_cart_contents(self):
        cart_contents = [str(product) for product in self.cart.cart]
        self.cart_contents_text.delete(1.0, tk.END)
        self.cart_contents_text.insert(tk.END, "\n".join(cart_contents))

    def clear_screen(self):
        self.cart_contents_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()

    # PRACTICE QUESTIONS:

# 8.	 GCD (Greatest Common Divisor):

import math
numbers = [14, 55, 78]
gcd = math.gcd(*numbers)

print(f"The GCD of {numbers} is {gcd}")

# OUTPUT: The GCD of [14, 55, 78] is 1

# 9.	Check Leap Year:

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# OUTPUT:  2024 is a leap year.

#   10: Generate random password:
import secrets
import string

def generate_random_password(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
password_length = 10
random_password = generate_random_password(password_length)
print(f"Random Password: {random_password}")

# Output:
# Random Password: brv{QPE'9m


# 11. Count Words in a String:

def count_words(input_string):
    words = input_string.split()
    return len(words)
text = "this is our first python assignment."
word_count = count_words(text)
print(f"The number of words in the string is: {word_count}")

# OUTPUT: The number of words in the string is: 6

# 12. Binary to Decimal:

binary_number = "11110000"
decimal_number = int(binary_number, 2)
print(f"The decimal equivalent of {binary_number} is {decimal_number}")

# OUTPUT: The decimal equivalent of 11110000 is 240

# 13. String anagrams:
 
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")

# OUTPUT: 'listen' and 'silent' are anagrams.

# 14. Check Armstrong Number:
 
def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    return number == digit_sum
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


# OUTPUT: 153 is an Armstrong number.



