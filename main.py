import tkinter as tk
from tkinter import ttk
import random

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("SOMBFAN")
        self.master.geometry("800x600")

        # Create a Notebook (tabs)
        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Calculator Tab
        calculator_tab = ttk.Frame(self.notebook)
        self.notebook.add(calculator_tab, text="Calculator")
        self.create_calculator(calculator_tab)

        # Random Number Generator Tab
        rng_tab = ttk.Frame(self.notebook)
        self.notebook.add(rng_tab, text="Random Number Generator")
        self.create_rng_tab(rng_tab)

        # Multiples of 2 Tab
        multiples_of_two_tab = ttk.Frame(self.notebook)
        self.notebook.add(multiples_of_two_tab, text="Multiples of 2")
        self.create_multiples_of_two_tab(multiples_of_two_tab)

        # Nearest Prime Number Tab
        nearest_prime_tab = ttk.Frame(self.notebook)
        self.notebook.add(nearest_prime_tab, text="Nearest Prime Number")
        self.create_nearest_prime_tab(nearest_prime_tab)

    def create_calculator(self, tab):
        self.entry_var = tk.StringVar()
        entry = tk.Entry(tab, textvariable=self.entry_var, justify="right", font=('Arial', 14))
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(tab, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_rng_tab(self, tab):
        # Entry for min value
        min_var = tk.DoubleVar()
        min_entry = tk.Entry(tab, textvariable=min_var, width=10)
        min_label = tk.Label(tab, text="Min:")
        min_label.grid(row=0, column=0)
        min_entry.grid(row=0, column=1, padx=5, pady=5)

        # Entry for max value
        max_var = tk.DoubleVar()
        max_var.set(187)  # Default max value
        max_entry = tk.Entry(tab, textvariable=max_var, width=10)
        max_label = tk.Label(tab, text="Max:")
        max_label.grid(row=0, column=2)
        max_entry.grid(row=0, column=3, padx=5, pady=5)

        # Checkbox for float/int
        float_var = tk.BooleanVar()
        float_checkbox = tk.Checkbutton(tab, text="Float", variable=float_var)
        float_checkbox.grid(row=1, column=0, padx=5, pady=5)

        # Entry for max floating points
        float_points_var = tk.IntVar()
        float_points_var.set(4)  # Default max floating points
        float_points_entry = tk.Entry(tab, textvariable=float_points_var, width=3)
        float_points_label = tk.Label(tab, text="Float Points:")
        float_points_label.grid(row=1, column=1, padx=5, pady=5)
        float_points_entry.grid(row=1, column=2, padx=5, pady=5)

        # Button to generate random number
        generate_button = tk.Button(tab, text="Generate", command=lambda: self.generate_random_number(min_var.get(), max_var.get(), float_var.get(), float_points_var.get()))
        generate_button.grid(row=2, column=0, columnspan=3, pady=10)

        # Display area for random number
        self.result_var = tk.StringVar()
        result_label = tk.Label(tab, text="Result:")
        result_label.grid(row=3, column=0)
        result_entry = tk.Entry(tab, textvariable=self.result_var, state='readonly')
        result_entry.grid(row=3, column=1, columnspan=2, pady=5)

    def create_multiples_of_two_tab(self, tab):
        # Entry for the number
        num_var = tk.IntVar()
        num_entry = tk.Entry(tab, textvariable=num_var, width=10)
        num_label = tk.Label(tab, text="Number:")
        num_label.grid(row=0, column=0)
        num_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to calculate next power of two
        calculate_button = tk.Button(tab, text="Calculate", command=lambda: self.calculate_next_power_of_two(num_var.get()))
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Display area for result
        self.next_power_of_two_var = tk.StringVar()
        result_label = tk.Label(tab, text="Next Power of Two:")
        result_label.grid(row=2, column=0)
        result_entry = tk.Entry(tab, textvariable=self.next_power_of_two_var, state='readonly')
        result_entry.grid(row=2, column=1, pady=5)

    def create_nearest_prime_tab(self, tab):
        # Entry for the number
        num_var = tk.IntVar()
        num_entry = tk.Entry(tab, textvariable=num_var, width=10)
        num_label = tk.Label(tab, text="Number:")
        num_label.grid(row=0, column=0)
        num_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to calculate nearest prime number
        calculate_button = tk.Button(tab, text="Calculate", command=lambda: self.calculate_nearest_prime(num_var.get()))
        calculate_button.grid(row=1, column=0, pady=10)

        # Display area for result
        self.nearest_prime_var = tk.StringVar()
        result_label = tk.Label(tab, text="Nearest Prime Number:")
        result_label.grid(row=2, column=0)
        result_entry = tk.Entry(tab, textvariable=self.nearest_prime_var, state='readonly')
        result_entry.grid(row=2, column=1, pady=5)

        # Buttons for next and previous prime numbers
        next_prime_button = tk.Button(tab, text="Next Prime", command=lambda: self.calculate_next_prime(num_var.get()))
        prev_prime_button = tk.Button(tab, text="Previous Prime", command=lambda: self.calculate_previous_prime(num_var.get()))

        next_prime_button.grid(row=3, column=0, pady=5)
        prev_prime_button.grid(row=3, column=1, pady=5)

    def on_button_click(self, button):
        current_entry_text = self.entry_var.get()

        if button == 'C':
            # Clear the entry
            self.entry_var.set('')
        elif button == '=':
            try:
                # Evaluate the expression and set the result in the entry
                result = eval(current_entry_text)
                self.entry_var.set(result)
            except Exception as e:
                # Handle errors (e.g., division by zero)
                self.entry_var.set('Error')
        else:
            # Update the entry with the clicked button
            self.entry_var.set(current_entry_text + button)

    def generate_random_number(self, min_val, max_val, is_float, float_points):
        if is_float:
            result = round(random.uniform(min_val, max_val), float_points)
        else:
            result = random.randint(int(min_val), int(max_val))

        self.result_var.set(result)

    def calculate_next_power_of_two(self, number):
        result = 2 ** (number.bit_length())
        self.next_power_of_two_var.set(result)

    def calculate_nearest_prime(self, number):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        lower_prime = number - 1
        upper_prime = number + 1

        while not (is_prime(lower_prime) or is_prime(upper_prime)):
            lower_prime -= 1
            upper_prime += 1

        result = lower_prime if is_prime(lower_prime) else upper_prime
        self.nearest_prime_var.set(result)

    def calculate_next_prime(self, number):
        next_prime = number + 1
        while not self.is_prime(next_prime):
            next_prime += 1
        self.nearest_prime_var.set(next_prime)

    def calculate_previous_prime(self, number):
        prev_prime = number - 1
        while not self.is_prime(prev_prime):
            prev_prime -= 1
        self.nearest_prime_var.set(prev_prime)

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
