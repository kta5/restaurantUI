extends Node


# SQLite module
const SQLite = preload("res://lib/gdsqlite.gdns")

var db = null
var current_user = null
var user_group = null
var time
var date = ""

func _ready():
	# Create gdsqlite instance
	db = SQLite.new()
	
	# Open database
	if(!db.open_db("res://restaurant.db")):
		print("Cannot open database.")
		return
	else:
		print("Connected!")
	
	time = OS.get_date()
	if time.month < 10:
		date = str(time.year) + "-0" + str(time.month)
		if time.day < 10:
			date += "-0" + str(time.day)
		else:
			date += "-" + str(time.day)
	else:
		date = str(time.year) + "-" + str(time.month)
		if time.day < 10:
			date += "-0" + str(time.day)
		else:
			date += "-" + str(time.day)
	print (date)
	
	pass
	

func _exit_tree():
	if (db and db.loaded()):
		# Close database
		db.close();
		
func go_to_menu():
	if user_group == "Manager":
		get_tree().change_scene("res://scenes/manager_menu.tscn")
	else:
		get_tree().change_scene("res://scenes/employee_menu.tscn")
	pass
