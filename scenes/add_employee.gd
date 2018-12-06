extends Node2D

var root_script

var options

var options_id = 0
var ename = ""
var username = ""
var password = ""
var wage = ""
var pos
var okey = ""


func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	options = self.get_child(0)
	options.add_item("Manager")
	options.add_item("Chef")
	options.add_item("Cashier")
	pass

func _on_Add_Order_pressed():
	if ename == "" || username == "" || password == "" || wage == "":
		print("empty boxes!")
		return
	
	if options_id == 0:
		pos = "Manager"
	if options_id == 1:
		pos = "Chef"
	if options_id == 2:
		pos = "Cashier"
	var okey_query = "SELECT COUNT(*) AS c FROM employee"
	var result = root_script.db.fetch_array(okey_query)	
	for i in result:
		okey = i.c + 1
	
	var new_order_query = "INSERT INTO employee VALUES('"
	new_order_query += str(ename) + "' , "
	new_order_query += str(okey) + " , '"
	new_order_query += str(pos) + "' , "
	new_order_query += str(wage) + " , '"
	new_order_query += str(username) + "' , '"
	new_order_query += str(password) + "'); "
	
	print (new_order_query)
	root_script.db.query(str(new_order_query))
	
	get_tree().change_scene("res://scenes/view_employees.tscn")
	pass # replace with function body


func _on_employee_le_text_changed(new_text):
	ename = new_text
	pass # replace with function body


func _on_Wage_le_text_changed(new_text):
	wage = new_text
	pass # replace with function body


func _on_username_le_text_changed(new_text):
	username = new_text
	pass # replace with function body


func _on_password_le_text_changed(new_text):
	password = new_text
	pass # replace with function body


func _on_Position_Option_item_selected(ID):
	options_id = ID
	pass # replace with function body
