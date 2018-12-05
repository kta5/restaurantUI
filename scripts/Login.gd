extends Node

# Variables
var entrybox_username = ""
var entrybox_password = ""
var root_script = null

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	pass

func _on_Username_LineEdit_text_changed(new_text):
	entrybox_username = new_text
	pass # replace with function body


func _on_Password_LineEdit_text_changed(new_text):
	entrybox_password = new_text
	pass # replace with function body


func _on_Login_Button_pressed():
		# Get item list from db
	var querry = "SELECT e_position from employee WHERE e_username = '"
	querry += entrybox_username
	querry += "' AND e_password = '"
	querry += entrybox_password
	querry += "' ;"
#
	var result = root_script.db.fetch_array(querry)
	if (not result or result.empty()):
		print("incorrect")
		return;
	else:
		print("Loged in as: " + entrybox_username)
		root_script.current_user = entrybox_username
		for i in result:
			root_script.user_group = i.e_position
			
		get_tree().change_scene("res://scenes/menu.tscn")
		pass
	

	pass # replace with function body
