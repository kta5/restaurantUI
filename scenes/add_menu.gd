extends Node2D

var root_script
var mname = ""
var price =""
var ingredients = ""
var mkey

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	
	pass


func _on_Add_pressed():
	if mname == "" || price == "" || ingredients == "":
		print ("no")
		return
		
	var okey_query = "SELECT COUNT(*) AS c FROM menu"
	var result = root_script.db.fetch_array(okey_query)	
	for i in result:
		mkey = i.c + 1
		
		
	var new_order_query = "INSERT INTO menu VALUES('"
	new_order_query += str(ingredients) + "' , "
	new_order_query += str(mkey) + " , "
	new_order_query += str(price) + " , '"
	new_order_query += str(mname) + "')"

	print (new_order_query)
	root_script.db.query(str(new_order_query))
	
	get_tree().change_scene("res://scenes/view_menu.tscn")
	
	pass # replace with function body


func _on_item_le_text_changed(new_text):
	mname = new_text
	pass # replace with function body


func _on_price_le_text_changed(new_text):
	price = new_text
	pass # replace with function body


func _on_ingredients_le_text_changed(new_text):
	ingredients = new_text
	pass # replace with function body
