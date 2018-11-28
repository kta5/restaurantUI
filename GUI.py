import tkinter


class GUI():

    top = tkinter.Tk()

    def __init__(self):
        # Code to add widgets will go here...
        self.top.geometry("500x500")
        # Employee Login Option
        w = tkinter.Button(self.top, text = "Employee Login", command=self.Login)
        w.place(x = 50, y = 50)
        self.top.update_idletasks()
        self.top.update()

    def Login(self):
        msg = tkinter.messagebox.showInfo("Login Prompt", "Please enter your Username and Password")









GUI()


