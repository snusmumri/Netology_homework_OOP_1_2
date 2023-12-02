# Задача № 1
import pprint
f = open('recipes.txt', encoding='utf-8')

cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
  cook_book = {}
  for x in f:
      list_ingridients = []
      dish_name = x.strip()
      count_ingridients = int(f.readline())

      for i in range(count_ingridients):
        item1, item2, item3 = f.readline().split("|")
        ingridient = {'ingredient_name': item1, 'quantity': item2, 'measure': item3}
        list_ingridients.append(ingridient)
      recipe_dish = {dish_name: list_ingridients}

      cook_book.update(recipe_dish)
      f.readline()

pprint.pprint(cook_book)

#Задача № 2
def get_shop_list_by_dishes(dishes, person_count):
  list_buy = {}
  for i in dishes:
    for j in cook_book:
      if i == j:
        for x in cook_book[j]:
          prod = {list(x.values())[0]: {'measure': list(x.values())[2], 'quantity': int(list(x.values())[1]) * person_count}}
          if list(x.values())[0] not in list_buy:
            list_buy.update(prod)
          else:
            list_buy[list(x.values())[0]]['quantity'] += int(list(x.values())[1]) * person_count

  print(list_buy)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)




