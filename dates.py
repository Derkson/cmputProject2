import re

#takes a large string, and slices out the first valid date query,
#returns a tuple, 0th index is the remaining string, 1st index another tuple
#with 0th index being the operator and the 1st index is the date
def process_date_q(cmd):
	dateQuery = "(date)\s*(:|>|<|>=|<=)\s*\d{4}\/\d{2}\/\d{2}" #regex to find a valid date query
	matcher = re.search(dateQuery, cmd)
	operator = re.search("(:|>|<|>=|<=)", matcher.group(0))
	date = re.search("\d{4}\/\d{2}\/\d{2}", matcher.group(0))
	return cmd[len(matcher.group(0)):].strip(), (operator.group(0), date.group(0))


if __name__ == "__main__":

	#print(process_date_q("date>9999/12/22		yeet 	date:1233/33/21"))
	print("Testing dates...")
