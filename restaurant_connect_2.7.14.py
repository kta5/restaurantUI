
import sqlite3


self.conn = sqlite3.connect('restaurant.db')
print "Opened database successfully"


#Creates Table CUSTOMER
self.conn.execute('''CREATE TABLE customer
             (c_name         TEXT     NOT NULL,
              c_custkey      DECIMAL(12,0) NOT NULL) ;''')

print " Customer Table created successfully"


#Creates Table ORDER
self.conn.execute('''CREATE TABLE ORDER
             (o_custkey     DECIMAL NOT NULL,
              o_orderkey    DECIMAL NOT NULL,
              o_total       DECIMAL(8,2) NOT NULL,
              o_date        DATE NOT NULL,
              o_status      CHAR(1) NOT NULL,
              o_employeekey DECIMAL(12,0) NOT NULL) ;''')

print " Order Table created successfully"

#Creates Table employee
self.conn.execute('''CREATE TABLE employee
             (e_name        TEXT     NOT NULL,
              e_employeekey DECIMAL(12,0) NOT NULL,
              e_position    CHAR(20) NOT NULL,
              e_pay         DECIMAL(8,2) NOT NULL);''')

print " employee Table created successfully"


#Creates Table ORDERITEM
self.conn.execute('''CREATE TABLE ORDERITEM
             (oi_name       TEXT     NOT NULL,
              oi_orderkey   DECIMAL(12,0) NOT NULL,
              oi_itemkey    DECIMAL(12,0) NOT NULL);''')

print " Orderitem Table created successfully"

#Creates Table MENU
self.conn.execute('''CREATE TABLE MENU
             (m_ingredients TEXT     NOT NULL,
              m_itemkey     DECIMAL(12,0) NOT NULL,
              m_price       DECIMAL(8,2) NOT NULL,
              m_name        CHAR(20) NOT NULL);''')

print " Menu Table created successfully"

#Creates Table INGREDIENT
self.conn.execute('''CREATE TABLE INGREDIENT
             (l_name        TEXT     NOT NULL,
              l_stock       DECIMAL NOT NULL,
              l_price       DECIMAL(8,2) NOT NULL,
              l_vendorkey   DECIMAL(12,0) NOT NULL);''')

print " Ingredient Table created successfully"


#Adds Data To Tables

y = input("Please enter the table you want to add to: ")

self.conn.execute('''INSERT INTO + 
             (w_warehousekey, w_name, w_supplierkey, w_capacity, w_address, w_nationkey) " +
				             "VALUES(?, ?, ?, ?, ?, ?)";










self.conn.close()



