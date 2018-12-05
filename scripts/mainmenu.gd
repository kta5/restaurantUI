extends Node


var root_script = null

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	displaybuttons()
	pass

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass

func displaybuttons():
	if root_script.user_group == "owner":
	
		pass
	elif root_script.user_group == "cashier":
	
		pass
	elif root_script.user_group == "chef":
	
		pass
	pass
	

func _on_Password_Change_Button_pressed():
	get_tree().change_scene("res://scenes/pwchange.tscn")
	pass # replace with function body


func _on_Logout_Button_pressed():
	root_script.current_user = null
	root_script.user_group = null
	get_tree().change_scene("res://scenes/Login.tscn")
	pass # replace with function body
