extends Node2D
var root_script = null
func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	get_child(0).text = "Welcome to hell, " + root_script.current_user
	pass
