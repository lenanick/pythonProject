
# print("Hello future QA Automation")

item = 1
name = 'Lena'
result = str(item)+ ' ' + name
print(result)

items = [item, name, 'Illia', 33, [11,22,"hello"], {'age':30}, True, False, (0,1,3), 4.5]

print(len(items))

print(items[4][2])

dict_items = {'age':38,
              'name': "Lena",
              'location': {'country':'Ukraine',
                           'city':'Ivano-Frankivsk'}}

print(type(dict_items), dict_items['location']['city'])




