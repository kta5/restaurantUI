extends HBoxContainer

# class member variables go here, for example:
# var a = 2
# var b = "textvar"
var root_script

var original_order_key = ""
var original_date = ""
var original_custkey = ""
var original_status = ""
var original_total = ""
var original_employee = ""
var okey_le = null
var date_le = null
var cust_le = null
var status_le = null
var total_le = null
var ekey_le = null


func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	root_script = get_tree().get_root().get_node("dbconnection")
	okey_le = self.get_child(0)
	date_le = self.get_child(1)
	cust_le = self.get_child(2)
	status_le = self.get_child(3)
	total_le = self.get_child(4)
	ekey_le = self.get_child(5)
	pass

#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass

func set_vals(order_key, date, custkey, status, total, employee):
	original_order_key = order_key
	original_date = date
	original_custkey = custkey
	original_status = status
	original_total = total
	original_employee = employee
	refresh()
	pass
	
func refresh():
	okey_le.text = str(original_order_key)
	date_le.text = str(original_date)
	cust_le.text = str(original_custkey)
	status_le.text = str(original_status)
	total_le.text = str(original_total)
	ekey_le.text = str(original_employee)
	pass

func _on_orderkey_LineEdit_text_changed(new_text):
	
	pass # replace with function body


func _on_date_LineEdit_text_changed(new_text):
	pass # replace with function body


func _on_custkey_LineEdit_text_changed(new_text):
	pass # replace with function body


func _on_status_LineEdit_text_changed(new_text):
	pass # replace with function body


func _on_total_LineEdit_text_changed(new_text):
	pass # replace with function body


func _on_employeekey_LineEdit_text_changed(new_text):
	pass # replace with function body

#o_orderkey"], o["o_date"],o["o_custkey"],o["o_status"],o["o_total"],o["o_employeekey"
func _on_Button_pressed():
	var querry = "UPDATE orders SET "
	var edited = false 
	if okey_le.text != str(original_order_key):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "o_orderkey = " + okey_le.text + " "
		pass
	if date_le.text != str(original_date):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "o_date = date('" + date_le.text + "') "
		pass
	if cust_le.text != str(original_custkey):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "o_custkey = " + cust_le.text + " "
		pass
	if status_le.text != str(original_status):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "o_status = '" + status_le.text + "' "
		pass
	if total_le.text != str(original_total):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "o_total = " + total_le.text + " "
		pass
	if ekey_le.text != str(original_employee):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "o_employeekey = " + ekey_le.text + " "
		pass
	
	
	querry += "WHERE o_orderkey = " + str(original_order_key)
	querry += " ;"
	if edited:
		print( querry)
		root_script.db.query(str(querry))
	pass # replace with function body




func _on_Button2_pressed():
	var querry = "DELETE FROM orders WHERE o_orderkey = "
	querry += str(original_order_key)
	root_script.db.query(str(querry))
	pass # replace with function body
