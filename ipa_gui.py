import tkinter as tk
import ipa_main

WIDTH = 1000
HEIGHT= 300
HEIGHT_WIDGET = 30

def create_app():
    root = tk.Tk()
    root.title("IPALearningAid")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.place(x=0, y=0, w=WIDTH, h=HEIGHT)
        self.create_widgets()
    

    def create_widgets(self):
        self.intro = tk.Label(self, text="Please enter an IPA Symbol:", fg="white", bg="#34A2FE")  # width = 100
        self.intro.place(x=0, y=0, height=HEIGHT_WIDGET, width=2/5 * WIDTH)
        self.intro.config(font=("Courier", 15))
        
        self.contents = tk.StringVar(value="")
        self.ipa_entry = tk.Entry(textvariable=self.contents)
        self.ipa_entry.place(x=2/5 * WIDTH, y=0, height=HEIGHT_WIDGET, width=3/5 * WIDTH)
        self.ipa_entry.config(font=("Courier", 15))
        self.ipa_entry.bind('<Key-Return>', self.print_desc)

        # self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # self.quit.pack(side="bottom")
        self.error = tk.Label(self, fg="white", bg="red") 
        self.error.place(x=0, y=HEIGHT_WIDGET, width=WIDTH, height=HEIGHT_WIDGET)
        self.error.config(font=("Courier", 15))

        self.ipa_symbols_header = tk.Label(self, text="IPA SYMBOLS", fg="white", bg="black")
        self.description_header = tk.Label(self, text="DESCRIPTION", fg="white", bg="black")
        self.nat_cat_header = tk.Label(self, text="NATURAL CLASSES/CATEGORY", fg="white", bg="black")
        self.ipa_symbols_header.config(font=("Courier", 20))
        self.description_header.config(font=("Courier", 20))
        self.nat_cat_header.config(font=("Courier", 20))
        self.ipa_symbols_header.place(x=0, y=2 * HEIGHT_WIDGET, height=HEIGHT_WIDGET, width=1/5 * WIDTH)
        self.description_header.place(x=1/5 * WIDTH, y=2 * HEIGHT_WIDGET, height=HEIGHT_WIDGET, width=1/5 * WIDTH)
        self.nat_cat_header.place(x=2/5 * WIDTH, y=2 * HEIGHT_WIDGET, height=HEIGHT_WIDGET, width=3/5 * WIDTH)
        
        HEIGHT_LEFT = HEIGHT - 3 * HEIGHT_WIDGET
        self.divider, self.divider2 = tk.Label(self, bg="black"), tk.Label(self, bg="black")
        self.divider.place(x=1/5*WIDTH, y=3 * HEIGHT_WIDGET, height=HEIGHT_LEFT, width=5)
        self.divider2.place(x=2/5*WIDTH + 5, y=3 * HEIGHT_WIDGET, height=HEIGHT_LEFT, width=5)
        
        self.ipa_symbols = tk.Label(self, text="IPA SYMBOLS", fg="white", bg="#34A2FE")
        self.description = tk.Label(self, text="DESCRIPTION", fg="white", bg="#34A2FE")
        self.nat_cat = tk.Label(self, text="NATURAL CLASSES/CATEGORY", fg="white", bg="#34A2FE")
        self.ipa_symbols.config(font=("Courier", 15))
        self.description.config(font=("Courier", 15))
        self.nat_cat.config(font=("Courier", 15))
        self.ipa_symbols.place(x=0, y=3 * HEIGHT_WIDGET, height=HEIGHT_LEFT, width=1/5 * WIDTH)
        self.description.place(x=1/5 * WIDTH + 5, y=3 * HEIGHT_WIDGET, height=HEIGHT_LEFT, width=1/5 * WIDTH)
        self.nat_cat.place(x=2/5 * WIDTH + +10, y=3 * HEIGHT_WIDGET, height=HEIGHT_LEFT, width=3/5 * WIDTH)
        

    def print_desc(self, event):
        result = ipa_main.final_output(self.contents.get())
        if not result:
            self.error["text"] = "Please enter a VALID IPA Symbol!"
            self.ipa_symbols["text"] = ""
            self.description["text"] = ""
            self.nat_cat["text"] = ""
        else:
            self.error["text"] = ""
            self.ipa_symbols["text"] = "\n".join(result[0])
            self.description["text"] = "\n".join(result[1])
            self.nat_cat["text"] = "\n".join(result[2])


create_app()