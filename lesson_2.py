item_1 = 1
item_0 = 1

name = 'Lena'
name_e =''
items_list = ['11', 22]
items_list_e = []


b_item_t = True
b_item_f = False

compare_item = item_1 > item_0

if not compare_item:
    print('-- 1 -- compare_item')

if compare_item:
    print('-- 1 -- True item')

    new_name = 'Olga'
    user_age = 30
    print('user_age', user_age)

    if new_name:

        new_user_age = user_age - 5
        print('new_user_age', new_user_age)


elif name_e:
    print('-- 2 -- Name item')
elif items_list_e:
    print('-- 3 -- items-list')
elif 10 > 20:
    print('-- 4 -- items-list')
else:
    print('False item')





