# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и
# также проверить тип и содержимое переменных.
arr = ['разработка', 'сокет', 'декоратор']

for line in arr:
    print('Задание 1_а. тип переменной: {0}; слово: {1} '.format(type(line), line))

arr = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
       b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
       b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']
for line in arr:
    print('Задание 1_б.тип: {0}; содержание: {1} '.format(type(line), line))

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе
# без преобразования в последовательность кодов (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

arr = [b'class', b'function', b'method']

for line in arr:
    print('Задание 2. тип: {0}; содержание: {1}; длинна: {2} '.format(type(line), line, len(line)))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

try:
    arr = ['attribute', 'класс', 'функция', 'type']
    for line in arr:
        print('Задание 3. ', line.encode())
except SyntaxError:
    print('Ошибка')
print('Задание 3. Вывод: русский язык не кодируется, в байтовом типе появляется ошибка')

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

arr = ['разработка', 'администрирование', 'protocol', 'standard']
for i in arr:
    a = i.encode('utf-8')
    print('Задание 4. ', a, type(a))
    b = bytes.decode(a, 'utf-8')
    print('Задание 4. ', b, type(b))

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
# результаты из байтовового в строковый тип на кириллице.

import subprocess

ping_resurs = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for ping_now in ping_resurs:
    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)
    i = 0
    for line in ping_process.stdout:
        if i < 1:
            print('Задание 5. ', line)
            line = line.decode('cp866').encode('utf-8')
            print('Задание 5. ', line.decode('utf-8'))
            i += 1
        else:
            break

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

resurs_string = ['сетевое программирование', 'сокет', 'декоратор']

with open('resurs.txt', 'w+') as f_n:  # запись файла
    for i in resurs_string:
        f_n.write(i + ' ')
    f_n.seek(0)
print('Задание 6. ', f_n)  # определение кодировки
file_coding = locale.getpreferredencoding()

with open('resurs.txt', 'r', encoding=file_coding) as f_n:  # считывание файла
    for i in f_n:
        print('Задание 6. ', i)
    f_n.seek(0)
