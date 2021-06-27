from socket import *
import json
import time
import sys
import log.server_log_config
import logging


def server_param():
    if sys.argv == 3:
        for param1, param2 in sys.argv:
            port = param1
            host = param2
    elif sys.argv == 2:
        for param in sys.argv:
            port = param
            host = ''
    else:
        host = ''
        port = 7777
    logger.info(f'server param {host}, {port}')
    return host, port


def client_data_to_dict(a):
    data_client = a
    objs = json.loads(data_client)
    client_responce = dict()
    for section, commands in objs.items():
        client_responce[section] = commands
    logger.info(client_responce)
    return client_responce


def server_responce_200(account_name):
    server_answer = {
        "response": 200,
        "alert": "Имя {}! Время: {}".format(account_name, time.time())
    }
    print(server_answer)
    return server_answer


def server_responce(client_responce):
    if client_responce['action'] == 'presence':
        account_name = client_responce['user']['account_name']
        answer = server_responce_200(account_name)
        return answer
    else:
        return SERVER_RESPONSE_ERROR


SERVER_RESPONSE_200 = {
    "response": 200,
    "alert": "Необязательное сообщение/уведомление"}

SERVER_RESPONSE_ERROR = {
    "response": '4xx / 5xx',
    "time": '<unix timestamp>',
    "error": "error message (optional)"}

logger = logging.getLogger('server')
if __name__ == '__main__':
    logger.debug('App started')

    host, port = server_param()
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    while True:
        client, addr = s.accept()
        logger.info(f'incom mess from {client},{addr}')
        data = client.recv(1024)
        print("Запрос от: {}".format(str(client)))
        try:
            data_client = data.decode('UTF-8')
        except ConnectionResetError as e:
            logger.error(e)
            break
        server_responce1 = client_data_to_dict(data_client)
        server_responce2 = server_responce(server_responce1)
        server_responce_json = str(server_responce2).encode('UTF-8')

        try:
            client.send(server_responce_json)
        except ConnectionResetError as e:
            logger.error(e)
            break
        logger.debug('App ending')
        client.close()
