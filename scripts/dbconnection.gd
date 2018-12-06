extends Node


# SQLite module
const SQLite = preload("res://lib/gdsqlite.gdns")

var db = null
var current_user = null
var user_group = null

func _ready():
	# Create gdsqlite instance
	db = SQLite.new()
	
	# Open database
	if(!db.open_db("res://restaurant.db")):
		print("Cannot open database.")
		return
	else:
		print("Connected!")
	
	pass
	

func _exit_tree():
	if (db and db.loaded()):
		# Close database
		db.close();
		
func go_to_menu():
	if user_group == "Manager":
		get_tree().change_scene("res://scenes/manager_menu.tscn")
	if user_group == "Manager":
		get_tree().change_scene("res://scenes/employee_menu.tscn")
	pass
