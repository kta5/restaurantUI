extends HBoxContainer

var root_script
var l0
var l1
var ikey = 0
var okey = 0
var vo = null
func _ready():
	root_script = get_tree().get_root().get_node("dbconnection")
	l0 = get_child(0)
	l1 = get_child(1)
	vo = get_parent().get_parent().get_parent()
	pass

func set_vals(n, price, o_orderkey, oi_itemkey):
	l0.text = str(n)
	l1.text = "$ " + str(price)
	okey = o_orderkey
	ikey = oi_itemkey
	pass

func _on_Button_pressed():
	var sql = "INSERT INTO orderitem VALUES ('"
	sql += l0.text + "', "
	sql += str(okey) + ", "
	sql += str(ikey) + ")"
	
	vo.oi_list.append(sql)
	vo.price += int(l1.text)
	vo.update_pricelabel()
	pass # replace with function body
