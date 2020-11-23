import tkinter as tk
import ipa_main


def create_app():
    root = tk.Tk()
    root.title("IPALearningAid")
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    

    def create_widgets(self):
        self.intro = tk.Label(self, text="Please enter an IPA Symbol:", fg="white", bg="#34A2FE", width="100")
        self.intro.pack(side="top")
        
        self.contents = tk.StringVar(value="<IPA Symbol>")
        # self.contents.set("this is a variable")
        self.ipa_entry = tk.Entry(textvariable=self.contents)
        self.ipa_entry.pack(side="top")
        self.ipa_entry.bind('<Key-Return>', self.print_desc)

        # self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # self.quit.pack(side="bottom")
        self.result = tk.Label(self, fg="white", bg="violet", width="100")
        self.result.pack(side="bottom")

    def print_desc(self, event):
        result = ipa_main.final_output(self.contents.get())
        self.result["text"] = result


create_app()