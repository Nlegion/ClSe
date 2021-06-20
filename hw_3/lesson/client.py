from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
# s.connect(('localhost', 8888))
# server_time = s.recv(1024)
# s.close()
# print(f"Текущее время сервера {server_time.decode('utf-8')}")

msg_to_server = 'Сообщение'
s.send(msg_to_server.encode('UTF-8'))
data = s.recv(1024)
decoded_data = data.decode('UTF-8')
print(f"Сообщение с сервера {decoded_data}")
s.close()
