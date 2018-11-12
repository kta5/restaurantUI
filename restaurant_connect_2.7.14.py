
import sqlite3


conn = sqlite3.connect('restaurant.db')
print "Opened database successfully"


#Creates Table CUSTOMER
conn.execute('''CREATE TABLE CUSTOMER
             (c_name         TEXT     NOT NULL,
              c_custkey      DECIMAL(12,0) NOT NULL) ;''')

print " Customer Table created successfully"


#Creates Table ORDER
conn.execute('''CREATE TABLE ORDER
             (o_custkey     DECIMAL NOT NULL,
              o_orderkey    DECIMAL NOT NULL,
              o_total       DECIMAL(8,2) NOT NULL,
              o_date        DATE NOT NULL,
              o_status      CHAR(1) NOT NULL,
              o_employeekey DECIMAL(12,0) NOT NULL) ;''')

print " Order Table created successfully"

#Creates Table EMPLOYEE
conn.execute('''CREATE TABLE EMPLOYEE
             (e_name        TEXT     NOT NULL,
              e_employeekey DECIMAL(12,0) NOT NULL,
              e_position    CHAR(20) NOT NULL,
              e_wage         DECIMAL(8,2) NOT NULL);''')

print " Employee Table created successfully"


#Creates Table ORDERITEM
conn.execute('''CREATE TABLE ORDERITEM
             (oi_name       TEXT     NOT NULL,
              oi_orderkey   DECIMAL(12,0) NOT NULL,
              oi_itemkey    DECIMAL(12,0) NOT NULL);''')

print " Orderitem Table created successfully"

#Creates Table MENU
conn.execute('''CREATE TABLE MENU
             (m_ingredients TEXT     NOT NULL,
              m_itemkey     DECIMAL(12,0) NOT NULL,
              m_price       DECIMAL(8,2) NOT NULL,
              m_name        CHAR(20) NOT NULL);''')

print " Menu Table created successfully"

#Creates Table INGREDIENT
conn.execute('''CREATE TABLE INGREDIENT
             (l_name        TEXT     NOT NULL,
              l_stock       DECIMAL NOT NULL,
              l_price       DECIMAL(8,2) NOT NULL,
              l_vendorkey   DECIMAL(12,0) NOT NULL);''')

print " Ingredient Table created successfully"

#Creates Table INGREDIENT
conn.execute('''CREATE TABLE INGREDIENT
             (l_name        TEXT     NOT NULL,
              l_stock       DECIMAL NOT NULL,
              l_price       DECIMAL(8,2) NOT NULL,
              l_vendorkey   DECIMAL(12,0) NOT NULL);''')

print " Ingredient Table created successfully"

#Adds Data To Tables
print "1 - CUSTOMER\n"
print "2 - ORDERS\n"
print "3 - EMPLOYEE\n"
print "4 - ORDERITEM\n"
print "5 - MENU\n"
print "6 - INGREDIENTS\n"


y = raw_input("Please enter the table you want to add to: ")

if y == 1: #for Customer Table

    print("Name: ");
    name = raw_input();
    print("\n");

    print("Customer Key : ");
    custkey = raw_input();
    print("\n");

    sql = ('''INSERT INTO CUSTOMER
                     (c_name, c_custkey) VALUES(%s, %s)''')
    values = (name, custKey)
    
    conn.execute(sql, values)

    conn.commit()


elif y == 2: #for Order Table
    print("Customer Key: ");
    custKey = raw_input();
    print("\n");

    print("Order Key: ");
    orderKey = raw_input();
    print("\n");

    print("Total Price: ");
    orderPrice = raw_input();
    print("\n");

    print("DATE (Format MM-DD-YYYY): ");
    date = raw_input();
    print("\n");

    print("Status (Type in F or O): ");
    status = raw_input();
    print("\n");

    print("Employee Key: ");
    employeeKey = raw_input();
    print("\n");


    sql = ('''INSERT INTO ORDER 
                     (o_custkey, o_orderkey, o_total, o_date, o_status, o_employeekey VALUES(%s, %s, %s, %s, %s, %s)''')
    values = (custKey, orderKey, orderPrice, date, status, employeeKey)
    
    conn.execute(sql, values)

    conn.commit()

    
elif y == 3: #for Employee
    
    print("Employee Name: ");
    employeeName = raw_input();
    print("\n");

    print("Employee Key: ");
    employeeKey = raw_input();
    print("\n");

    print("Position: ");
    position = raw_input();
    print("\n");

    print("Wage: ");
    wage = raw_input();
    print("\n");

    
    sql = ('''INSERT INTO EMPLOYEE 
                     (e_name, e_employeekey, e_position, e_wage) VALUES(%s, %s, %s, %s)''')
    values = (employeeName, employeeKey, position, wage)
    
    conn.execute(sql, values)

    conn.commit()


elif y == 4: #for OrderItem
    print("Item Name: ");
    itemName = raw_input();
    print("\n");

    print("Order Key: ");
    orderKey = raw_input();
    print("\n");

    print("Item Key: ");
    itemKey = raw_input();
    print("\n");

    
    sql = ('''INSERT INTO EMPLOYEE 
                     (oi_name, oi_orderkey, oi_itemkey) VALUES(%s, %s, %s)''')
    values = (itemName, orderKey, itemKey)
    
    conn.execute(sql, values)

    conn.commit()


elif y == 5: # for Menu
    print("Ingredient: ");
    ingredient = raw_input();
    print("\n");

    print("Item Key: ");
    itemKey = raw_input();
    print("\n");

    print("Food Price: ");
    foodPrice = raw_input();
    print("\n");

    print("Name: ");
    name = raw_input();
    print("\n");

    
    sql = ('''INSERT INTO MENU 
                     (m_ingredients, m_itemkey, m_price, m_name) VALUES(%s, %s, %s, %s)''')
    values = (ingredient, itemKey, foodPrice, name)
    
    conn.execute(sql, values)

    conn.commit()
    


#print out all orders for the current day

    sql = ("SELECT o_orderkey FROM ORDER WHERE o_date = (SELECT CURDATE(o_date) FROM orders)")

    conn.execute(sql)

    for row in sql:
        print "o_orderkey"
           


#check how many times a certain customer ordered

    print("Please type in the customer key: ");
    custkey = raw_input();
    print("\n");
    
    sql = ("SELECT COUNT(o_orderkey) FROM ORDER WHERE o_custkey = " + custkey)

    result = conn.execute(sql)

    print result


#view all current(incomplete) order, if none please state so.

    sql = ("SELECT o_orderkey, o_date FROM ORDER WHERE o_status = 'O' AND o_date = (SELECT CURDATE(o_date) FROM orders)")
    
    result = conn.execute(sql)

    print result


# Print out a list of all ingredients that have 0 quantity.

    sql = ("SELECT I_name FROM ingredients WHERE I_stock = 0")

    result = conn.execute(sql)
    print result


# Print out all orders handled by a certain employee
    print("Please type in the employee key: ");
    employeekey = raw_input();
    print("\n");


    sql = ("SELECT o_orderkey " +
           "FROM orders " +
           "WHERE o_employeekey = " + employeekey)

    result = conn.execute(sql)
    print result



# Make a new order
    print("Please type in the employee key: ");
    employeekey = raw_input();
    print("\n");
    
    print("Please type in the employee key: ");
    employeekey = raw_input();
    print("\n");

    print("Please type in the employee key: ");
    employeekey = raw_input();
    print("\n");

    
# Output the Gross Profit for a certain month and year

    print("Please enter the month(Format MM): ")
    month = raw_input()
    print("\n");
    
    print("Please enter the Year(Format YYYY): ")
    year = raw_input()
    print("\n");


    sql = ("SELECT SUM(o_total) " +
           "FROM ORDER " +
           "WHERE o_date LIKE '"+ year + "-" + month + "-__'")

    result = conn.execute(sql)
    print result

# Calculate how much money needs to be paid to the employees every month(based on 8 hour days)

    sql = ("SELECT COUNT( " +
           "FROM 
# Calculate the amount of distinct customers that come to the restaurant on a certain month and year

    print("Please enter the month(Format MM): ")
    month = raw_input()
    print("\n");
    
    print("Please enter the Year(Format YYYY): ")
    year = raw_input()
    print("\n");

    sql = ("SELECT COUNT(DISTINCT o_custkey) " +
           "FROM ORDER " +
           "WHERE o_date LIKE '"+ year + "-" + month + "-__'")

    result = conn.execute(sql)
    print result          
conn.close()



