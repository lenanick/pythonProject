# 1. Создать переменную типа String
item_1 = 'Lena'
print(type(item_1))

# 2. Создать переменную типа Integer
item_2 = 25
print(type(item_2))

# 3. Создать переменную типа Float
item_3 = 2.5
print(type(item_3))

# 4. Создать переменную типа Bytes
item_4 = b"Hello"
print(type(item_4))

# 5. Создать переменную типа List
item_5 = ['Qa', 'Developer', 'PM']
print(type(item_5))

# 6. Создать переменную типа Tuple
item_6 = ('Elena', 25, 'Illia')
print(type(item_6))

# 7. Создать переменную типа Set
item_7 = {'QA', 1, 2}
print(type(item_7))

# 8. Создать переменную типа Frozen set
item_8 = frozenset('QA Manual')
print(type(item_8))

# 9. Создать переменную типа Dict
item_9 = {'age': 38}
print(type(item_9))

# 10. Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
a = 'QA'
b = 'Manual'
i = a +' '+ b
print(i)

# 11. Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(item_1,item_2)

# 13 Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(item_1 +' '+ str(item_2))
