import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind(('localhost',port))
s.listen(1)
print(host)
print("Waiting for Connection")
con,addr = s.accept()
print(addr," Connection established")

fName = input(str("Enter name of file: "))
theFile = open(fName,'rb')
theFile_data = theFile.read(2048)
con.send(theFile_data)
print("Data sent succesfully")