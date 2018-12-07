extends Node2D

var root_script = null
var orders_hbox = preload("res://scenes/in_hbox.tscn")
var container = null
var orders_list = Array()
var oos_only = false
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
	var sql = "SELECT * FROM ingredients"
	
	if oos_only:
		sql += " WHERE i_stock = 0"
	
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
		new_order.set_vals(o["i_name"], o["i_price"],o["i_stock"],o["i_vendorkey"])
		
		#container.add_child(new_order)
		pass
		    
	pass

func _on_Add_Menu_Item_pressed():
	get_tree().change_scene("res://scenes/add_in.tscn")
	pass # replace with function body


func _on_Refresh_pressed():
	refresh()
	pass # replace with function body


func _on_CheckButton_toggled(button_pressed):
	oos_only = button_pressed
	pass # replace with function body
