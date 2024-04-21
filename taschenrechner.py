import tkinter as tk

class Settings:
    def __init__(self):
        self.size = 10
        self.rows = 3
        self.columns = 4
        self.text = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '=']

def main(root):
    settings = Settings()

    erg_zeile = tk.Label(root, height=settings.size, background='lightblue', text='0')
    erg_zeile.pack(fill=tk.X)
    eingabe = tk.Frame(root)
    eingabe.pack()

    buttons = [tk.Button(eingabe, width=settings.size * 2, height=settings.size, text=settings.text[i], background='lightgray')
               for i in range(settings.rows * settings.columns)]

    for b in buttons:
        b['command'] = lambda b=b : fun(b)

    for row in range(settings.rows):
        for column in range(settings.columns):
            i = row * settings.columns + column
            buttons[i].grid(row=row, column=column)

    plus = False
    minus = False
    lösung = False
    buffer = 0

    def fun(button):
        x = button['text']
        if x == '+':
            plus = True
            buffer = erg_zeile['text']
        elif x == '-':
            minus = True
            buffer = erg_zeile['text']
        elif x == '=':
            pass     
        else:
            display_number(button['text'])

    def display_number(n):
        erg_zeile['text'] = n

if __name__ == '__main__':
    root = tk.Tk()
    main(root)
    root.mainloop()