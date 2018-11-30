extends Node

# SQLite module
const SQLite = preload("res://lib/gdsqlite.gdns");

# Variables
var current_user = null
var entrybox_username = null
var entrybox_password = null


func _ready():
	# Create gdsqlite instance
	var db = SQLite.new()

		# Open database
	if (!db.open_db("res://restaurant.db")):
		print("Cannot open database.")
		return
	else:
		print("Connected!")
		
	
	pass

func login():
		# Get item list from db
	var result = db.fetch_array("SELECT * from employees")
	#if (not pots or pots.empty()):
	#	return;
	pass