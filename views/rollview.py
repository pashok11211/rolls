import json
class RollView:
    def show_roll(self, roll):  # показ ролла
        print("Информация о ролле:")
        print(f"Название: {roll.get_name()}")
        print(f"Основной ингредиент: {roll.get_main_ingredient()}")
        print(f"Вес риса: {roll.get_rice_weight()} г")
        print(f"Вес водорослей: {roll.get_seaweed_weight()} г")
        print(f"Начинки: {', '.join(roll.get_fillings())}")

    def save_order_to_json(self, filename, data):  # сохранение ордера
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def get_data_from_json(self, level, filename):  # почлучение даты от json
        if level < 1:
            return "Доступ запрещен."

        try:
            with open(filename, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return "Файл не найден."

    def show_info(self, data):  # показывает информацию
        print("Информация о ролле:")
        for key, value in data.items():
            print(f"{key}: {value}")

class AdminView:
        def show_edit_options(self, roll):  # показывает изменения

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

        def show_admin_view(self, roll):  # показывает изменения админу
            self.show_edit_options(roll)


