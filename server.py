from rs import ReverseShell

if __name__ == '__main__':
	# Creates a new reverse shell instance.
	with ReverseShell() as rs:
		# Binds the reverse shell to port 55555.
		rs.bind()