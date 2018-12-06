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

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	root_script = get_tree().get_root().get_node("dbconnection")
	container = self.get_child(0)
	refresh()
	pass

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass

func refresh():
	orders_list = Array()
	# view all current(incomplete) order, if none please state so
	var sql = "SELECT * FROM orders"
	var result = root_script.db.fetch_array(sql)
	
	for i in result:
		orders_list.append(i)
	print(orders_list)
	var num_things = orders_list.size()
	var startnum = currentpage * max_orders_displayed - 1
	var endnum = currentpage * max_orders_displayed - 1
	if endnum  > num_things - 1:
		endnum = num_things-1
	for i in range(0, num_things-1):
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
