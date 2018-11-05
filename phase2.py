import sqlite3

class phase2:
    self.conn = None
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
        self.conn.execute('''CREATE TABLE customer
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
        # Creates Table employee
        self.conn.execute('''CREATE TABLE employee
                     (e_name        TEXT     NOT NULL,
                      e_employeekey DECIMAL(12,0) NOT NULL,
                      e_position    CHAR(20) NOT NULL,
                      e_pay         DECIMAL(8,2) NOT NULL,
                      e_username    VARCHAR(20) NOT NULL,
                      e_password    VARCHAR(20) NOT NULL);''')

        print(" employee Table created successfully")
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
        self.current_user = None
        self.user_group = None
        user_name = input("username: ")
        pw = input("password: ")
        login_query = self.conn.execute("SELECT e_username, e_position "
                                        "FROM employee "
                                        "WHERE e_username = '" + user_name + "' "
                                        "AND e_password = '" + pw + "';")
        for row in login_query:
            self.current_user = row[0]
            self.user_group = row[1]
        if self.current_user is not None:
            print("Logged in as: " + self.current_user)
        else:
            print("Invalid credentials")
        pass

    def password_reset(self):
        employee_table = self.conn.execute("SELECT count(*) FROM sqlite_master "
                                           "WHERE type = 'table' AND name = 'employee';")
        for row in employee_table:
            if row[0] == 0:
                print("No table employee")
                return

        user_name = input("Enter username ")

        actual_username = None
        old_pw = None
        find_user_query = self.conn.execute("SELECT e_username "
                                            "FROM employee "
                                            "WHERE e_username = '" + user_name + "';")
        for row in find_user_query:
            actual_username = row[0]

        find_pw_query = self.conn.execute("SELECT e_password "
                                          "FROM employee "
                                          "WHERE e_username = '" + actual_username + "';")
        for row in find_pw_query:
            old_pw = row[0]

        user_input = input("Enter old password: ")
        if user_input == old_pw:
            while True:
                new_pw = input("Enter new password ")
                new_pw_confirm = input("Enter new password again: ")
                print("UPDATE employee SET e_password = '" + new_pw + "' WHERE e_username = '" + actual_username + "';")
                if new_pw == new_pw_confirm:
                    self.conn.execute("UPDATE employee SET e_password = '" + new_pw + "' WHERE e_username = '" + actual_username + "';")
                    self.conn.commit()
                    break
                else:
                    print("Passwords do not match, try again")
                pass
            pass
        else:
            print("Incorrect password")
        pass

    # create new user
    def new_user(self):
        new_username = input("Enter new username: ")
        name_check_query = self.conn.execute("SELECT e_username "
                                             "FROM employee "
                                             "WHERE e_username = '" + new_username + "';")
        for row in name_check_query:
            if row[0] is not None:
                print("Username taken")
                pass
            else:
                return

        pass
        real_name = input("Enter real name: ")
        position = input("Enter position")
        wage = input("Enter wage")
        e_key = 0
        ecount_query = self.conn.execute("SELECT COUNT(*) "
                                         "FROM employee;")
        for row in ecount_query:
            e_key = row[0] + 1
        self.conn.execute("INSERT into employee "
                          "VALUES ")

    def insert_data(self):
        y = input("Please enter the table you want to add to: ")

        if y == 1:  # for Customer Table
            name = input("Name: ")
            custkey = input("Customer Key : ")
            sql = '''INSERT INTO CUSTOMER (c_name, c_custkey) VALUES(%s, %s)'''
            values = (name, custkey)
            self.conn.execute(sql, values)
            self.conn.commit()

        elif y == 2:  # for Order Table
            custKey = input("Customer Key: ")
            orderKey = input("Order Key: ")
            orderPrice = input("Total Price: ")
            date = input("DATE (Format MM-DD-YYYY): ")
            status = input("Status (Type in F or O): ")
            employeeKey = input("Employee Key: ")
            sql = '''INSERT INTO ORDER (o_custkey, o_orderkey, o_total, o_date, o_status, o_employeekey VALUES(%s, %s, %s, %s, %s, %s)'''
            values = (custKey, orderKey, orderPrice, date, status, employeeKey)
            self.conn.execute(sql, values)
            self.conn.commit()

        elif y == 3:  # for Employee
            employeeName = input("Employee Name: ")
            employeeKey = input("Employee Key: ")
            position = input("Position: ")
            wage = input("Wage: ")

            sql = '''INSERT INTO EMPLOYEE (e_name, e_employeekey, e_position, e_wage) VALUES(%s, %s, %s, %s)'''
            values = (employeeName, employeeKey, position, wage)
            self.conn.execute(sql, values)
            self.conn.commit()

        elif y == 4:  # for OrderItem
            itemName = input("Item Name: ")
            orderKey = input("Order Key: ")
            itemKey = input("Item Key: ")

            sql = '''INSERT INTO EMPLOYEE (oi_name, oi_orderkey, oi_itemkey) VALUES(%s, %s, %s)'''
            values = (itemName, orderKey, itemKey)
            self.conn.execute(sql, values)
            self.conn.commit()

        elif y == 5:  # for Menu
            ingredient = input("Ingredient: ")
            itemKey = input("Item Key: ")
            foodPrice = input("Food Price: ")
            name = input("Name: ")
            sql = '''INSERT INTO MENU (m_ingredients, m_itemkey, m_price, m_name) VALUES(%s, %s, %s, %s)'''
            values = (ingredient, itemKey, foodPrice, name)
            self.conn.execute(sql, values)
            self.conn.commit()

    def incomplete_orders(self):
        # view all current(incomplete) order, if none please state so.
        sql = "SELECT o_orderkey, o_date FROM ORDER WHERE o_status = 'O' AND o_date = (SELECT CURDATE(o_date) FROM orders)"
        result = self.conn.execute(sql)
        for row in result:
            print(row[0])
            pass
        pass

    def todays_orders(self):
        # print out all orders for the current day
        sql = "SELECT o_orderkey FROM ORDER WHERE o_date = (SELECT CURDATE(o_date) FROM orders)"
        self.conn.execute(sql)
        for row in sql:
            print(row[0])
            pass
        pass

    def num_specific_customer_orders(self):
        # check how many times a certain customer ordered
        custkey = input("type in the customer key: ")
        sql = ("SELECT COUNT(o_orderkey) FROM ORDER WHERE o_custkey = " + custkey)
        result = self.conn.execute(sql)
        for row in result:
            print(row[0])
            pass
        pass

    # Print out a list of all ingredients that have 0 quantity.
    def find_zero_quantity(self):
        sql = "SELECT I_name FROM ingredients WHERE I_stock = 0"
        result = self.conn.execute(sql)
        for row in result:
            print(row[0])
            pass
        pass

    # Print out all orders handled by a certain employee
    def employee_orders(self):
        print("Please type in the employee key: ")
        employeekey = input()
        sql = ("SELECT o_orderkey " +
               "FROM orders " +
               "WHERE o_employeekey = " + employeekey)

        result = self.conn.execute(sql)
        for row in result:
            print(row[0])
            pass
        pass

    def gross_month_profit(self):
        month = input("Please enter the month(Format MM): ")
        year = input("Please enter the Year(Format YYYY): ")

        sql = ("SELECT SUM(o_total) " +
               "FROM ORDER " +
               "WHERE o_date LIKE '" + year + "-" + month + "-__'")

        result = self.conn.execute(sql)
        gross_profit = 0
        for row in result:
            gross_profit = row[0]
        print(gross_profit)
        pass

    def menu(self):
        user_input = None
        while user_input != 'e':
            user_input = input("input: ")

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
                self.gross_month_profit()
                pass
            if user_input == '18':
                self.employee_wage()
                pass
            if user_input == '19':
                self.distinct_customers()
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
              "'3' insert new user\n"
              "'4' create customer table\n"
              "'5' create order table\n"
              "'6' create employee  table\n"
              "'7' create order item table\n"
              "'8' create menu table\n"
              "'9' create ingredient table\n"
              "'10' insert new orders\n"
              "'11' insert new menu item\n"
              "'12' view all incomplete orders\n"
              "'13' view all orders on date mm-dd-yyyu\n"
              "'14' Check how many times a certain customer ordered\n"
              "'15' Print out a list of all ingredients that have 0 quantity\n"
              "'16' Print out all orders handled by a certain employee\n"
              "'17' output gross profit for a month / year\n"
              "'18' calculate expenses in employee wages\n"
              "'19' calculate number of distinct customer for a month\n"
              "'20'\n"
              "'h' to display this message"
              )
        pass


phase2()
