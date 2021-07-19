import socket 
from _thread import *

#에코 서버는 망에 붙은 사람들에게 다 보내주는것 , QOS보장
# 쓰레드에서 실행되는 코드입니다. 

# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다. 
def threaded(client_socket, addr): 

    print('Connected by :', addr[0], ':', addr[1]) 



    # 클라이언트가 접속을 끊을 때 까지 반복합니다. 
    while True: 

        try:

            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)

            if not data: 
                print('Disconnected by ' + addr[0],':',addr[1])
                break

            print('Received from ' + addr[0],':',addr[1] , data.decode())
            
            for cs in client_sockets:
                cs.send(data)

            #client_socket.send(data) 

        except :#ConnectionResetError as e:
            for idx,cs in enumerate(client_sockets):
                if cs == client_socket:
                    client_sockets.pop(idx)
                    print("idx",idx)
                    break
            
            print('Disconnected by ' + addr[0],':',addr[1])
            break
             
    client_socket.close() 


HOST = '192.168.42.38'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

client_sockets = [] #알바생들의 현황(쓰레드)


print('server start')


# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.
# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다. 
while True: 

    print('wait')


    client_socket, addr = server_socket.accept() #accept하는 순간 멈춤(손님이 들어온 순간)
    client_sockets.append(client_socket)
    start_new_thread(threaded, (client_socket, addr)) 

server_socket.close() 