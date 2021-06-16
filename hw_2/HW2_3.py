# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
# второму — целое число, третьему — вложенный словарь,
# где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import os
import yaml

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join('hw2/', 'file.yaml')
data = {
    'items': ['test1', 'test2', 'test3', 'test4'],
    'items_quantity': 4,
    'items_price': {
        'test1': 'test1',
        'test2': 'test2',
        'test3': 'test3',
        'test4': 'test4'
    }
}

with open(filename, 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

with open(filename) as f_n:
    print(f_n.read())
