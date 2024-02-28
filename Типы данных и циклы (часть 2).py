# -*- coding: cp1251 -*-

#Задание 1. Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя 
#(пример структуры данных приведен ниже). Вам необходимо написать программу, 
#которая выведет на экран множество уникальных гео-меток всех пользователей.

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
ids_set = set()
for id_ in ids.values():
  ids_set = ids_set.union(id_)
print(ids_set)

#Задание 2. Дана переменная, в которой хранится список поисковых запросов пользователя 
#(пример структуры данных приведен ниже, но запросы потенциально могут быть любые). 
#Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт']
for i in set([len(i.split()) for i in queries]):
  print(f'Поисковых запросов, содержащих {i} слов(а): {len([s for s in queries if len(s.split()) == i ]) / len(queries) :.2%}')
  
#Задание 3. Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам. 
#Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: ((revenue / cost) - 1) * 100.

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

#Задание 4. Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен ниже).
#Напишите программу, которая возвращает название канала с максимальным объемом продаж.

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
max_val = max(stats.values())
stat = {el: v for el, v in stats.items() if v == max_val}
keys = list(map(str, stat.keys()))
print(f'Максимальный объем продаж на рекламном канале:', max(keys))

#Задание 5. Дан список произвольной длины. Необходимо написать код, который на основе исходного списка составит словарь 
#такого уровня вложенности, какова длина исхондого списка.

my_list = ['2018-01-01', 'yandex', 'cpc', 100]  #1.

my_list = ['a', 'b', 'c', 'd', 'e', 'f']    #2.

def dict(my_list):
    result = my_list[-1]
    for element in reversed(my_list[:-1]):
        result = {element: result}
    return result

print('Результат:', dict(my_list))

#Задание 6. Дана книга рецептов с информацией о том, сколько ингредиентов нужно для приготовления блюда в расчете на одну порцию 
#(пример данных представлен ниже). 
#Напишите программу, которая будет запрашивать у пользователя количество порций для приготовления этих блюд и 
#отображать информацию о суммарном количестве требуемых ингредиентов в указанном виде. 
#Внимание! Одинаковые ингредиенты с разными размерностями нужно считать раздельно!

cook_book = {
  'салат': [
     {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
     {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
     {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
  'пицца': [
     {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
  'лимонад': [
     {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
     {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
     {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}
purchases = int(input('Введите количество порций: '))
shopdict = {}
for dish in cook_book.values():
  for ingr in dish:
    key = (ingr['ingridient_name'], ingr['measure'])
    shopdict.setdefault(key, 0)
    shopdict[key] += ingr['quantity'] * purchases

for name, q in shopdict.items():
  print(f'{name[0]}: {q} {name[1]}')
