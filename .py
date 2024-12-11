def read_recipes_to_dict(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
    return cook_book
def main():
    # Укажите путь к файлу с рецептами
    filename = r'C:\Users\vladi\Desktop\coo\recipes.txt'
    try:
        cook_book = read_recipes_to_dict(filename)
        print("Содержимое cook_book:")
        for dish, ingredients in cook_book.items():
            print(f"{dish}:")
            for ingredient in ingredients:
                print(f"  {ingredient}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо {dish} не найдено в книге рецептов.")
            continue
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list


def main():
    filename = r'C:\Users\vladi\Desktop\coo\recipes.txt'
    try:
        cook_book = read_recipes_to_dict(filename)
        
        # Пример использования функции get_shop_list_by_dishes
        dishes = ['Запеченный картофель', 'Омлет']
        person_count = 2
        shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
        
        print("Список покупок:")
        for ingredient, details in shop_list.items():
            print(f"{ingredient}: {details}")
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
