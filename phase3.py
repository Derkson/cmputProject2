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
	remaining = cmd	
	while remaining != "":
		# clean up command
		cmd = remaining.strip()	
		# case statement for all input handlers
		if starts_with(cmd, "output="):
			remaining = handle_mode(cmd)
		elif starts_with(cmd, "date"):
			remaining = process_date_q(cmd)
		elif starts_with_email(cmd):
			remaining = process_email_q(cmd)
		elif cmd == "exit()":
			# Custom Exit command
			raise KeyboardInterrupt()
		else:
			remaining = process_term_q(cmd)


def main():
	global mode
	while True:
		try:
			# prompt for a command
			handle_command(input("> ").strip())
			print(mode)
		except KeyboardInterrupt as e:
			print("\nBye!")
			exit(0)
		except Exception as e:
			print(e)

if __name__ == "__main__":
	main()
