extends Node


# Variables
var current_user = null
var entrybox_username = null
var entrybox_password = null
var root_script = null

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	pass

func login_attempt():
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
		current_user = entrybox_username

		for i in result:
			position = i.e_position
#
		
	pass