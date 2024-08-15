import socket
s= socket. socket()
port = 56789
s.connect(('172.26.82.139',port))
print(s.recv(1024))
s.close()
