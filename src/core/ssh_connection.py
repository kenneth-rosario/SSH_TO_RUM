import paramiko

class SSHConnection:
	HOST = "rumad.uprm.edu"
	USERNAME = "estudiante"
	PASSWORD = ""
	can_connect = False
	can_return_channel = False

	def __init__(self):
		self.can_connect = True
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

	def connect(self):
		if self.can_connect:
			self.client.connect(self.HOST, username=self.USERNAME, password=self.PASSWORD)
			self.can_connect = False
			self.can_return_channel = True
		else:
			raise ValueError("Still cannot connect")

	def get_channel(self):
		if self.can_return_channel:
			self.can_return_channel = False
			return self.client.invoke_shell(width=500, height=500)
		else:
			raise ValueError("Still Cannot Return Channel")

	def channel_return_ready(self):
		return self.can_return_channel

	def close(self):
		self.client.close()
		self.can_connect = True
		self.can_return_channel = False
