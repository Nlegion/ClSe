import logging
import logging.handlers
import os.path

logger = logging.getLogger('server')

formatter = logging.Formatter("%(asctime)s - %(levelname)-4s - %(module)-4s - %(message)s ")

storage_name = 'log-storage'
if not os.path.exists(storage_name):
    os.mkdir(storage_name)
filename = os.path.join(storage_name, 'server.log')

fh = logging.handlers.TimedRotatingFileHandler(filename, encoding='utf-8', when='D', interval=1, backupCount=7)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')
