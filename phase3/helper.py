from bsddb3 import db

def get_database():
	database = db.DB()
	DB_File = "da.idx"
	database.open(DB_File, None, db.DB_BTREE, db.DB_CREATE) 
	return database
	

def get_rows(l, u):
	# given an upper and lower bound 
	# l and u are INCLUSIVE 
	# 	that exist withing the DB....
	# find a set of rows between the two 
	rows = set()
	if l is None and u is None:
		return rows	
	
	cur_upper, cur_lower = get_cursors()
	
	# assert l, u are byte strings...
	assert(type(l) == type("".encode("utf8")))
	assert(type(u) == type("".encode("utf8")))
		
	# set cursors to range
	cur_upper.set_range(u)
	upper_k, upper_v = cur_upper.current()
	
	cur_lower.set_range(l)
	lower_k, lower_v = cur_lower.current()

	# get all rows between l, u
	while lower_k <=  upper_k:
		#print("l: {}, {}".format(lower_k, lower_v))
		cur_lower.next()
		lower_k, lower_v = cur_lower.current()
		if lower_k <=  upper_k:
			break; 
		rows.add(lower_v)
		 	
	return rows


def write_test(l, u):
	rows = get_rows(l, u)
	with open("output.txt", 'w') as f:
		for r in rows:
			f.write(str(r)+ "\n")
	return rows

def get_cursors():
	d = get_database()
	c_u = d.cursor()
	c_l = d.cursor()
	return c_l, c_u 	

if __name__ == "__main__":
	def test(l, u, exp):
		assert(type(exp) == type(set()))
		assert(exp == get_rows(l,u))
	
	print("Running tests...")
