extends Node2D

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

var root_script = null
var orders_list = Array()
var currentpage = 0
var max_orders_displayed = 3
var orders_hbox = preload("res://scenes/orders_hbox.tscn")
var container = null
var status_filter
var te

var status_filter_id = 0

var today_only
var e_filter = ""
var c_filter = ""
var bd_filter = ""
var ad_filter = ""

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	root_script = get_tree().get_root().get_node("dbconnection")
	container = self.get_child(0)

	status_filter = self.get_child(3)
	te = self.get_child(4)
	status_filter.add_item("All")
	status_filter.add_item("O")
	status_filter.add_item("F")
	refresh()
		
	pass

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass

func refresh():
	for child in container.get_children():
		child.queue_free()
	
	orders_list = Array()
	# view all current(incomplete) order, if none please state so
	var sql = "SELECT * FROM orders"
	
	var filtered = false
	if status_filter_id == 1:
		sql += " WHERE o_status = 'O' "
		filtered = true
	if status_filter_id == 2:
		sql += " WHERE o_status = 'F' "
		filtered = true
		
	if today_only:
		if not filtered:
			sql += " WHERE "
		else:
			sql += " AND "
		sql += "o_date = date('" + root_script.date + "')"
		
	if e_filter != "":
		if not filtered:
			sql += " WHERE "
			filtered = true
		else:
			sql += " AND "
		sql += "o_employeekey = " + e_filter
		
	if c_filter != "":
		if not filtered:
			sql += " WHERE "
			filtered = true
		else:
			sql += " AND "
		sql += "o_custkey = " + c_filter
		
	if ad_filter != "":
		if not filtered:
			sql += " WHERE "
			filtered = true
		else:
			sql += " AND "
		sql += "o_date >= '" + ad_filter + "' "
		
		
				
	if bd_filter != "":
		if not filtered:
			sql += " WHERE "
			filtered = true
		else:
			sql += " AND "
		sql += "o_date <= '" + bd_filter + "' "
		
		
	print (sql)
	var result = root_script.db.fetch_array(sql)
	
	if result != null:
		for i in result:
			orders_list.append(i)

	var num_things = orders_list.size()
	var startnum = currentpage * max_orders_displayed - 1
	var endnum = currentpage * max_orders_displayed - 1
	if endnum  > num_things - 1:
		endnum = num_things-1
	for i in range(0, num_things):
		var new_order = orders_hbox.instance()
		#order_key, date, custkey, status, total, employee
		var o = orders_list[i]
		print (o)
		container.add_child(new_order)
		new_order.set_vals(o["o_orderkey"], o["o_date"],o["o_custkey"],o["o_status"],o["o_total"],o["o_employeekey"])
		
		#container.add_child(new_order)
		pass
		    
	pass

func _on_Back_Button_pressed():
	get_tree().change_scene("res://scenes/menu.tscn")
	pass # replace with function body




func _on_Add_Order_Button_pressed():
	get_tree().change_scene("res://scenes/Add_Order_Kevin.tscn")
	pass # replace with function body


func _on_Refresh_pressed():
	refresh()
	pass # replace with function body


func _on_Status_Filter_item_selected(ID):
	status_filter_id = ID
	pass # replace with function body


func _on_Todays_Orders_toggled(button_pressed):
	today_only = button_pressed
	pass # replace with function body


func _on_Employee_LineEdit_text_changed(new_text):
	e_filter = new_text
	pass # replace with function body


func _on_Customer_LineEdit_text_changed(new_text):
	c_filter = new_text
	pass # replace with function body


func _on_after_le_text_changed(new_text):
	ad_filter = new_text
	pass # replace with function body


func _on_before_le_text_changed(new_text):
	bd_filter = new_text
	pass # replace with function body
	
func show_items(order_number):
	te.text = ""
	var sql = "SELECT * FROM orderitem WHERE oi_orderkey = "
	sql += str(order_number)
	print( sql)
	var result = root_script.db.fetch_array(sql)
	
	if result != null:
		for i in result:
			te.text += i.oi_name + " "
	

	pass
