import socket 


HOST = '192.168.42.149'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

client_socket.connect((HOST, PORT)) 

while True: 
    data = client_socket.recv(1024) 

    print('Received from the server :',repr(data.decode())) 


client_socket.close()