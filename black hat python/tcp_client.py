import socket

target_host = "www.google.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #1

#connect the client
client.connect((target_host,target_port))  #2

#send some data
client.send(b"GET / HTTP/1.1\nHOST: google.com\r\n\r\n") #3

#recive some date
response = client.recv(4096)

print(response.decode())
client.close()