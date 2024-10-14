from roll.roll import Roll
import json
class RollController:
    def __init__(self, roll):
        self.roll = roll

    def restaurant_view(self):  # показ меню
        return f"Ролл: {self.roll.get_name()}, Основной ингредиент: {self.roll.get_main_ingredient()}"

    def website_view(self): # показ меню на сайте
        return (f"Ролл: {self.roll.get_name()}, Основной ингредиент: {self.roll.get_main_ingredient()}, "
                f"Начинка: {', '.join(self.roll.get_fillings())}")

    def update_roll(self, rice_weight=None, seaweed_weight=None, fillings=None):  # обнавление блюда
        if rice_weight is not None:
            self.roll.set_rice_weight(rice_weight)
        if seaweed_weight is not None:
            self.roll.set_seaweed_weight(seaweed_weight)
        if fillings is not None:
            self.roll.update_recipe(fillings=fillings)

    def check_access(self, access_level):  # проверка на доступ
        return access_level == "admin"

    def save_roll_to_json(self, filename):  # сохранение данных в json

        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.roll.to_dict(), json_file, ensure_ascii=False, indent=4)

    def load_roll_from_json(self, filename):  # загрузка данных о блюде в json

        try:
            with open(filename, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                self.roll = Roll.from_dict(data)
        except FileNotFoundError:
            print("Файл не найден.")
        except json.JSONDecodeError:
            print("Ошибка чтения файла.")