extends Node2D

var root_script
var price = 0
var tpricele = 0
var cname = ""
var ckey = 0
var employee = ""
var employeekey = null
var time = null
var date = null
var okey = 0
var menu
var oi_list = Array()

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	menu = get_child(10)
	menu.hide()
	time = OS.get_date()
	tpricele = get_child(4)
	if time.month < 10:
		date = str(time.year) + "-0" + str(time.month)
		if time.day < 10:
			date += "-0" + str(time.day)
		else:
			date += "-" + str(time.day)
	else:
		date = str(time.year) + "-" + str(time.month)
		if time.day < 10:
			date += "-0" + str(time.day)
		else:
			date += "-" + str(time.day)
	print (date)
	
	pass

func _on_Customer_Name_LineEdit_text_changed(new_text):
	cname = new_text
	pass # replace with function body


func _on_Total_Price_LineEdit_text_changed(new_text):
	price = int(new_text)
	pass # replace with function body
	
func _on_Employee_Input_text_changed(new_text):
	employee = new_text
	pass # replace with function body

func _on_Add_Order_pressed():
	if cname == "" || employee == "":
		print("empty boxes!")
		return
	#get employee key
	var querry = "SELECT e_employeekey from employee WHERE e_name = '"
	querry += employee
	querry += "' ;"
	var result = root_script.db.fetch_array(querry)
	if (not result or result.empty()):
		print("employee not found")
		return;
	else:
		for i in result:
			employeekey = i.e_employeekey
	
	#get customer, make new if not exist
	querry = "SELECT c_custkey from customer WHERE c_name = '"
	querry += cname
	querry += "' ;"
	result = root_script.db.fetch_array(querry)
	if (not result or result.empty()):
		var c_count
		var c_countquery = "SELECT COUNT(*) AS c FROM customer"
		var c_count_res = root_script.db.fetch_array(c_countquery)
		for i in c_count_res:
			ckey = i.c + 1
		
		var new_custquery = "INSERT INTO customer VALUES ('"
		new_custquery += cname + "', "
		new_custquery += str(ckey) + ");"
		print( new_custquery)
		root_script.db.query(str(new_custquery))
	else:
		for i in result:
			ckey = i.c_custkey
		
	var okey_query = "SELECT COUNT(*) AS c FROM orders"
	result = root_script.db.fetch_array(okey_query)	
	for i in result:
		okey = i.c + 1
	
	var new_order_query = "INSERT INTO orders VALUES("
	new_order_query += str(ckey) + ", "
	new_order_query += str(okey) + ", "
	new_order_query += str(price) + ", date('"
	new_order_query += str(date) + "'), "
	new_order_query += "'O', "
	new_order_query += str(employeekey) + "); "
	
	print (new_order_query)
	root_script.db.query(str(new_order_query))
	
	get_tree().change_scene("res://scenes/view_orders.tscn")
	pass # replace with function body


func _on_Add_Item_pressed():
	menu.show()
	pass # replace with function body

func update_pricelabel():
	tpricele.text = str(price)
	pass