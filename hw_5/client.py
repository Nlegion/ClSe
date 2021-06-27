from socket import *
import json
import time
import sys
import log.client_log_config
import logging


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
    try:
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
        start_info = f'Connected to server: {data_time}:{account_name}'
        logger.info(start_info)
        return data_clients_presence
    except ConnectionResetError as e:
        logger.error(e)
        exit(1)


def client_data_encode():
    data_client = data_clients_input()
    data_to_send = data_client.encode('UTF-8')
    return data_to_send


def server_responce_to_str(a):
    server_responce = a
    server_responce = server_responce.decode('UTF-8')
    server_responce = json.dumps(server_responce, ensure_ascii=False, sort_keys=True, indent=2)
    return server_responce


logger = logging.getLogger('client')

if __name__ == '__main__':
    logger.debug('App started')
    host, port = client_param()
    s = socket(AF_INET, SOCK_STREAM)
    client_data_to_send = client_data_encode()
    try:
        s.connect((host, port))
    except ConnectionResetError as e:
        logger.error(e)
    try:
        s.send(client_data_to_send)
        tm = s.recv(10000)
        logger.info(f'Data sended to {client_data_to_send}')
    except ConnectionResetError as e:
        logger.error(e)
    tp = server_responce_to_str(tm)
    print(tp)
    logger.debug('App ending')
    s.close()
