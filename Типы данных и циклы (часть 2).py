# -*- coding: cp1251 -*-

#������� 1. ���� ����������, � ������� �������� �������, ���������� ���-����� ��� ������� ������������ 
#(������ ��������� ������ �������� ����). ��� ���������� �������� ���������, 
#������� ������� �� ����� ��������� ���������� ���-����� ���� �������������.

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
ids_set = set()
for id_ in ids.values():
  ids_set = ids_set.union(id_)
print(ids_set)

#������� 2. ���� ����������, � ������� �������� ������ ��������� �������� ������������ 
#(������ ��������� ������ �������� ����, �� ������� ������������ ����� ���� �����). 
#��� ���������� �������� ���������, ������� ������� �� ����� ������������� ���������� ���� � �������� � ��������� ����.

queries = [
    '�������� ������� ������',
    '������� ������',
    '����� ����',
    '���� �������',
    '������� ���� �����',
    '���� �� ������',
    '������� ��� �����']
for i in set([len(i.split()) for i in queries]):
  print(f'��������� ��������, ���������� {i} ����(�): {len([s for s in queries if len(s.split()) == i ]) / len(queries) :.2%}')
  
#������� 3. ���� ����������, � ������� �������� ���������� � �������� � ������ ��������� �������� �� ��������� ����������. 
#���������� ��������� �������� ��������� ����������� ROI, ������� ���������� �� �������: ((revenue / cost) - 1) * 100.

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
c = sorted(results.items())
for company, info in results.items():
  info['revenue']
  info['cost']
  info['ROI'] = ((info['revenue'] / info['cost']) - 1) * 100
print(*c, sep='\n')

#������� 4. ���� ����������, � ������� �������� ���������� ��������� ������� �� ������� ������ (������ ��������� ������ �������� ����).
#�������� ���������, ������� ���������� �������� ������ � ������������ ������� ������.

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
max_val = max(stats.values())
stat = {el: v for el, v in stats.items() if v == max_val}
keys = list(map(str, stat.keys()))
print(f'������������ ����� ������ �� ��������� ������:', max(keys))

#������� 5. ��� ������ ������������ �����. ���������� �������� ���, ������� �� ������ ��������� ������ �������� ������� 
#������ ������ �����������, ������ ����� ��������� ������.

my_list = ['2018-01-01', 'yandex', 'cpc', 100]  #1.

my_list = ['a', 'b', 'c', 'd', 'e', 'f']    #2.

def dict(my_list):
    result = my_list[-1]
    for element in reversed(my_list[:-1]):
        result = {element: result}
    return result

print('���������:', dict(my_list))

#������� 6. ���� ����� �������� � ����������� � ���, ������� ������������ ����� ��� ������������� ����� � ������� �� ���� ������ 
#(������ ������ ����������� ����). 
#�������� ���������, ������� ����� ����������� � ������������ ���������� ������ ��� ������������� ���� ���� � 
#���������� ���������� � ��������� ���������� ��������� ������������ � ��������� ����. 
#��������! ���������� ����������� � ������� ������������� ����� ������� ���������!

cook_book = {
  '�����': [
     {'ingridient_name': '���', 'quantity': 50, 'measure': '��'},
     {'ingridient_name': '������', 'quantity': 2, 'measure': '��'},
     {'ingridient_name': '������', 'quantity': 20, 'measure': '��'},
     {'ingridient_name': '�������', 'quantity': 10, 'measure': '��'},
     {'ingridient_name': '��������� �����', 'quantity': 20, 'measure': '��'},
     {'ingridient_name': '�����', 'quantity': 10, 'measure': '��'},
     {'ingridient_name': '�����', 'quantity': 20, 'measure': '��'}
    ],
  '�����': [
     {'ingridient_name': '���', 'quantity': 20, 'measure': '��'},
     {'ingridient_name': '�������', 'quantity': 30, 'measure': '��'},
     {'ingridient_name': '�����', 'quantity': 30, 'measure': '��'},
     {'ingridient_name': '������', 'quantity': 10, 'measure': '��'},
     {'ingridient_name': '������', 'quantity': 20, 'measure': '��'},
     {'ingridient_name': '�����', 'quantity': 100, 'measure': '��'},
    ],
  '�������': [
     {'ingridient_name': '�����', 'quantity': 1, 'measure': '��'},
     {'ingridient_name': '����', 'quantity': 200, 'measure': '��'},
     {'ingridient_name': '�����', 'quantity': 10, 'measure': '��'},
     {'ingridient_name': '����', 'quantity': 20, 'measure': '��'},
    ]
}
purchases = int(input('������� ���������� ������: '))
shopdict = {}
for dish in cook_book.values():
  for ingr in dish:
    key = (ingr['ingridient_name'], ingr['measure'])
    shopdict.setdefault(key, 0)
    shopdict[key] += ingr['quantity'] * purchases

for name, q in shopdict.items():
  print(f'{name[0]}: {q} {name[1]}')
