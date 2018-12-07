extends Node2D

var root_script = null
var orders_list = Array()
var orders_hbox = preload("res://scenes/employee_hbox.tscn")
var container = null
var status_filter

var status_filter_id = 0
var e_filter = ""

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	root_script = get_tree().get_root().get_node("dbconnection")
	container = self.get_child(0)
	refresh()
	status_filter = self.get_child(3)
	status_filter.add_item("All")
	status_filter.add_item("Manager")
	status_filter.add_item("Chef")
	status_filter.add_item("Cashier")
	pass


func refresh():
	for child in container.get_children():
		child.queue_free()
	
	orders_list = Array()
	# view all current(incomplete) order, if none please state so
	var sql = "SELECT * FROM employee"
	
	var filtered = false
	if status_filter_id == 1:
		sql += " WHERE e_position = 'Manager' "
		filtered = true
	if status_filter_id == 2:
		sql += " WHERE e_position = 'Chef' "
		filtered = true
	if status_filter_id == 3:
		sql += " WHERE e_position = 'Cashier' "
		filtered = true
		
	if e_filter != "":
		if not filtered:
			sql += " WHERE "
			filtered = true
		else:
			sql += " AND "
		sql += "e_name LIKE '" + e_filter + "%'"
	
	print (sql)
	var result = root_script.db.fetch_array(sql)
	
	if result != null:
		for i in result:
			orders_list.append(i)

	var num_things = orders_list.size()

	for i in range(0, num_things):
		var new_order = orders_hbox.instance()
		#order_key, date, custkey, status, total, employee
		var o = orders_list[i]
		print (o)
		container.add_child(new_order)
		new_order.set_vals(o["e_name"], o["e_employeekey"],o["e_position"],o["e_wage"],o["e_username"],o["e_password"])
		
		#container.add_child(new_order)
		pass
		    
	pass

func _on_Back_Button_pressed():
	get_tree().change_scene("res://scenes/menu.tscn")
	pass # replace with function body


func _on_Refresh_pressed():
	refresh()
	pass # replace with function body


func _on_Employee_LineEdit_text_changed(new_text):
	e_filter = new_text
	pass # replace with function body


func _on_Status_Options_item_selected(ID):
	status_filter_id = ID
	pass # replace with function body


func _on_Add_Employee_Button_pressed():
	get_tree().change_scene("res://scenes/add_employee.tscn")
	pass # replace with function body
