import socket
mysock = socket.socket(socket.AF_INET)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr43.org/romeo.txt HTTP'