print('__Задание 1__')
cook_book = {}
with open("C:/Users/lysot/OneDrive/Рабочий стол/recipes.txt", 'r', encoding='utf-8') as f:
    recipes_list = f.readlines()
    recipes_list1 = []
    start = 0

    for el in recipes_list:
        if el == '\n':
            ind = recipes_list.index('\n')
            recipes_list1.append(recipes_list[start:ind])
            start = ind
            del recipes_list[ind]
        if el == recipes_list[-1]:
            recipes_list1.append(recipes_list[start:-1])

    for lst in recipes_list1:
        for i in range(len(lst)):
            lst[i] = lst[i].rstrip()

    keys_list = ['ingredient_name', 'quantity', 'measure']
    for lst in recipes_list1:
        l = []
        for el in lst[2:]:
            el = el.split(' | ')
            l.append(dict(zip(keys_list, el)))
        cook_book[lst[0]] = l

    print(cook_book)
    print()
    print('__Задание 2__')


def get_shop_list_by_dishes(dishes, person_count):
    ingr_dict = {}
    for dishe in dishes:
        for el in cook_book[dishe]:
            name = el['ingredient_name']
            quantity = el['quantity']
            measure = el['measure']
            ingr_dict.setdefault(name, {}).setdefault('measure', measure)
            ingr_dict[name]['quantity'] = ingr_dict.setdefault(name).setdefault('quantity',
                                                                                    int(quantity) * person_count)
    return dict(sorted(ingr_dict.items()))


dishes = ['Омлет', 'Запеченный картофель']
person_count = 2
print(get_shop_list_by_dishes(dishes, person_count))
print()

print('__Задание 3__')
len_dict = {}
doc1 = '1.txt'
doc2 = '2.txt'
doc3 = '3.txt'

with open(f"C:/Users/lysot/OneDrive/Рабочий стол/{doc1}", 'r', encoding='utf-8') as f:
    file = f.readlines()
    len_dict.setdefault(doc1, file)

with open(f"C:/Users/lysot/OneDrive/Рабочий стол/{doc2}", 'r', encoding='utf-8') as f:
    file = f.readlines()
    len_dict.setdefault(doc2, file)

with open(f"C:/Users/lysot/OneDrive/Рабочий стол/{doc3}", 'r', encoding='utf-8') as f:
    file = f.readlines()
    len_dict.setdefault(doc3, file)

for k in sorted(len_dict, key=lambda k: len(len_dict[k])):
    print(k)
    print(*len_dict[k])
