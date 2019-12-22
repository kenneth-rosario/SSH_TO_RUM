import paramiko
import time
from core import SSHConnection

## simple experimentation to see how everything looks in linux ##
def test1():

    client = SSHConnection()

    client.connect()

    channel = client.get_channel()

    channel.send('5')

    time.sleep(3)

    if channel.recv_ready():
        output = channel.recv(9999).decode('latin-1')
        print(output)

    client.close()
