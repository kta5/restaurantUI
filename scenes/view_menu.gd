extends Node2D

var root_script = null
var orders_hbox = preload("res://scenes/menu_hbox.tscn")
var container = null
var orders_list = Array()

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	root_script = get_tree().get_root().get_node("dbconnection")
	container = self.get_child(0)
	refresh()
	pass


func refresh():
	for child in container.get_children():
		child.queue_free()
	
	# view all current(incomplete) order, if none please state so
	var sql = "SELECT * FROM menu"
		
	orders_list = Array()
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
		new_order.set_vals(o["m_name"], o["m_itemkey"],o["m_price"],o["m_ingredients"])
		
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

	pass # replace with function body


func _on_Status_Options_item_selected(ID):

	pass # replace with function body


func _on_Add_Menu_Item_pressed():
	get_tree().change_scene("res://scenes/add_menu.tscn")
	pass # replace with function body
