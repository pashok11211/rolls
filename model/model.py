import json
from datetime import datetime


class Model:
    def __init__(self):
        self.data = {"info": "Информация о блюде"}

    def update_data(self, new_data):
        if isinstance(new_data, dict):
            self.data.update(new_data)
            return True
        return False

    def get_data(self):
        return self.data

    def get_dish_image(self, dish_name):
        images = {
            "Калифорнийский ролл": "static/images/roll.jpg",
            "Пицца": "static/images/pizza.jpg"
        }
        return images.get(dish_name, "Изображение не найдено")

    def create_dish(self, dish_name, description):

        self.data['dish_name'] = dish_name
        self.data['description'] = description

    def create_order_json(self, order_name):

        order_info = {
            "order_name": order_name,
            "timestamp": datetime.now().isoformat()
        }

        with open(f"{order_name}.json", "w", encoding="utf-8") as json_file:
            json.dump(order_info, json_file, ensure_ascii=False, indent=4)

    def read_order_json(self, filename):

        try:
            with open(filename, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return "Файл не найден"
        except json.JSONDecodeError:
            return "Ошибка чтения файла"

    def get_data_from_json(self, level, filename):
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)

            if self.check_access(level):
                return data
            else:
                return "У вас нет прав доступа к этой информации."
        except FileNotFoundError:
            return f"Файл '{filename}' не найден."
        except json.JSONDecodeError:
            return "Ошибка при чтении данных из файла."

    def check_access(self, level):

        return level >= 1
