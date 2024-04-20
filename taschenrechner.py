import tkinter as tk

class Rechner:
    
    def __init__(self):
        self.val = 0

    def summe(self, a, b):
        self.val = a + b
    
    def differenz(self, a, b):
        self.val = a - b
    
class Settings:
    def __init__(self):
        self.size = 10
        self.rows = 3
        self.columns = 4
        self.text = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '=']

def main(root):
    settings = Settings()

    erg = tk.Label(root, height=settings.size, background='lightblue', text='ERGEBNIS')
    erg.pack(fill=tk.X)
    eingabe = tk.Frame(root)
    eingabe.pack()

    buttons = [tk.Button(eingabe, width=settings.size * 2, height=settings.size, text=settings.text[i], background='lightgray')
               for i in range(settings.rows * settings.columns)]

    for row in range(settings.rows):
        for column in range(settings.columns):
            i = row * settings.columns + column
            buttons[i].grid(row=row, column=column)
            print(i)

if __name__ == '__main__':
    root = tk.Tk()
    main(root)
    root.mainloop()