from socket import *
import json
import time
import sys


def client_param():
    if sys.argv == 3:
        for param1, param2 in sys.argv:
            host = param1
            port = param2
    elif sys.argv == 2:
        for param in sys.argv:
            host = param
            port = 7777
    else:
        host = '127.0.0.1'
        port = 7777

    return host, port


def data_clients_input():
    account_name = input("Введите имя: ")
    action = "presence"
    data_time = time.time()
    data_type = "online"
    data_client_json = {"action": action,
                        "time": data_time,
                        "type": data_type,
                        "user": {
                            "account_name": account_name,
                            "status": "Статус норм"}}
    data_clients_presence = json.dumps(data_client_json, ensure_ascii=False)

    return data_clients_presence


def client_data_encode():
    data_client = data_clients_input()
    data_to_send = data_client.encode('UTF-8')
    return data_to_send


def server_responce_to_str(a):
    server_responce = a
    server_responce = server_responce.decode('UTF-8')
    server_responce = json.dumps(server_responce, ensure_ascii=False, sort_keys=True, indent=2)
    return server_responce


host, port = client_param()
s = socket(AF_INET, SOCK_STREAM)
client_data_to_send = client_data_encode()
s.connect((host, port))
s.send(client_data_to_send)
tm = s.recv(10000)
tp = server_responce_to_str(tm)
print(tp)
s.close()
