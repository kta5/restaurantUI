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
        # Creates Table customer
        try:
            self.conn.execute('''CREATE TABLE customer
                         (c_name         TEXT     NOT NULL,
                          c_custkey      DECIMAL(12,0) NOT NULL) ;''')
            print("Table customer created")
        except sqlite3.OperationalError:
            print("Table already exists")
        pass

    def create_table_order(self):
        # Creates Table orders
        try:
            self.conn.execute('''CREATE TABLE orders 
                         (o_custkey     DECIMAL NOT NULL, 
                          o_orderkey    DECIMAL NOT NULL, 
                          o_total       DECIMAL(8,2) NOT NULL, 
                          o_date        DATE NOT NULL, 
                          o_status      CHAR(1) NOT NULL, 
                          o_employeekey DECIMAL(12,0) NOT NULL);''')

            print("orders Table created successfully")
        except sqlite3.OperationalError:
            print("table already exists")
        pass

    def create_table_employee(self):
        # Creates Table employee
        try:
            self.conn.execute('''CREATE TABLE employee
                         (e_name        TEXT     NOT NULL,
                          e_employeekey DECIMAL(12,0) NOT NULL,
                          e_position    CHAR(20) NOT NULL,
                          e_wage         DECIMAL(8,2) NOT NULL,
                          e_username    VARCHAR(20) NOT NULL,
                          e_password    VARCHAR(20) NOT NULL);''')

            print(" employee Table created successfully")
        except sqlite3.OperationalError:
            print("table already exists")
        pass

    def create_table_orderitem(self):
        # Creates Table ORDERITEM
        try:
            self.conn.execute('''CREATE TABLE orderitem
                         (oi_name       TEXT     NOT NULL,
                          oi_orderkey   DECIMAL(12,0) NOT NULL,
                          oi_itemkey    DECIMAL(12,0) NOT NULL);''')

            print(" Orderitem Table created successfully")
        except sqlite3.OperationalError:
            print("table already exists")
        pass

    def create_table_menu(self):
        # Creates Table menu
        try:
            self.conn.execute('''CREATE TABLE menu
                         (m_ingredients TEXT     NOT NULL,
                          m_itemkey     DECIMAL(12,0) NOT NULL,
                          m_price       DECIMAL(8,2) NOT NULL,
                          m_name        CHAR(20) NOT NULL);''')

            print("Menu Table created successfully")
        except sqlite3.OperationalError:
            print("table already exists")
        pass

    def create_table_ingredient(self):
        # Creates Table ingredients
        try:
            self.conn.execute('''CREATE TABLE ingredients
                         (l_name        TEXT     NOT NULL,
                          l_stock       DECIMAL NOT NULL,
                          l_price       DECIMAL(8,2) NOT NULL,
                          l_vendorkey   DECIMAL(12,0) NOT NULL);''')

            print("Ingredient Table created successfully")
        except sqlite3.OperationalError:
            print("table already exists")
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
        employee_table = self.conn.execute("19 count(*) FROM sqlite_master "
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

                if new_pw == new_pw_confirm:
                    self.conn.execute("UPDATE employee SET e_password = '" + new_pw + "' WHERE e_username = '" + actual_username + "';")
                    self.conn.commit()
                    print("password changed")
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
                return

        new_pw = input("Enter password: ")
        pass
        real_name = input("Enter real name: ")
        position = input("Enter position: ")
        wage = input("Enter wage: ")
        e_key = 0
        ecount_query = self.conn.execute("SELECT COUNT(*) "
                                         "FROM employee;")
        for row in ecount_query:
            e_key = row[0] + 1

        self.conn.execute('''INSERT into employee 
                          VALUES (?,?,?,?,?,?)''',
                          (real_name,e_key,position,wage,new_username,new_pw))
        self.conn.commit()

    def insert_data(self):
        y = input('''Please enter the table you want to add to: 
'1' for customer
'2' for orders
'3' for orderitem
'4' for menu
''')

        if y == '1':  # for Customer Table
            name = input("Name: ")
            custkey = input("Customer Key : ")
            sql = '''INSERT INTO customer (c_name, c_custkey) VALUES (,)'''
            values = (name, custkey)
            self.conn.execute(sql, values)
            self.conn.commit()

        elif y == '2':  # for Order Table
            custKey = input("Customer Key: ")
            orderKey = input("Order Key: ")
            orderPrice = input("Total Price: ")
            date = input("DATE (Format MM-DD-YYYY): ")
            status = input("Status (Type in F or O): ")
            employeeKey = input("Employee Key: ")
            sql = '''INSERT INTO orders (o_custkey, o_orderkey, o_total, o_date, o_status, o_employeekey VALUES(%s, %s, %s, %s, %s, %s)'''
            values = (custKey, orderKey, orderPrice, date, status, employeeKey)
            self.conn.execute(sql, values)
            self.conn.commit()

        elif y == '3':  # for OrderItem
            itemName = input("Item Name: ")
            orderKey = input("Order Key: ")
            itemKey = input("Item Key: ")

            sql = '''INSERT INTO orderitem (oi_name, oi_orderkey, oi_itemkey) VALUES(%s, %s, %s)'''
            values = (itemName, orderKey, itemKey)
            self.conn.execute(sql, values)
            self.conn.commit()

        elif y == '4':  # for Menu
            ingredients = input("Ingredient: ")
            itemKey = input("Item Key: ")
            foodPrice = input("Food Price: ")
            name = input("Name: ")
            sql = '''INSERT INTO menu (m_ingredients, m_itemkey, m_price, m_name) VALUES(%s, %s, %s, %s)'''
            values = (ingredients, itemKey, foodPrice, name)
            self.conn.execute(sql, values)
            self.conn.commit()
            pass

        pass

    def incomplete_orders(self):
        # view all current(incomplete) order, if none please state so.
        sql = "SELECT o_orderkey, o_date FROM orders WHERE o_status = 'O'"
        result = self.conn.execute(sql)
        print("incomplete orders: ")
        for row in result:
            print("order# " + str(row[0]))
            pass
        pass

    def todays_orders(self):
        # print out all orders for the current day
        day = input("enter day(DD): ")
        month = input("enter month(MM): ")
        year = input("enter year(YYYY): ")
        sql = "SELECT o_orderkey FROM orders  " \
              "WHERE strftime('%d', o_date)  = '" + day + "' AND  strftime('%Y', o_date)  = '" + year + "' AND strftime('%m',o_date) = '" + month + "';"
        self.conn.execute(sql)
        for row in sql:
            print(row)
            pass
        pass

    def num_specific_customer_orders(self):
        # check how many times a certain customer ordered
        custkey = input("type in the customer key: ")
        sql = ("SELECT COUNT(o_orderkey) FROM orders WHERE o_custkey = " + custkey)
        result = self.conn.execute(sql)
        for row in result:
            print(row[0])
            pass
        pass

    # Print out a list of all ingredients that have 0 quantity.
    def find_zero_quantity(self):
        sql = "SELECT l_name FROM ingredients WHERE I_stock = 0"
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
        month = input("enter month(MM): ")
        year = input("enter year(YYYY): ")

        sql = ("SELECT SUM(o_total) " +
               "FROM orders " +
               "WHERE strftime('%Y', o_date)  = '" + year + "' AND strftime('%m',o_date) = '" + month + "';")

        result = self.conn.execute(sql)
        gross_profit = 0
        for row in result:
            gross_profit = row[0]
        print(gross_profit)
        pass
    def employee_wage(self):
        cost = 0
        sql = ("SELECT SUM(e_wage) " +
               "FROM employee")
        result = self.conn.execute(sql)

        for row in result:
            cost += row[0]
        print(cost)
        pass
        pass

    def distinct_customers(self):
        month = input("enter month(MM): ")
        year = input("enter Year(YYYY): ")
    
        sql = ("SELECT COUNT(DISTINCT o_custkey) " +
               "FROM orders " +
               "WHERE strftime('%Y', o_date)  = '" + year + "' AND strftime('%m',o_date) = '" + month + "';")
        custnum = 0
        result = self.conn.execute(sql)
        for row in result:
            custnum = row[0]
        print("unique customers: " + str(custnum))
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
                self.create_table_submenu()
                pass
            if user_input == '5':
                self.insert_data()
                pass
            if user_input == '6':

                pass
            if user_input == '7':

                pass
            if user_input == '8':

                pass
            if user_input == '9':

                pass
            if user_input == '10':

                pass
            if user_input == '11':

                pass
            if user_input == '12':
                self.incomplete_orders()
                pass
            if user_input == '13':
                self.todays_orders()
                pass
            if user_input == '14':
                self.num_specific_customer_orders()
                pass
            if user_input == '15':
                self.find_zero_quantity()
                pass
            if user_input == '16':
                self.employee_orders()
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

    def create_table_submenu(self):
        user_input = input("Enter customer, order, employee, orderitem, menu, ingredient")
        if user_input == 'customer':
            self.create_table_customer()
            pass
        if user_input == 'order':
            self.create_table_order()
            pass
        if user_input == 'employee':
            self.create_table_employee()
            pass
        if user_input == 'orderitem':
            self.create_table_orderitem()
            pass
        if user_input == 'menu':
            self.create_table_menu()
            pass
        if user_input == 'ingredient':
            self.create_table_ingredient()
            pass
        pass

    def help(self):
        print("'1' login as user\n"
              "'2' reset user password\n"
              "'3' insert new user\n"
              "'4' create tables\n"
              "'5' insert new data\n"
              "'6' \n"
              "'7' \n"
              "'8' \n"
              "'9' \n"
              "'10' \n"
              "'11' \n"
              "'12' view all incomplete orders\n"
              "'13' view all orders of a date\n"
              "'14' Check how many times a certain customer ordered\n"
              "'15' Print ingredients of 0 quantity\n"
              "'16' Print orders handled by certain employee\n"
              "'17' output gross profit for month / year\n"
              "'18' calculate expenses in employee wages\n"
              "'19' calculate number of distinct customer for a month\n"
              "'20' \n"
              "'e' to exit\n"
              "'h' to display this message"
              )
        pass


phase2()
