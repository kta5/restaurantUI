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
