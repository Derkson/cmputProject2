import re
from datetime import *
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
		raise Exception("Invalid Query")


def get_date_range(l,u,datelist):
	# Return an upper bound and a lower bound
	for tuple in datelist:
		if tuple[0] == ':':
			if ((tuple[1] >= l) and (tuple[1] <= u)):
				l, u = tuple[1], tuple[1]
				continue
			return None, None

		if tuple[1] > u:
			if ((tuple[0] == '>') or (tuple[0] == '>=')):
				return None, None
			continue
		if tuple[1] < l:
			if ((tuple[0] == '<') or (tuple[0] == '<=')):
				return None, None
			continue

		if tuple[0] == '>=':
			l = tuple[1]
			continue
		if tuple[0] == '<=':
			u = tuple[1]
			continue

		if tuple[0] == '>':
			if tuple[1] == u:
				return None, None
			l = (datetime.strptime(tuple[1], "%Y/%m/%d") + timedelta(days=1)).strftime('%Y/%m/%d')
			continue
		if tuple[0] == '<':
			if tuple[1] == l:
				return None, None
			u = (datetime.strptime(tuple[1], "%Y/%m/%d") + timedelta(days=-1)).strftime('%Y/%m/%d')
			continue

	return l, u

def get_date_rows(datelist):

	if datelist.isEmpty():
		return set()

	# i will get you your databse lower and upperBound
	l, u = get_date_range(l,u,datelist)
	if l == None:
		return set()
	return get_date_rows_range(l, u)


def get_date_rows_range(lowerBound, upperBound):
	pass

if __name__ == "__main__":
	#pass
	#print(process_date_q("date>9999/12/22		yeet 	date:1233/33/21"))
	#print(process_date_q("date>1923/44/23   date:3455/12/56"))
	#print(process_date_q("date<4444/69/69 YYEEET BITHC TITSTE"))
	#print(process_date_q("DATE/4/213/3"))
	#print("Testing dates...")
	lowerBound = "2010/01/01"
	upperBound = "2020/01/01"
	print(get_date_range(lowerBound,upperBound,[(":","2009/04/21")]))
	print(get_date_range(lowerBound,upperBound,[(":","2017/04/21")]))
	print(get_date_range(lowerBound,upperBound,[(":","2022/04/21")]))
	print(get_date_range(lowerBound,upperBound,[(">","2009/04/21")]))
	print(get_date_range(lowerBound,upperBound,[(">","2010/01/01")]))
	print(get_date_range(lowerBound,upperBound,[(">","2013/01/01")]))
	print(get_date_range(lowerBound,upperBound,[(">","2020/01/01")]))
	print(get_date_range(lowerBound,upperBound,[(">","2020/01/02")]))
	print(get_date_range(lowerBound,upperBound,[(">=","2009/01/01")]))
	print(get_date_range(lowerBound,upperBound,[(">=","2010/01/01")]))
	print(get_date_range(lowerBound,upperBound,[(">=","2012/01/01")]))
	print(get_date_range(lowerBound,upperBound,[(">=","2020/01/01")]))
	print(get_date_range(lowerBound,upperBound,[(">=","2021/01/01")]))
	print("lalalalalallalalala")
	print(get_date_range(lowerBound,upperBound,[("<","2009/04/21")]))
	print(get_date_range(lowerBound,upperBound,[("<","2010/01/01")]))
	print(get_date_range(lowerBound,upperBound,[("<","2013/01/01")]))
	print(get_date_range(lowerBound,upperBound,[("<","2020/01/01")]))
	print(get_date_range(lowerBound,upperBound,[("<","2020/01/02")]))
	print(get_date_range(lowerBound,upperBound,[("<=","2009/01/01")]))
	print(get_date_range(lowerBound,upperBound,[("<=","2010/01/01")]))
	print(get_date_range(lowerBound,upperBound,[("<=","2012/01/01")]))
	print(get_date_range(lowerBound,upperBound,[("<=","2020/01/01")]))
	print(get_date_range(lowerBound,upperBound,[("<=","2021/01/01")]))
	print("BILBO BAGGY SHORTS")
	print(get_date_range(lowerBound,upperBound,[("<=","2016/01/01"),(">","2013/04/15")]))
	print(get_date_range(lowerBound,upperBound,[(":","2016/01/01"),(">","2016/01/01")]))
