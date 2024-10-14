import json
from datetime import datetime

class Model:
    def __init__(self):
        self.data = {"info": "Информация о блюде"}

    def update_data(self, new_data):  # обновление данных
        if isinstance(new_data, dict):
            self.data.update(new_data)
            return True
        return False

    def get_data(self):  # получение данных
        return self.data

    def get_dish_image(self, dish_name):  # получение фото
        images = {
            "Калифорнийский ролл": "static/images/roll.jpg",
            "Пицца": "static/images/pizza.jpg"
        }
        return images.get(dish_name, "Изображение не найдено")

    def create_dish(self, dish_name, description):  # создание блюда
        self.data['dish_name'] = dish_name
        self.data['description'] = description

    def create_order_json(self, order_name):  # создание ордера

        order_info = {
            "order_name": order_name,
            "timestamp": datetime.now().isoformat()
        }

        with open(f"{order_name}.json", "w", encoding="utf-8") as json_file:
            json.dump(order_info, json_file, ensure_ascii=False, indent=4)

    def read_order_json(self, filename): # чтение ордера json'ом

        try:
            with open(filename, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return "Файл не найден"
        except json.JSONDecodeError:
            return "Ошибка чтения файла"