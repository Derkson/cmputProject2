from dates import *
from emails import *
from terms import *
# global mode stuff
mode = "full"


def starts_with(string, substring):
	return 	string.find(substring) == 0

def starts_with_email(string):
	return starts_with(string, "to") or \
			starts_with(string, "from")  or \
			starts_with(string, "cc")  or \
			starts_with(string, "bcc")

def handle_mode(cmd):
	global mode
	if cmd == "output=brief":
		mode = "breif"
		return cmd[12:]
	elif cmd == "output=full":
		mode = "full"
		return cmd[11:]
	else:
		raise Exception("Invalid Mode change")

def handle_command(cmd):
	global mode
	obj = None
	datelist = []
	emaillist = []
	termlist = []
	while cmd != "":
		cmd = cmd.strip()

		if starts_with(cmd, "output="):
			print("MODE")
			cmd, obj = handle_mode(cmd)
			break; # only allowd to have mode change

		if cmd == "exit()":
			# Custom Exit command
			raise KeyboardInterrupt()

		if starts_with(cmd, "date"):
			cmd, obj = process_date_q(cmd.strip())
			print(obj)
			if obj != None:
				datelist.append(obj)
				continue

		if starts_with_email(cmd):
			cmd, obj = process_email_q(cmd.strip())
			print(obj)
			if obj != None:
				emaillist.append(obj)
				continue

		cmd, obj = process_term_q(cmd.strip())
		print(obj)
		termlist.append(obj)

	valid_pool = []
	if datelist is not []:
		valid_pool.append(get_date_rows(datelist))
	if termlist is not []:
		valid_pool.append(get_term_rows(termlist))
#	if emaillist is not []:
#		valid_pool.append(get_email_rows(emaillist))	

	valid_pool = set.intersect(*valid_pool)
	return printEmails(valid_pool)

def printEmails(actualSet):
	database = db.DB()
	database.open('re.idx', None, db.DB_BTREE, db.DB_CREATE)
	cur = database.cursor()

	for row in actualSet:
		print(cur.set(row))

def main():
	global mode
	while True:
		try:
			# prompt for a command
			handle_command(input("> ").strip())
		except KeyboardInterrupt as e:
			print("\nBye!")
			exit(0)
#		except Exception as e:
#			print(e)

if __name__ == "__main__":
	main()
