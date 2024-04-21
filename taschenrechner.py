import tkinter as tk

class Settings:
    def __init__(self):
        self.size = 10
        self.text = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.operators = ['+', '-', '=']
        self.font = 'Bookman 10'

class Main(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.settings = Settings()
    
        self.erg_zeile = tk.Label(master, height=self.settings.size, background='lightblue', text='0', font=self.settings.font)
        self.erg_zeile.pack(fill=tk.X)
        self.eingabe = tk.Frame(master)
        self.eingabe.pack()
        self.newnumber = True
        self.add = False
        self.diff = False
        self.init_buttons()
        self.init_operators()

    def init_buttons(self):
        self.buttons = [tk.Button(self.eingabe, width=self.settings.size * 2, height=self.settings.size, text=self.settings.text[i],
                            command=lambda n=self.settings.text[i]: self.put_number(n), background='lightgray', font=self.settings.font)
                for i in range(9)]

        for row in range(3):
            for column in range(3):
                i = row * 3 + column
                self.buttons[i].grid(row=row, column=column)

    def init_operators(self):
        funs = [self.plus, self.minus, self.ergebnis]
        for i, op in enumerate(self.settings.operators):
            but = tk.Button(self.eingabe, width=self.settings.size * 2, height=self.settings.size, text=op,
                            background='lightgray', command=funs[i], font=self.settings.font)
            but.grid(row=i, column=3)

    def plus(self):
        self.newnumber = True
        self.add = True
        self.zwischenerg = self.erg_zeile['text']

    def minus(self):
        self.newnumber = True
        self.diff = True
        self.zwischenerg = self.erg_zeile['text']

    def ergebnis(self):
        if self.add:
            self.erg_zeile['text'] = str(int(self.erg_zeile['text']) + int(self.zwischenerg))
            self.add = False
        elif self.diff:
            self.erg_zeile['text'] = str(int(self.zwischenerg) - int(self.erg_zeile['text']))
            self.add = False

    def put_number(self, n):
        if self.newnumber:
            self.erg_zeile['text'] = n
            self.newnumber = False
        else:
            self.erg_zeile['text'] += n

if __name__ == '__main__':
    root = tk.Tk()
    main = Main(root)
    root.mainloop()