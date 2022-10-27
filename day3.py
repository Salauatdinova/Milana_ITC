import math
# a = 2**3
# b = 3**2
# if a>b:
#         print(a)
# else:
#         print(b)


# a = int(input("Enter number: "))
# if 0<a<21 or 100>a>57:
#     print('Разрешенная цифра')
# else:
#     print("Запрещенная цифра ")


# a = int(input("Ввведите число: "))

# if a > 100 or a < 0:
#     print("Out of range")
# elif a > 0 and a < 21:
#     print("разрещенная цифра")
# elif a>57 and a<100:
#     print("разрещенная цифра")
# else:
#     print("Запрещенная цифра")

# a = int(input("Ввведите число: "))

# if a % 2 ==0:
#     print('четное')
# else:
#     print("Нечетное число")
# if a % 3 ==0:
#     print("Делится на три без остатка")
# else:
#     print('Не делится на три')


# if True:
#     print("True")
# a = 17
# if a > 10 :
#     print('true')

#     a = 10//5
#     b = 10/5
#     if a == b:
#         print(a+b)


# a = 10
# b = 5
# if a > 0 and b > 0:
#     print('числа положительные')


# if a > b:
#     print(a+2)
# else:
#     print(b+2)


# a = int(input("Enter number: "))
# if a>0:
#     print('Положительное число')
# else:
#     print('Отрицательное число')


# a = int(input('Enter number'))
# if a>18:
#     print('совершеннолетний')
# elif a < 4:
#     print('Ребенок')


# a = 45
# b = 6
# if a%b==0:
#     print('Делится')
# else:
#     print('Неделится')


# a = 25
# b = 35
# c = 75
# if b > a < c:
#     print('min:', a)
#     if b>c :
#         print('max: ' ,c)
#     else:
#         print('max: ',c)
# elif a>b<c:
#     print('min: ', b)
# elif a>c<b:
#     print('min: ', c)


# num1 = int(input("Введите первое число: "))

# num2 = int(input("Введите второе число: "))

# print("Result:", num1 + num2)


# word = "HI"
# print(word * 2)


# a = ['hello', 12, 1.9, True, [1, 2, 4, 5]]


# s = a.index(1.9)
# a.pop(s)
# print(a)


#  print(a[::-1])
# print(a.count(12)

# print(a)
# a.remove('hello')
# print(a)


# a = [1, 2, 3, 4, 5, 6]
# b = [7, 8, 9, 10, 11, 12]

# a.extend(b)
# print(a+b)


# d = []
# d.append((1, 4, 5, 7, 9))
# d.append((1, 3, 4))
# print(d)


# s = (3456, 87654)
# d.append(s)


# a = (1, 2, 3, 4, )
# print(tuple(a))


# a = tuple([1, 2, 3, 4])
# print(a)

# lst = [1,2,3,4,5]
# print(type(lst))
# print(lst)

# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)


# from unicodedata import name


# class_a = [32, 67, 90, 12, 9, 7, 45, 10, 7, 9, 11]

# print(class_a[9])
# class_a.append(55)
# print(class_a)
# s = class_a.index(55)
# print(class_a[s])
# class_a.remove(45)
# print(class_a)

# s = class_a.index(45)
# print(class_a[s])
# class_a.pop(s)
# print(class_a)

# a = [1, 2, 3, 35, 4, 5, 6]
# s = max(a)
# n = min(a)

# list_1 = []
# list_2 = []


# i = int(input('>>  '))
# if i % 2 == 0:
#     list_1.append(i)
# else:
#     list_2.append(1)
#     print(list_1, list_2)


# products = [
#   '0 яблоко',
#   '1 груша',
#   '2 арбуз',
#   '3 банан',
#   '4 мандарин'
# ]
# print(products)
# i = int(input('Введите индекс '))

# if i >= 0 and i <=4 :
#     print(f"Мы удалили: {products[i]}")
#     products.pop(i)
#     print(products)

# else:
#     print('продукт с таким индексом не существует')


# points = 0
# print(points)
# i = int(input('сколько будет 5+6:    10, 12, 11 : '))

# if i == 11:
#     points += 1

# print(points)


# a = {1212, 89, 789.678}
# методы уд.
# a.remove(89)
# a.pop()
# a.clear()
# a.discard(1346)

# методы доб.
# a.add(14)
# a.update([1,23,4,5])

# методы срав.
# a = {1212, 43, 90, 89}
# b = {12, 4, 90, 89}

# Возр.объекты которые есть и во множестве a и b


# a = {213:123, 'key': 'value'}

# a['new'] = 145
# a.['key'] = {'run': True}
# a.['key2'] = {'run': True}

# a.update({'run': True})

# print(a)

# a = {
#     "key": 'value',
#     'key2': {'run': True},
#     'key3': {'run3': True},
# }
# print(a.get('key3'))
# print(a['key3'])


# dates_of_birth = {3,10,11,7,31,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)


# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

# print(farm_1.intersection(farm_2))

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

# print(farm_1.difference(farm_2))


# a = set()
# a.update(['23','27','7','55','1'])
# print(a)
# a.pop()
# print(a)


# menu = {"besh_barmek": "130", "lagman": "130", "plov": "125", "chai": "10"}

# print(menu)

# menu["lagman"] = "135"

# print(menu)
# menu.pop("plov")
# print(menu)
# "drinks")


# a = {'bugyu', 567567, 6 , 8 ,567, 'vghvgh'}

# b = {'bugyu', 567567, 6 , 8 ,567, 'vghvgh', 67, 'vgh'}

# print(a)

# a.add('33')

# print(a)

# a.remove('bugyu')

# print(a)

# a.update('Mika', '23')

# print(a)
# l = ['bgbvvghbgh','nhnhj',5656]

# a.intersection_update(b)
# print(a)

# a.update(l)
# print(a)

# print(a.difference(b))
# print(a)

# a.discard('a')
# print(a)

# a.clear()

# print(a)
# # b.clear()
# print(b)
# {'bgbvvghbgh', 6, 8, 'vghvgh', 567567, 'M', '2', 5656, 'a', 'nhnhj', '3', 'i', '33', 'k



# from pprint import pprint


# my_friends = {
#     "Joomart": "+77555246810",
#     "Adinai": "+77555013579",
#     "Ermek": "+77777013579",
#     "Atai": "+77777246810",
#     "Alymbek": "+77555501234",
# }

# his_her_friends = {
#     "Lyazat": "+77551123456",
#     "Salavat": "+77552234567",
#     "Daniyar": "+77553345678",
#     "Bolot": "+77554456789",
#     "Alymbek": "+77555501234",
#     "Dastan": "+77556678912",
#     "Maksat": "+77557789012",
#     "Adinai": "+77555013579",
# }
# our_friends = {}
# our_friends.update(my_friends)
# # pprint(my_friends)
# our_friends.update(his_her_friends)
# # pprint(our_friends)

# print(my_friends['Joomart'])
# print(his_her_friends['Salavat'])



# a = int(input('vvedi chislo:'))

# r = range(0, 22, 2)
# print(a in r)


# r = range(0, 22, 2)

# print(r

#  ['Almaty', 'Pavlodar', 'Korday']

# словари
# b = {
#     'Almaty': 000,
#     'Pavlodar': 140,
#     'Korday': 400
# }
# r = dict(Almaty=000,Pavlodar=140,Korday=400)
# t = dict.fromkeys(['a','b','c'],100)
# print(t)


#2

# user = input('Введите почту: ')
# a = user.endswith('@gmail.com')
# b = user.endswith('email.ru')
# if a or b == True: 
#     pasford = 123456
#     print(pasford)
# else:
#     print('Не верный формат почты')

# past = int(input('Подвердите пороль'))

# if past == pasford:
#     print('Подверждение прошло успешно')  
# else:
#     print('Не удалось подвердить почту ')


#10


# marks = {}
# marks ['Bill']=int(input('Enter mark for Bill:'))
# marks ['Jane']=int(input('Enter mark for Jane:'))
# marks ['john']=int(input('Enter mark for John:'))
# marks ['Mary']=int(input('Enter mark for Mary:'))

# a = sum(marks.values())/len(marks.values())
# sum_m = math.ceil(a)
# print(f"Enter mark for Bille {marks['Bill']}")
# print(f"Enter mark for Jane {marks['Jane']}")
# print(f"Enter mark for John {marks['john']}")
# print(f"Enter mark for Mary {marks['Mary']}")
# print('average mark :', sum_m)













    
    




