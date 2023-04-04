import tkinter as tk

class NumberSystemConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Number System Converter")
        self.master.config(bg="#333")

        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self.master, text="Enter a number:", bg="#333", fg="#fff")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_entry = tk.Entry(self.master, bg="#444", fg="#fff")
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_base_label = tk.Label(self.master, text="From base:", bg="#333", fg="#fff")
        self.from_base_label.grid(row=1, column=0, padx=10, pady=10)

        self.from_base_var = tk.StringVar()
        self.from_base_var.set("2")
        self.from_base_dropdown = tk.OptionMenu(self.master, self.from_base_var, "2", "5", "6", "8", "10", "16")
        self.from_base_dropdown.config(bg="#444", fg="#fff", activebackground="#555", activeforeground="#fff", highlightthickness=0)
        self.from_base_dropdown.grid(row=1, column=1, padx=10, pady=10)

        self.to_base_label = tk.Label(self.master, text="To base:", bg="#333", fg="#fff")
        self.to_base_label.grid(row=2, column=0, padx=10, pady=10)

        self.to_base_var = tk.StringVar()
        self.to_base_var.set("10")
        self.to_base_dropdown = tk.OptionMenu(self.master, self.to_base_var, "2", "5", "6", "8", "10", "16")
        self.to_base_dropdown.config(bg="#444", fg="#fff", activebackground="#555", activeforeground="#fff", highlightthickness=0)
        self.to_base_dropdown.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = tk.Button(self.master, text="Convert", command=self.convert_number, bg="#444", fg="#fff", activebackground="#555", activeforeground="#fff", highlightthickness=0)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self.master, text="", bg="#333", fg="#fff")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def convert_number(self):
        number = self.input_entry.get()
        from_base = int(self.from_base_var.get())
        to_base = int(self.to_base_var.get())

        try:
            # Convert the input number to base 10
            decimal_number = int(number, from_base)

            # Convert the base 10 number to the desired base
            if to_base == 2:
                result = bin(decimal_number)[2:]
            elif to_base == 5:
                result = self.base_conversion(decimal_number, 5)
            elif to_base == 6:
                result = self.base_conversion(decimal_number, 6)
            elif to_base == 8:
                result = oct(decimal_number)[2:]
            elif to_base == 10:
                result = str(decimal_number)
            elif to_base == 16:
                result = hex(decimal_number)[2:].upper()

            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Invalid input")

    def base_conversion(self, number, base):
        result = ""

        while number > 0:
            remainder = number % base
            result = str(remainder) + result
            number //= base

        return result

root = tk.Tk()
converter = NumberSystemConverter(root)
root.mainloop()

