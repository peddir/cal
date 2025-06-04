import tkinter as tk
from tkinter import ttk, messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.expression = ""

        style = ttk.Style()
        style.configure('TButton', font=('Arial', 15), padding=10)

        self.display = tk.Entry(root, font=('Arial', 20), borderwidth=2, relief="ridge", justify="right")
        self.display.pack(fill="both", ipady=10, padx=10, pady=10)

        buttons_frame = tk.Frame(root)
        buttons_frame.pack(expand=True, fill="both")

        # Define buttons layout
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+'),
        ]

        for row_values in buttons:
            row = tk.Frame(buttons_frame)
            row.pack(expand=True, fill="both")
            for btn_text in row_values:
                btn = ttk.Button(row, text=btn_text, command=lambda x=btn_text: self.on_button_click(x))
                btn.pack(side="left", expand=True, fill="both")

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display.delete(0, tk.END)
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()



