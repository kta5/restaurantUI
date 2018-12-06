extends Button

var root_script = null

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
