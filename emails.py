
def process_email_q(cmd):
	#print("emails")
	colonIndex = cmd.find(':')

	inc1 = colonIndex
	endIndex = inc1 + 1
	while endIndex = inc1 + 1:
		inc1 = endIndex
		endIndex = endIndex + cmd[inc1:].find(' ');
		pass

	#Here endIndex =  the index of the first space after the email

	email = cmd[colonIndex + 1:endIndex].strip()
	number = 0

	if cmd.starts_with(string, "from"):
		number = 1
		pass
	elif cmd.starts_with(string, "cc"):
		number = 2
		pass
	elif cmd.starts_with(string, "bcc"):
		number = 3
		pass

	return (cmd[endIndex:].stripl() , (number , email))


if __name__ == "__main__":
	print("Testing emails...")
