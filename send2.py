import socket               # Import socket module
import sys
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345          # Reserve a port for your service.

s.connect((host, port))

f = open('Ms-Tus-2016-DesiSCR-x264-AAC-Kp.mp4','rb')
print 'Sending...'
l = f.read(10240)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(10240)

print "Done Sending"
s.shutdown(socket.SHUT_WR)
print s.recv(1024)

s.close
