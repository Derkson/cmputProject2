
def process_email_q(cmd):
	#print("emails")
	try:
		colonIndex = cmd.find(':')

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

		# TODO: do we need to check validity of emails???
		return (cmd[endIndex:].strip() , (number , email))
	except Exception as e:
		# something went wrong....
		return cmd, None

def get_email_rows(eList):
	pass


if __name__ == "__main__":
	print("Testing emails...")
