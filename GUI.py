import tkinter



class GUI():

    top = tkinter.Tk()
    # Code to add widgets will go here...
    top.geometry("500x500")


    # Employee Login Option
    w = Button(top, text = "Employee Login", command = Login)
    w.place(x = 50, y = 50)
    top.mainloop()


    def Login():
        msg = messagebox.showInfo("Login Prompt", "Please enter your Username and Password")








GUI()


