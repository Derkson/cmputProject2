
def process_email_q(cmd):
	#print("emails")
	colonIndex = cmd.find(':')

	inc1 = colonIndex
	endIndex = inc1 + 1
	while endIndex == inc1 + 1:
		inc1 = endIndex
		endIndex = endIndex + cmd[inc1:].find(' ')
		pass

	#Here endIndex =  the index of the first space after the email

	email = cmd[colonIndex + 1:endIndex].strip()
	number = ["to","from","cc","bcc"].index(cmd[:(colonIndex-1)].strip())

	return (cmd[endIndex:].stripl() , (number , email))


if __name__ == "__main__":
	print("Testing emails...")
