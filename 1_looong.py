import socket




hostname = raw_input("Hostname:")
port = input("Port: ")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))

# Es rep el missatge inicial del servidor
data = s.recv(1024)
print "Recieved", repr(data)

times = input("Number of times for the letter to be printed")
letter = raw_input("Letter to be printed: ")
number = raw_input("Final number: ")

#for i in range (1,times):
s.sendall(letter*times)

s.sendall(number)

s.shutdown(socket.SHUT_WR)

while 1:
	data = s.recv(1024)
	if data == "":
		break
	print "Recieved", repr(data)
print "Connetion Terminated"
s.close()



