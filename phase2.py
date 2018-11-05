import sqlite3

class phase2:
    conn = None 

    def __init__(self):
        print ('connecting')
        conn = sqlite3.connect('restaurant.db')
        self.help()
        self.menu()
        pass

    def menu(self):

        in = input()
    
    def help():
        pass

phase2()
