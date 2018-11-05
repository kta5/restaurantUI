import sqlite3

class phase2:
    conn = None 
    dbpath = "restaurant.db"

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
        # Creates Table CUSTOMER
        self.conn.execute('''CREATE TABLE CUSTOMERS
                     (c_name         TEXT     NOT NULL,
                      c_custkey      DECIMAL(12,0) NOT NULL) ;''')
        print("Table CUSTOMER created")
        pass

    def function2(self):
        # Creates Table ORDER
        self.conn.execute('''CREATE TABLE ORDER
                     (o_custkey     DECIMAL NOT NULL,
                      o_orderkey    DECIMAL NOT NULL,
                      o_total       DECIMAL(8,2) NOT NULL,
                      o_date        DATE NOT NULL,
                      o_status      CHAR(1) NOT NULL,
                      o_employeekey DECIMAL(12,0) NOT NULL) ;''')

        print(" Order Table created successfully")
        pass

    def function3(self):
        # Creates Table EMPLOYEE
        self.conn.execute('''CREATE TABLE EMPLOYEE
                     (e_name        TEXT     NOT NULL,
                      e_employeekey DECIMAL(12,0) NOT NULL,
                      e_position    CHAR(20) NOT NULL,
                      e_pay         DECIMAL(8,2) NOT NULL);''')

        print(" Employee Table created successfully")
        pass

    def function4(self):
        # Creates Table ORDERITEM
        self.conn.execute('''CREATE TABLE ORDERITEM
                     (oi_name       TEXT     NOT NULL,
                      oi_orderkey   DECIMAL(12,0) NOT NULL,
                      oi_itemkey    DECIMAL(12,0) NOT NULL);''')

        print(" Orderitem Table created successfully")
        pass

    def function5(self):
        # Creates Table MENU
        self.conn.execute('''CREATE TABLE MENU
                     (m_ingredients TEXT     NOT NULL,
                      m_itemkey     DECIMAL(12,0) NOT NULL,
                      m_price       DECIMAL(8,2) NOT NULL,
                      m_name        CHAR(20) NOT NULL);''')

        print("Menu Table created successfully")
        pass

    def function6(self):
        # Creates Table INGREDIENT
        self.conn.execute('''CREATE TABLE INGREDIENT
                     (l_name        TEXT     NOT NULL,
                      l_stock       DECIMAL NOT NULL,
                      l_price       DECIMAL(8,2) NOT NULL,
                      l_vendorkey   DECIMAL(12,0) NOT NULL);''')

        print("Ingredient Table created successfully")
        pass

    def function7(self):

        pass

    def function8(self):

        pass

    def function9(self):

        pass

    def function10(self):

        pass

    def help(self):
        print("'1' create table customer\n"
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
