import tkinter as tk
from tkinter import messagebox


def calculate():
    operation = operation_var.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operation == "Add":
        result = num1 + num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
        result = num1 / num2
    elif operation == "Subtract":
        result = num1 - num2

    result_label.config(text=f"Result = {result}")


app = tk.Tk()
app.title("Calculator")

operation_label = tk.Label(app, text="Select Operation:")
operation_label.pack()
operation_var = tk.StringVar()
operation_var.set("Add")
operation_option_menu = tk.OptionMenu(app, operation_var, "Add", "Multiply", "Division", "Subtract")
operation_option_menu.pack()

num1_label = tk.Label(app, text="Enter 1st number:")
num1_label.pack()
entry_num1 = tk.Entry(app)
entry_num1.pack()

num2_label = tk.Label(app, text="Enter 2nd number:")
num2_label.pack()
entry_num2 = tk.Entry(app)
entry_num2.pack()

calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
