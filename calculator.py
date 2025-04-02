import tkinter as tk
# Grundfunktionen

# Addition

# Subtraktion

# Multiplikation

# Division

# Add number to entry field

entry = None


def calculate(entry):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def button_click(button, entry):
    if button == "=":
        calculate(entry)
    elif button == "C":
        clear_entry(entry)
    else:
        entry.insert(tk.END, button)

def clear_entry(entry):
    entry.delete(0, tk.END)


def main():
    # Calculator window
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("300x400")

    # Number entry field
    entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
    entry.grid(row=0, column=0, columnspan=4)

    # Button List
    buttons = [
        "1", "2", "3", "+",
        "4", "5", "6", "-",
        "7", "8", "9", "*",
        "0", "=", "/", "C"
    ]

    # Add buttons with loop
    row = 1
    column = 0

    for button in buttons:
        btn = tk.Button(window, text=button, command=lambda b=button: button_click(b, entry), font=("Arial", 14), width=5, height=2)
        btn.grid(row=row, column=column)
        column += 1
        if column == 4:
            row += 1
            column = 0

    # Main loop
    window.mainloop()


if __name__ == "__main__":
    main()
