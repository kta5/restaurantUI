extends HBoxContainer

var root_script
var field0
var field1
var field2
var field3
var o0
var o1
var o2
var o3

func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	field0 = self.get_child(0)
	field1 = self.get_child(1)
	field2 = self.get_child(2)
	field3 = self.get_child(3)
	pass
#name, price, stock, vendor
func set_vals(a, b, c, d):
	o0 = str(a)
	o1 = str(b)
	o2 = str(c)
	o3 = str(d)
	
	field0.text = str(a)
	field1.text = str(b)
	field2.text = str(c)
	field3.text = str(d)
	pass
	
func _on_Button_pressed():
	var querry = "UPDATE ingredients SET "
	var edited = false 
	if field0.text != str(o0):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "i_name = '" + field0.text + "' "
		pass
	if field1.text != str(o1):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "i_price = " + field1.text + " "
		pass
	if field2.text != str(o2):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "i_stock = " + field2.text + " "
		pass
	if field3.text != str(o3):
		if not edited:
			edited = true
		else:
			querry += ", "
		querry += "i_vendorkey = '" + field3.text + "' "
		pass
	
	
	querry += "WHERE i_name = '" + str(o0)
	querry += "' ;"
	if edited:
		print( querry)
		root_script.db.query(str(querry))
	pass # replace with function body

func _on_Button2_pressed():
	var querry = "DELETE FROM ingredients WHERE i_name = '"
	querry += str(o0)
	querry += "'"
	root_script.db.query(str(querry))
	pass # replace with function body
