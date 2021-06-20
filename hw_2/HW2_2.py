# Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными.
# Для этого:
# Создать функцию write_order_to_json(),
# в которую передается 5 параметров — товар (item),
# количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import os
import json


def write_order_to_json(item, quantity, price, buyer, date):
    filename = os.path.join('hw2/', 'orders.json')

    if os.path.exists(filename):
        data = {}

        with open(filename, encoding="utf-8") as fl:
            data = json.loads(fl.read())

        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

        with open(filename, "w", encoding="utf-8") as fl:
            json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)

        print('Данные добавлены')

    else:
        print('Исходный файл не найден')


if __name__ == '__main__':
    write_order_to_json('test_1', '1', '1', 'test1', '01.01.1900')
    write_order_to_json('test_2', '2', '2', 'test2', '02.02.1900')
    write_order_to_json('test_3', '3', '3', 'test3', '03.03.1900')
