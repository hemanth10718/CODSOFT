from tkinter import *

class SimpleCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x200")
        self.root.configure(bg='light blue')
        
        self.first_number = StringVar()
        self.second_number = StringVar()
        self.result = StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="First Number:", font=('arial', 14), bg='light blue').grid(row=0, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.first_number, font=('arial', 14)).grid(row=0, column=1, padx=10, pady=10)
        
        Label(self.root, text="Second Number:", font=('arial', 14), bg='light blue').grid(row=1, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.second_number, font=('arial', 14)).grid(row=1, column=1, padx=10, pady=10)
        
        Button(self.root, text="Add", font=('arial', 14), command=self.add).grid(row=2, column=0, padx=10, pady=10)
        Button(self.root, text="Subtract", font=('arial', 14), command=self.subtract).grid(row=2, column=1, padx=10, pady=10)
        Button(self.root, text="Multiply", font=('arial', 14), command=self.multiply).grid(row=3, column=0, padx=10, pady=10)
        Button(self.root, text="Divide", font=('arial', 14), command=self.divide).grid(row=3, column=1, padx=10, pady=10)
        
        Label(self.root, text="Result:", font=('arial', 14), bg='light blue').grid(row=4, column=0, padx=10, pady=10)
        Entry(self.root, textvariable=self.result, font=('arial', 14), state='readonly').grid(row=4, column=1, padx=10, pady=10)

    def add(self):
        try:
            first = float(self.first_number.get())
            second = float(self.second_number.get())
            self.result.set(first + second)
        except ValueError:
            self.result.set("Invalid input")

    def subtract(self):
        try:
            first = float(self.first_number.get())
            second = float(self.second_number.get())
            self.result.set(first - second)
        except ValueError:
            self.result.set("Invalid input")

    def multiply(self):
        try:
            first = float(self.first_number.get())
            second = float(self.second_number.get())
            self.result.set(first * second)
        except ValueError:
            self.result.set("Invalid input")

    def divide(self):
        try:
            first = float(self.first_number.get())
            second = float(self.second_number.get())
            if second != 0:
                self.result.set(first / second)
            else:
                self.result.set("Cannot divide by zero")
        except ValueError:
            self.result.set("Invalid input")

root = Tk()
App = SimpleCalculator(root)
root.mainloop()
