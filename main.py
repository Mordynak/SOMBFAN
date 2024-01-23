import tkinter as tk
from tkinter import ttk
import random

class SOMBFAN:
    def __init__(self, master):
        self.master = master
        self.master.title("SOMBFAN")

        # Create a Notebook (tabs)
        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Random Number Generator Tab
        rng_tab = ttk.Frame(self.notebook)
        self.notebook.add(rng_tab, text="Random Number")
        self.create_rng_tab(rng_tab)

        # Multiples of 2 Tab
        multiples_of_two_tab = ttk.Frame(self.notebook)
        self.notebook.add(multiples_of_two_tab, text="Texture Size")
        self.create_multiples_of_two_tab(multiples_of_two_tab)

        # Nearest Prime Number Tab
        nearest_prime_tab = ttk.Frame(self.notebook)
        self.notebook.add(nearest_prime_tab, text="Prime Numbers")
        self.create_nearest_prime_tab(nearest_prime_tab)

        # Calculate prime numbers on startup
        self.calculate_nearest_prime(256)  # You can replace 256 with your desired initial value

    def create_rng_tab(self, tab):
        # Entry for min value
        min_var = tk.DoubleVar()
        min_entry = tk.Entry(tab, textvariable=min_var, width=10)
        min_label = tk.Label(tab, text="Min:")
        min_label.grid(row=0, column=0)
        min_entry.grid(row=0, column=1, padx=5, pady=5)

        # Entry for max value
        max_var = tk.DoubleVar()
        max_var.set(8192)  # Default max value
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
        num_var = tk.IntVar(value=256)
        num_entry = tk.Entry(tab, textvariable=num_var, width=10)
        num_label = tk.Label(tab, text="Input:")
        num_label.grid(row=0, column=0)
        num_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to calculate nearest power of two
        calculate_button = tk.Button(tab, text="Calculate", command=lambda: self.calculate_nearest_power_of_two(num_var.get()))
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons to divide and multiply by 2
        divide_button = tk.Button(tab, text="Divide by 2", command=lambda: self.divide_by_two())
        multiply_button = tk.Button(tab, text="Multiply by 2", command=lambda: self.multiply_by_two())

        divide_button.grid(row=3, column=0, pady=5)
        multiply_button.grid(row=3, column=1, pady=5)

        # Display area for result
        self.next_power_of_two_var = tk.StringVar()
        result_label = tk.Label(tab, text="Result:")
        result_label.grid(row=2, column=0)
        result_entry = tk.Entry(tab, textvariable=self.next_power_of_two_var, state='readonly')
        result_entry.grid(row=2, column=1, pady=5)

        # Call calculate_nearest_power_of_two initially
        self.calculate_nearest_power_of_two(2)  # Default value set to 2

    def divide_by_two(self):
        current_result = self.next_power_of_two_var.get()
        try:
            divided_result = int(current_result) // 2
            self.next_power_of_two_var.set(divided_result)
        except ValueError:
            pass  # Handle the case where the result is not an integer

    def multiply_by_two(self):
        current_result = self.next_power_of_two_var.get()
        try:
            multiplied_result = int(current_result) * 2
            self.next_power_of_two_var.set(multiplied_result)
        except ValueError:
            pass  # Handle the case where the result is not an integer

    def calculate_nearest_power_of_two(self, number):
        lower_power = 2 ** (number.bit_length() - 1)
        higher_power = 2 ** (number.bit_length())

        distance_lower = abs(number - lower_power)
        distance_higher = abs(number - higher_power)

        result = lower_power if distance_lower <= distance_higher else higher_power
        self.next_power_of_two_var.set(result)

    def create_nearest_prime_tab(self, tab):
        # Entry for the number
        num_var = tk.IntVar(value=256)
        num_entry = tk.Entry(tab, textvariable=num_var, width=10)
        num_label = tk.Label(tab, text="Input:")
        num_label.grid(row=0, column=0)
        num_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to calculate number
        calculate_button = tk.Button(tab, text="Calculate", command=lambda: self.calculate_nearest_prime(num_var.get()))
        calculate_button.grid(row=1, column=0, pady=10)

        # Display area for nearest prime
        nearest_prime_label = tk.Label(tab, text="Nearest Prime:")
        nearest_prime_label.grid(row=2, column=0)
        self.nearest_prime_var = tk.StringVar()
        nearest_prime_result = tk.Entry(tab, textvariable=self.nearest_prime_var, state='readonly')
        nearest_prime_result.grid(row=2, column=1, pady=5)

        # Display area for prime neighbors
        neighbors_label = tk.Label(tab, text="Prime Neighbors:")
        neighbors_label.grid(row=3, column=0)
        self.neighbors_result = tk.Text(tab, height=8, width=20, wrap="none", state='disabled', takefocus=0)
        self.neighbors_result.grid(row=3, column=1, pady=5)



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

    def calculate_nearest_power_of_two(self, number):
        lower_power = 2 ** (number.bit_length() - 1)
        higher_power = 2 ** (number.bit_length())

        distance_lower = abs(number - lower_power)
        distance_higher = abs(number - higher_power)

        result = lower_power if distance_lower <= distance_higher else higher_power
        self.next_power_of_two_var.set(result)

    def find_nearest_prime(self, number):
        lower_prime = number - 1
        upper_prime = number + 1

        while not (self.is_prime(lower_prime) or self.is_prime(upper_prime)):
            lower_prime -= 1
            upper_prime += 1

        return lower_prime if self.is_prime(lower_prime) else upper_prime

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def calculate_nearest_prime(self, number):
        try:
            if number < 2:
                return  # Return if the input number is less than 2

            def generate_prime_list(center, count, direction):
                primes = []
                current = center
                while len(primes) < count:
                    current += direction
                    if self.is_prime(current):
                        primes.append(current)
                return primes

            nearest_prime = self.find_nearest_prime(number)
            lower_primes = generate_prime_list(nearest_prime, 4, -1)
            higher_primes = generate_prime_list(nearest_prime, 4, 1)

            # Update the nearest_prime_var with the nearest prime
            self.nearest_prime_var.set(nearest_prime)

            # Update the neighbors_result widget with the prime neighbors
            self.neighbors_result.config(state='normal')
            self.neighbors_result.delete(1.0, tk.END)
            for prime in lower_primes + higher_primes:
                self.neighbors_result.insert(tk.END, f"{prime}\n")
            self.neighbors_result.config(state='disabled')

        except ValueError:
            # Handle the case where the input is not a valid integer
            pass

def main():
    root = tk.Tk()
    app = SOMBFAN(root)
    root.mainloop()

if __name__ == "__main__":
    main()
