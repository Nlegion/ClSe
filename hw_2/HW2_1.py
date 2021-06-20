import csv, os, re


def get_data(file):
    with open("hw2/{0}.txt".format(file), mode='rb') as f_n:
        result = []
        for line in f_n.readlines():
            result += re.findall(r'^(\w[^:]+).*:\s+([^:\r,\n]+)\s*$', line.decode('cp1251'))
        f_n.close()
    return result


def write_to_csv(data):
    with open('hw2/exit.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
        csv_file.close()
    return ('Файл записан')


files = ['info_1', 'info_2', 'info_3']
os_prod, os_name, os_code, os_type = [], [], [], []
main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
for item in files:
    for get in get_data(item):
        os_prod.append(get[1]) if get[0] == main_data[0][0] else None
        os_name.append(get[1]) if get[0] == main_data[0][1] else None
        os_code.append(get[1]) if get[0] == main_data[0][2] else None
        os_type.append(get[1]) if get[0] == main_data[0][3] else None
for i in range(len(os_prod)):
    main_data.append([os_prod[i], os_name[i], os_code[i], os_type[i]])

print(write_to_csv(main_data))