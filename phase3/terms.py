import re
from bdb_helper import get_database
def process_term_q(cmd):
	# if there is nothing left, return nothing
	if cmd == "":
		return "", None

	regex = "((subj|body)(\s)*:)?(\s)*[0-9a-zA-Z_-]+[%]?"
	matcher = re.search(regex, cmd)
	if matcher == None or matcher.span()[0] != 0:
		raise Exception("Error: parsing term query: \'{}\'".format(cmd))
	term_q = matcher.group(0)

	prefix = ""
	if ":" in term_q:
		# ASSUMPTION: only one semi colon in term_q
		prefix, term_q = term_q.split(":")
		prefix = prefix.strip()
		term_q = term_q.strip()

	wildcard = term_q.strip()[-1] == '%'
	term = ""
	if wildcard:
		term = term_q[:-1]
	else:
		term = term_q
	obj = (prefix, term.lower(), wildcard, )

	# return everything that isnt the term query
	return cmd[matcher.span()[1]:], obj

def get_term_rows(termlist):
	#need to account for the prefix being body or subj
	#need to account for if there is a wildcard
	#finding matches or partial matches
	rows = []
	db = get_database("te.idx")
	cursor = db.cursor()
	cursor.last()
	last_term = cursor.current()[0]

	for current in termlist:
		termSet = set()
		#cursor.set_range(current[1].encode("utf8"))
		if current[0] == "body" or current[0] == "":
			cursor.set_range(b"b-" + current[1].encode("utf8"))
			if current[2] == True: #wildcard in body
				while cursor.current()[0].find(b"b-" + current[1].encode("utf8")) == 0:
					termSet.add(cursor.current()[1])
					print(cursor.current()[0])
					cursor.next()
					if cursor.current()[0] == last_term:
						break
			else:
				while cursor.current()[0] == (b"b-" + current[1].encode("utf8")):
					termSet.add(cursor.current()[1])
					print(cursor.current()[0])
					cursor.next()
					if cursor.current()[0] == last_term:
						break

		elif current[0] == "subj" or current[0] == "":
			cursor.set_range(b"s-" + current[1].encode("utf8"))
			if current[2] == True: #wildcard in subj
				while cursor.current()[0].find(b"s-" + current[1].encode("utf8")) == 0:
					termSet.add(cursor.current()[1])
					print(cursor.current()[0])
					cursor.next()
					if cursor.current()[0] == last_term:
						break
			else:
				while cursor.current()[0] == (b"s-" + current[1].encode("utf8")):
					termSet.add(cursor.current()[1])
					print(cursor.current()[0])
					cursor.next()
					if cursor.current()[0] == last_term:
						break
		rows.append(termSet)
	return set.intersection(*rows)


if __name__ == "__main__":
	def test_proc(cmd, e_rem, e_obj):
		rem, obj = process_term_q(cmd)
		assert(rem == e_rem)
		assert( obj == e_obj)

	def test_error(cmd):
		try:
			rem, obj = process_term_q(cmd)
			assert(False)
		except AssertionError as e:
			print("Assertion Failed: {}".format(cmd))
		except Exception as e:
			assert(True)

	print("running tests...")
	test_proc("body:tm_-90    ","    ",('body', 'tm_-90', False))
	test_proc("subj:tem_-123   ","   ",('subj', 'tem_-123', False) )
	test_proc("body:  m_-23  ","  ", ('body','m_-23',False))
	test_proc("subj  : term-_90 "," ",('subj','term-_90',False) )
	test_proc("termmmm-_90 "," ",("",'termmmm-_90',False) )
	test_proc("termm-_90   ","   ",("",'termm-_90',False) )
	test_proc("date : to"," : to",("",'date',False) )

	test_proc("subj  : termm-_90% "," ",('subj','termm-_90',True) )
	test_proc("body:  termm_-23%  ","  ",('body','termm_-23',True) )
	test_proc("body:termm_-90%    ","    ",('body','termm_-90',True) )
	test_proc("subj:termm_-123%   ","   ",('subj','termm_-123',True) )
	test_proc("termmmm-_90% "," ",("",'termmmm-_90',True) )
	test_proc("termm-_90%   ","   ",("",'termm-_90',True) )

	test_proc("body%   ","   ",("",'body',True) )
	test_proc("subj%   ","   ",("",'subj',True) )
	test_proc("subj %   "," %   ",("",'subj',False) )

	test_error("#m_-90#")
	test_error(" : body")
	test_error(" < body")
	test_error(": to")



	print(str(get_term_rows([\
		('subj','from',True)\
	])))
	print(str(get_term_rows([\
		('body','from',True)\
	])))
	print(str(get_term_rows([\
		('subj','from',False)\
	])))
	print(str(get_term_rows([\
		('body','from',False)\
	])))
	print(str(get_term_rows([\
		('','from',True)\
	])))
	print(str(get_term_rows([\
		('','from',False)\
	])))

	## TODO: test more terms!!!!
