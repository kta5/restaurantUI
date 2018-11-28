import tkinter


class GUI:

    top = tkinter.Tk()  # tkinter instance
    cuser = None    # current user

    def __init__(self):
        # Code to add widgets will go here...
        self.top.geometry("500x500")
        self.main()
        pass

    def login(self):
        msg = tkinter.messagebox.showInfo("Login Prompt", "Please enter your Username and Password")
        
        pass

    def main(self):
        while True:
            if self.cuser is not None:
                self.login()
                pass
            else:

                pass

            self.top.update_idletasks()
            self.top.update()
            pass
        pass

    pass

GUI()


