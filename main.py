def add_dish(file, cook_book):
    dish_name = file.readline().strip().lower()
    number_of_ingridients = int(file.readline().strip())
    ingridients = []
    for i in range(number_of_ingridients):
        line = (file.readline().strip()).split(' | ')
        ingridients.append({'ingridient_name': line[0], 'quantity': int(line[1]), 'measure': line[2]})
    cook_book[dish_name] = ingridients

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                                        shop_list_item['measure']))

def create_shop_list():
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as file:
        while True:
            add_dish(file, cook_book)
            if not file.readline():
                break
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)

create_shop_list()