from bdb_helper import *
import re

def process_email_q(cmd):
	#print("emails")
	try:
		colonIndex = cmd.find(':')
		if colonIndex == -1:
			return cmd, None
			pass

		increment = colonIndex
		endIndex = colonIndex + cmd[colonIndex:].find(' ')
		while endIndex == increment + 1:
			increment += 1
			endIndex = increment + cmd[increment:].find(' ') + 1
			#print(increment,"---",endIndex)
			pass

		#Here endIndex =  the index of the first space after the email
		#print(increment, "    " , endIndex)

		#regular case
		email = cmd[colonIndex + 1:endIndex].strip()
		if endIndex <= increment:
			#The string end after the email term
			endIndex = len(cmd)
			email = cmd[colonIndex + 1:].strip()
			pass


		number = ["to","from","cc","bcc"].index(cmd[:(colonIndex)].strip())

		emailterm = "([A-Za-z_-]*(\.[A-Za-z_-]*)+|[A-Za-z_-]*)@([A-Za-z_-]*(\.[A-Za-z_-]*)+|[A-Za-z_-]*)"
		matcher = re.search(emailterm,email)
		if not matcher or matcher.span()[0] != 0 or (matcher.span()[1] - matcher.span()[0]) != len(email):
			print("Invalid Email")
			return cmd, None
		# TODO: do we need to check validity of emails???
		return (cmd[endIndex:].strip() , (number , email))
	except Exception as e:
		# something went wrong....
		return cmd, None

def get_email_rows(eList):

	email_list = []
	db = get_database('em.idx')
	cursor = db.cursor()
	cursor.last()
	last_term = cursor.current()[0]

	for current in eList:
		target = ["to","from","cc","bcc"][current[0]]+ '-' + current[1]
		target = target.encode("utf8")

		termSet = set()
		cursor.set_range(target)
		while cursor.current()[0] == target:
			termSet.add(cursor.current()[1])
			print(cursor.current()[0])
			cursor.next()
			if cursor.current()[0] == last_term:
				break

		email_list.append(termSet)

	return set.intersection(*email_list)



if __name__ == "__main__":
	print("Testing emails...")
