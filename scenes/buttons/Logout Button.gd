extends Button

# class member variables go here, for example:
# var a = 2
# var b = "textvar"
var root_script = null

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass


func _on_Logout_Button_pressed():
	root_script.current_user = null
	root_script.user_group = null
	get_tree().change_scene("res://scenes/Login.tscn")
	pass # replace with function body
