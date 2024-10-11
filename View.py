import json


class View:
    def show_info(self, data):
        print("Информация о блюде:", data)

    def show_dish_image(self, image_path):
        print(f"Изображение расположено по пути: {image_path}")

    def save_order_to_json(self, filename, order_data):
        with open(filename, 'w') as json_file:
            json.dump(order_data, json_file)
            print(f"Файл '{filename}' успешно сохранен.")

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