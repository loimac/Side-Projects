import socket

s = socket.socket()
port = 8080
s.connect(('localhost',port))
print("Connection established")

fName = input(str("Please enter the file name to download: "))
theFile = open(fName,'wb')
theFile_data = s.recv(2048)
theFile.write(theFile_data)
theFile.close()
print("File retrieved.")