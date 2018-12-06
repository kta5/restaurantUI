extends Node2D

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

var root_script = null
var orders_list = Array()
var currentpage = 0
var max_orders_displayed = 3
var orders_hbox = preload("res://scenes/oi_hbox.tscn")
var container = null
var today_only
var e_filter = ""
var c_filter = ""
var okey
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
	for child in container.get_children():
		child.queue_free()
	
	orders_list = Array()
	var sql = "SELECT * FROM menu"
	
	print (sql)
	var result = root_script.db.fetch_array(sql)
	
	if result != null:
		for i in result:
			orders_list.append(i)

	var num_things = orders_list.size()
	var okey_query = "SELECT COUNT(*) AS c FROM orders"
	result = root_script.db.fetch_array(okey_query)	
	for i in result:
		okey = i.c + 1
	
	for i in range(0, num_things):
		var new_order = orders_hbox.instance()
		#order_key, date, custkey, status, total, employee
		var o = orders_list[i]
		print (o)
		container.add_child(new_order)
		var oi = new_order.set_vals(o["m_name"], o["m_price"],okey , o["m_itemkey"])
		
		#container.add_child(new_order)
		pass
		    
	pass

func _on_Button_pressed():
	self.hide()
	pass # replace with function body
