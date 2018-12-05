extends Node2D

# class member variables go here, for example:
# var a = 2
# var b = "textvar"
var root_script = null
var entrybox_newpassword = ""

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	root_script = get_tree().get_root().get_node("dbconnection")
	pass

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass



func _on_New_Password_LineEdit_text_changed(new_text):
	entrybox_newpassword = new_text
	pass # replace with function body



func _on_Change_Password_Button_pressed():
	var querry = "UPDATE employee SET e_password = '"
	querry += entrybox_newpassword
	querry += "' WHERE e_username = '"
	querry += root_script.current_user
	querry += "' ;"
#
	root_script.db.query(str(querry))
	
	pass # replace with function body


func _on_Back_Button_pressed():
	get_tree().change_scene("res://scenes/menu.tscn")
	pass # replace with function body
