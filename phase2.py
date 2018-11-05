import sqlite3

class phase2:
    conn = None 
    dbpath = "restauraunt.db"

    def __init__(self):
        print('connecting to ' + self.dbpath + ' ...')
        self.conn = sqlite3.connect(self.dbpath)
        print('connected')
        self.help()
        self.menu()
        pass

    def menu(self):
        user_input = None
        while user_input != 'e':
            user_input = input()

            if user_input == '1':
                self.function1()
                pass
            if user_input == '2':
                self.function2()
                pass
            if user_input == '3':
                self.function3()
                pass
            if user_input == '4':
                self.function4()
                pass
            if user_input == '5':
                self.function5()
                pass
            if user_input == '6':
                self.function6()
                pass
            if user_input == '7':
                self.function7()
                pass
            if user_input == '8':
                self.function8()
                pass
            if user_input == '9':
                self.function9()
                pass
            if user_input == '10':
                self.function10()
                pass
            if user_input == '11':
                self.function11()
                pass
            if user_input == '12':
                self.function12()
                pass
            if user_input == '13':
                self.function13()
                pass
            if user_input == '14':
                self.function14()
                pass
            if user_input == '15':
                self.function15()
                pass
            if user_input == '16':
                self.function16()
                pass
            if user_input == '17':
                self.function17()
                pass
            if user_input == '18':
                self.function18()
                pass
            if user_input == '19':
                self.function19()
                pass
            if user_input == '20':
                self.function20()
                pass
            if user_input == 'h':
                help()
                pass
            pass
        print("disconnecting from " + self.dbpath + " ...")
        self.conn.close()
        exit()

        pass

    def function1(self):
        pass


    def help(self):
        print("'1' for user login test\n"
              "'2'\n"
              "'3'\n"
              "'4'\n"
              "'5'\n"
              "'6'\n"
              "'7'\n"
              "'8'\n"
              "'9'\n"
              "'10'\n"
              "'11'\n"
              "'12'\n"
              "'13'\n"
              "'14'\n"
              "'15'\n"
              "'16'\n"
              "'17'\n"
              "'18'\n"
              "'19'\n"
              "'20'\n"
              "'h' to display this message"
              )
        pass

phase2()
