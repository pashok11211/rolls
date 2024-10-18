import json

class RollView:
    """
    Класс для представления информации о ролле для пользователя.
    """
    def show_roll(self, roll):
        """
        Выводит краткую информацию о ролле.

            roll: Объект класса Roll, представляющий ролл.
        """
        print("Информация о ролле:")
        print(f"Название: {roll.get_name()}")
        print(f"Основной ингредиент: {roll.get_main_ingredient()}")
        print(f"Вес риса: {roll.get_rice_weight()} г")
        print(f"Вес водорослей: {roll.get_seaweed_weight()} г")
        print(f"Начинки: {', '.join(roll.get_fillings())}")

    def show_info(self, data):
        """
        Выводит подробную информацию о ролле из словаря данных.

            data: Словарь данных о ролле.
        """
        print("Информация о ролле:")
        for key, value in data.items():
            print(f"{key}: {value}")

    def save_order_to_json(self, filename, order_data):
        """
        Сохраняет данные о заказе в JSON-файл.

            filename: Путь к файлу.
            order_data: Данные о заказе.
        """
        with open(filename, 'w') as file:
            json.dump(order_data, file)

class AdminView:
    """
    Класс для представления администраторского вида ролла.
    """
    def show_edit_options(self, roll):
        """
        Предлагает администратору редактировать параметры ролла.

            roll: Объект класса Roll, представляющий ролл.
        """
        print("Редактирование ролла:")
        print(f"Текущее название: {roll.get_name()}")
        new_name = input("Введите новое название : ")
        if new_name:
            roll.set_name(new_name)

        new_main_ingredient = input("Введите новый основной ингридиент : ")
        if new_main_ingredient:
            roll.set_main_ingredient(new_main_ingredient)

        new_rice_weight = input("Введите новый вес риса (г) : ")
        if new_rice_weight:
            roll.set_rice_weight(float(new_rice_weight))

        new_seaweed_weight = input("Введите новый вес водорослей (г) : ")
        if new_seaweed_weight:
            roll.set_seaweed_weight(float(new_seaweed_weight))

        print("Текущие начинки:", ', '.join(roll.get_fillings()))
        fillings = input("Введите новые начинки через запятую : ")
        if fillings:
            roll.update_recipe(fillings=[filling.strip() for filling in fillings.split(',')])

        print("Ролл был обновлен.")

    def show_admin_view(self, roll):
        """
        Выводит администраторский вид ролла, позволяющий редактировать его параметры.

            roll: Объект класса Roll, представляющий ролл.
        """
        self.show_edit_options(roll)