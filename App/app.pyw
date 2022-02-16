import json
import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

class Main_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.iconbitmap("./App/home.ico")
        self.tk.title("Siêu ứng dụng")
        self.label_uname = Label(text = "Username")
        self.label_pass = Label(text = "Password")
        self.label_uname.grid(row=0, column=0)
        self.label_pass.grid(row=1, column=0)
        self.entry_uname = Entry()
        self.entry_uname.grid(row=0, column=1, columnspan=2)
        self.entry_pass = Entry()
        self.entry_pass.grid(row=1, column=1, columnspan=2)
        self.button1 = Button(text = "Submit")
        self.button1.grid(row=2, column=1)
        self.button2 = Button(text = "Delete")
        self.button2.grid(row=2, column=2)
        self.state = False
        self.button1.bind("<Button-1>", self.submit)
        self.button2.bind("<Button-1>", self.delete)
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def submit(self, event=None):
        uname = self.entry_uname.get()
        passw = self.entry_pass.get()
        x = 'Username:'+uname+', Password:'+passw
        with open ("./App/log", "a") as log:
            log.write(x + "\n")
        

    def delete(self, event=None):
        self.entry_uname.delete(first=0, last=1000)
        self.entry_pass.delete(first=0, last=1000)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.wm_attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.wm_attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    w = Main_Window()
    w.tk.mainloop()


