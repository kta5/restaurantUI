import tkinter



class GUI():

    def __init__(self):
        top = tkinter.Tk()
        # Code to add widgets will go here...
        top.geometry("500x500")
        # Employee Login Option
        w = tkinter.Button(top, text = "Employee Login", command=self.Login)
        w.place(x = 50, y = 50)
        top.mainloop()

    def Login(self):
        msg = tkinter.messagebox.showInfo("Login Prompt", "Please enter your Username and Password")









GUI()


