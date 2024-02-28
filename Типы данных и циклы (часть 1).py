# -*- coding: cp1251 -*-

#������� 1. ���� ����������, � ������� �������� ����� �� ��������� ����. �������� ���, ������� ������� �� �����: ������� �����, 
#���� ����� ���� � ����� ��������; ��� ������� �����, ���� ����� ���� ������.

word = list(input('������� �����: '))
if len(word) % 2 == 0:
  print(word[(len(word)-1)//2:(len(word)+2)//2])
else:
  print(word[0])
  
#������� 2. �������� ���������, ������� ��������������� ����������� � ������������ ����� (�� ������ �� ���) � 
#����� ������� ���� ������� ����� ���� ����� ��������� �����.

number = True
sum_ = 0
while number != 0:
   number = int(input('������� ����� '))
   sum_ += number
print(sum_)

#������� 3. �� ������ MVP dating-�������, � � ��� ���� ������ ������ � �������. 
#��������� ��������: ������ ������������ �� �������, ���� ������ ����������� ����� �� �������� � 
#���������� ����� � ����������� ��������� ����� ����������! �� �� �� ����� ������ ���������, ���� ���-�� ����� �������� ��� ����:

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

import re
b = re.split(r'[,;]\s?', str(boys))
b.sort()
g = re.split(r'[,;]\s?', str(girls))
g.sort()
if len(b) == len(g):
  print(f'��������� ����: {list(zip(b, g))}')
else:
  print('��������, ���-�� ����� �������� ��� ����!')
  
#������� 4. � ��� ���� ������, ���������� ���������� � ������������� ����������� � ����������� �� ������������ ������ �� ������� 
#(��������� ������ � �������). ���������� �������� ���, ������� ���������� ������� ����������� �� ������ � ��������(!) 
#��� ������ ������.

countries_temperature = [
    ['�������', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['��������', [57.2, 55.4, 59, 59, 53.6]],
    ['������', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['������', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
print('������� ����������� � �������: ')
for element in countries_temperature:
    v = ((sum(element[1]) - (32 * len(element[1]))) / 1.8) / len(element[1])
    print(element[0],'-', round(v,1), 'C')
    
#������� 5. ������� ������ � ������������� ��������. ���������� �������� ���, ������� �������� ������ ����� �� ���������� 
#(1 �����, 3 �����, 2 �����, 2-3 �����). �������� ��������, ��� �� ��� ����� �������������� �������� ������������ 
#� ������������ �������.
#���� ����� �������, �� ������� ��� � ������ �������� (������ ����), � ���� �� ������� � ������� �����. 
#��� ������� ������� ���������� ���������, � �������� ����� ���������� �� ��������.

import re
car_ids = ['�222��96', '��22��193']
for element in car_ids:
    if re.findall(r'\w\d{3}\w{2}\d{2,3}', element):
        print('�����', element[0:6], '�������. ������', element[6:])
    else:
        print('�����', element, '�� �������')   
        
#������� 6. ��� ����� ����� �� ���������� ������������� ������� ��� ������� ������������ (������������,����;���������). 
#��� ���������� �������� ��������, ������� ������� ������� �������� ���������� �� ������������. 
#�. �. ���� ��������� ��������� ����� ���� ���������� � ���������� ���������� �������������. 
#� ��� ���������� ��������� �������� ������� ����������.

import re
stream = [
    'user4,2021-01-01;3',
    'user3,2022-01-07;4',
    'user2,2022-03-29;1',
    'user1,2020-04-04;13',
    'user2,2022-01-05;7',
    'user1,2021-06-14;4',
    'user3,2022-07-02;10',
    'user4,2021-03-21;19',
    'user4,2022-03-22;4',
    'user4,2022-04-22;8',
    'user4,2021-05-03;9',
    'user4,2022-05-11;11'
]

stream = [
    'user100,2022-01-01;150',
    'user99,2022-01-07;205',
    'user1001,2022-03-29;81'
]

total_views = sum([int(re.split('[,;]', element)[2]) for element in stream])
no_of_users = len(set([re.split('[,;]', element)[0] for element in stream]))
print(f'������� ����� ���������� �� ����������� ������������: {total_views / no_of_users :.2f}')