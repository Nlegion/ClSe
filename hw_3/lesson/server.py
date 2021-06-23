from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

while True:
    client, adr = s.accept()
    # print(f'Подключение по адресу{adr}')
    # time_str = time.ctime(time.time())
    # client.send(time_str.encode('utf-8'))
    data = client.recv(1024)
    decoded_data = data.decode('UTF-8')
    print(f'Сообщение от клиента: {decoded_data}')
    msg_to_client = 'Сообщение получено'
    client.send(msg_to_client.encode('UTF-8'))
    client.close()
