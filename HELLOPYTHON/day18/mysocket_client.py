import socket 
import threading
import time

def thread_recv(cs):
    while True: 
        data = cs.recv(1024) 
        print('\nReceived from the server :',repr(data.decode()))

def thread_send(cs):
    while True: 
        message = input('Enter Message : ')
        if message == 'quit':
            break
        txt = '{}:{}'.format(cs.getsockname()[0], message)
        cs.send(txt.encode()) 

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client_socket.connect(('192.168.42.38', 9999)) 

# print(client_socket.getsockname()[0])

my_t1 = threading.Thread(target=thread_recv,args=(client_socket,))
my_t1.start()
my_t2 = threading.Thread(target=thread_send,args=(client_socket,))
my_t2.start()

# my_t1.join()
# my_t2.join()


while True:
    time.sleep(1)
    pass

client_socket.close()