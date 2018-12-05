extends Node2D

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

var root_script = null
var orders_list = Array()
var currentpage = 0

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	root_script = get_tree().get_root().get_node("dbconnection")
	refresh()
	pass

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass

func refresh():
	orders_list = Array()
	# view all current(incomplete) order, if none please state so
	var sql = "SELECT o_orderkey, o_date FROM orders WHERE o_status = 'O'"
	var result = root_script.db.fetch_array(sql)
	
	for i in result:
		orders_list.append(i)
		pass
		
	for i in range(3):
		
		pass
		    
	pass

func _on_Back_Button_pressed():
	get_tree().change_scene("res://scenes/menu.tscn")
	pass # replace with function body
