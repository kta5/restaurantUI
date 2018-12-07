extends Node2D

var root_script
var iname = ""
var istock = ""
var iprice = ""
var ivendorkey = 4

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	pass


func _on_Add_pressed():
	if iname == "" || istock == "" || iprice == "":
		print ("no")
		return
		
	var new_order_query = "INSERT INTO ingredients VALUES('"
	new_order_query += str(iname) + "' , "
	new_order_query += str(istock) + " , "
	new_order_query += str(iprice) + " , "
	new_order_query += str(ivendorkey) + ")"

	print (new_order_query)
	root_script.db.query(str(new_order_query))
	
	get_tree().change_scene("res://scenes/view_in.tscn")
	
	pass # replace with function body


func _on_item_le_text_changed(new_text):
	iname = new_text
	pass # replace with function body


func _on_price_le_text_changed(new_text):
	iprice = new_text
	pass # replace with function body


func _on_ingredients_le_text_changed(new_text):
	istock = new_text
	pass # replace with function body
