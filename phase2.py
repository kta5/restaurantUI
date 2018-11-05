import sqlite3

class phase2:
    conn = None 
    dbpath = "restaurant.db"
    current_user = None
    user_group = None
    def __init__(self):
        print('connecting to ' + self.dbpath + ' ...')
        self.conn = sqlite3.connect(self.dbpath)
        print('connected')
        self.help()
        self.menu()
        pass

    def create_table_customer(self):
        # Creates Table CUSTOMER
        self.conn.execute('''CREATE TABLE CUSTOMERS
                     (c_name         TEXT     NOT NULL,
                      c_custkey      DECIMAL(12,0) NOT NULL) ;''')
        print("Table CUSTOMER created")
        pass

    def create_table_order(self):
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

    def create_table_employee(self):
        # Creates Table EMPLOYEE
        self.conn.execute('''CREATE TABLE EMPLOYEE
                     (e_name        TEXT     NOT NULL,
                      e_employeekey DECIMAL(12,0) NOT NULL,
                      e_position    CHAR(20) NOT NULL,
                      e_pay         DECIMAL(8,2) NOT NULL),
                      e_username    VARCHAR(20) NOT NULL,
                      e_password    VARCHAR(20) NOT NULL;''')

        print(" Employee Table created successfully")
        pass

    def create_table_orderitem(self):
        # Creates Table ORDERITEM
        self.conn.execute('''CREATE TABLE ORDERITEM
                     (oi_name       TEXT     NOT NULL,
                      oi_orderkey   DECIMAL(12,0) NOT NULL,
                      oi_itemkey    DECIMAL(12,0) NOT NULL);''')

        print(" Orderitem Table created successfully")
        pass

    def create_table_menu(self):
        # Creates Table MENU
        self.conn.execute('''CREATE TABLE MENU
                     (m_ingredients TEXT     NOT NULL,
                      m_itemkey     DECIMAL(12,0) NOT NULL,
                      m_price       DECIMAL(8,2) NOT NULL,
                      m_name        CHAR(20) NOT NULL);''')

        print("Menu Table created successfully")
        pass

    def create_table_ingredient(self):
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

    def login(self):
        user_name = input("username: ")
        pw = input("password: ")
        login_query = self.conn.execute("SELECT e_username, e_role "
                                        "FROM EMPLOYEES "
                                        "WHERE e_username = '" + user_name + "' "
                                        "AND e_password = '" + pw + "';")
        for row in login_query:
            self.current_user = row[0]
            self.user_group = row[1]

        pass

    def password_reset(self):
        employee_table = self.conn.execute("SELECT count(*) FROM sqlite_master "
                                           "WHERE type = 'table' AND name = 'EMPLOYEES';")
        for row in employee_table:
            if row[0] == 0:
                print("No table EMPLOYEES")
                return

        user_name = input("Enter username ")

        actual_username = None
        old_pw = None
        find_user_query = self.conn.execute("SELECT e_username "
                                            "FROM EMPLOYEES "
                                            "WHERE e_username = '" + user_name + "';")
        for row in find_user_query:
            actual_username = find_user_query[0]

        find_pw_query = self.conn.execute("SELECT e_password "
                                          "FROM EMPLOYEES "
                                          "WHERE e_username = '" + actual_username + "';")
        for row in find_pw_query:
            old_pw = find_pw_query[0]

        user_input = input("Enter old password: ")
        if user_input == old_pw:
            while True:
                new_pw = input("Enter new password")
                new_pw_confirm = input("Enter new password again: ")

                if new_pw == new_pw_confirm:
                    self.conn.execute("UPDATE e_password = '" + new_pw + "' "
                                      "FROM EMPLOYEES "
                                      "WHERE e_username = '" + actual_username + "';")
                    break
                else:
                    print("Passwords do not match, try again")
                pass
            pass
        else:
            print("Incorrect password")
        pass

    def new_user(self):
        pass

    def menu(self):
        user_input = None
        while user_input != 'e':
            user_input = input()

            if user_input == '1':
                self.login()
                pass
            if user_input == '2':
                self.password_reset()
                pass
            if user_input == '3':
                self.new_user()
                pass
            if user_input == '4':
                self.create_table_customer()
                pass
            if user_input == '5':
                self.create_table_order()
                pass
            if user_input == '6':
                self.create_table_employee()
                pass
            if user_input == '7':
                self.create_table_orderitem()
                pass
            if user_input == '8':
                self.create_table_menu()
                pass
            if user_input == '9':
                self.create_table_ingredient()
                pass
            if user_input == '10':
                #self.function10()
                pass
            if user_input == '11':
                #self.function11()
                pass
            if user_input == '12':
                #self.function12()
                pass
            if user_input == '13':
                #self.function13()
                pass
            if user_input == '14':
                #self.function14()
                pass
            if user_input == '15':
                #self.function15()
                pass
            if user_input == '16':
                #self.function16()
                pass
            if user_input == '17':
                #self.function17()
                pass
            if user_input == '18':
                #self.function18()
                pass
            if user_input == '19':
                #self.function19()
                pass
            if user_input == '20':
                #self.function20()
                pass
            if user_input == 'h':
                help()
                pass
            pass
        print("disconnecting from " + self.dbpath + " ...")
        self.conn.close()
        exit()

        pass

    def help(self):
        print("'1' login as user\n"
              "'2' reset user password\n"
              "'3' make new user\n"
              "'4' create order table\n"
              "'5' create employee table\n"
              "'6' create order item table\n"
              "'7' create menu table\n"
              "'8' create ingredient table\n"
              "'9' create customer table"
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
