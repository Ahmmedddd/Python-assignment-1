import tkinter as tk

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author, "available": True}
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book["title"] == title and book["available"]:
                book["available"] = False
                return f"Checked out: {title} by {book['author']}"
        return f"Book not found or already checked out: {title}"

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title and not book["available"]:
                book["available"] = True
                return f"Returned: {title} by {book['author']}"
        return f"Book not found or not checked out: {title}"

    def list_books(self):
        available_books = [book["title"] for book in self.books if book["available"]]
        return available_books

class LibraryUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.library = Library("My Library")

        # Create labels and entry fields
        self.title_label = tk.Label(root, text="Title:")
        self.title_entry = tk.Entry(root)
        self.author_label = tk.Label(root, text="Author:")
        self.author_entry = tk.Entry(root)

        # Create buttons
        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.checkout_button = tk.Button(root, text="Check Out Book", command=self.check_out_book)
        self.return_button = tk.Button(root, text="Return Book", command=self.return_book)
        self.list_button = tk.Button(root, text="List Books", command=self.list_books)

        # Pack widgets
        self.title_label.pack()
        self.title_entry.pack()
        self.author_label.pack()
        self.author_entry.pack()
        self.add_button.pack()
        self.checkout_button.pack()
        self.return_button.pack()
        self.list_button.pack()

        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.pack()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        self.library.add_book(title, author)
        self.output_text.insert(tk.END, f"Added: {title} by {author}\n")

    def check_out_book(self):
        title = self.title_entry.get()
        result = self.library.check_out_book(title)
        self.output_text.insert(tk.END, result + "\n")

    def return_book(self):
        title = self.title_entry.get()
        result = self.library.return_book(title)
        self.output_text.insert(tk.END, result + "\n")

    def list_books(self):
        books = self.library.list_books()
        self.output_text.insert(tk.END, "Available Books:\n")
        for book in books:
            self.output_text.insert(tk.END, f"- {book}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryUI(root)
    root.mainloop()


# PRACTICE QUESTIONS:1.CAlCULATE FACTORIAl:
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
number = 4
print(f"The factorial of {number} is {factorial(number)}")
output:  The factorial of 4 is 24.

#   2.	Check prime number:
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True
number = 17  
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

output:  17 is a prime number.

# 3.	SUM OF DIGITS:

def sum_of_digits(n):
  
    total = 0

    number_str = str(abs(n))
    
    for digit in number_str:
        total += int(digit)

    return total


number = 12345  
result = sum_of_digits(number)
print(f"The sum of digits in {number} is {result}")

OUTPUT:
The sum of digits in 12345 is 15

# 4.	Reverse a string:

def reverse_string(input_string):
    return input_string[::-1]

original_string = "things will get reverse!"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)

output: Original string: things will get reverse!
Reversed string: !esrever teg lliw sgniht

# 5.	Even and Odd number:

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = 50  
result = check_even_odd(num)
print(f"{num} is {result}.")

output: 50 is Even.

# 6.	Maximum and minimum:

numbers = [5, 2, 9, 1, 6, 3, 8]

maximum = max(numbers)
minimum = min(numbers)

print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

OUTPUT: Maximum: 9 Minimum: 1
  
# 7.	Count Vowels and Consonants:

def count_vowels_and_consonants(input_string):
    
    input_string = input_string.lower()

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count


text = "I Study in UMT"
vowels, consonants = count_vowels_and_consonants(text)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")

OUTPUT:   Vowels: 4  Consonants: 7



# 8.	 GCD (Greatest Common Divisor):

import math
numbers = [14, 55, 78]
gcd = math.gcd(*numbers)

print(f"The GCD of {numbers} is {gcd}")

OUTPUT: The GCD of [14, 55, 78] is 1


