import re

#takes a large string, and slices out the first valid date query,
#returns a tuple, 0th index is the remaining string, 1st index another tuple
#with 0th index being the operator and the 1st index is the date
def process_date_q(cmd):
	dateQuery = "(date)\s*(:|>|<|>=|<=)\s*\d{4}\/\d{2}\/\d{2}" #regex to find a valid date query
	matcher = re.search(dateQuery, cmd)
	if matcher and matcher.span()[0] == 0:
		operator = re.search("(:|>|<|>=|<=)", matcher.group(0))
		date = re.search("\d{4}\/\d{2}\/\d{2}", matcher.group(0))
		return cmd[len(matcher.group(0)):].strip(), (operator.group(0), date.group(0))
	else:
		#raise Exception("Invalid Query")
		return cmd, None


if __name__ == "__main__":
	#pass
	print(process_date_q("date>9999/12/22		yeet 	date:1233/33/21"))
	print(process_date_q("date>1923/44/23   date:3455/12/56"))
	print(process_date_q("date<4444/69/69 YYEEET BITHC TITSTE"))
	print(process_date_q("DATE/4/213/3"))
	#print("Testing dates...")
