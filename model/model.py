import json
from datetime import datetime

class Model:
    """
    Класс для управления данными приложения.
    """
    def __init__(self):
        """
        Инициализирует объект Model.
        """
        self.data = {"info": "Информация о блюде"}

    def update_data(self, new_data):
        """
        Обновляет данные приложения.

        new_data: Новые данные для обновления.

        True, если обновление прошло успешно, False - в противном случае.
        """
        if isinstance(new_data, dict):
            self.data.update(new_data)
            return True
        return False

    def get_data(self):
        """
        Возвращает текущие данные приложения.
        """
        return self.data

    def get_dish_image(self, dish_name):
        """
        Возвращает путь к изображению блюда.

        dish_name: Название блюда.

        Путь к изображению блюда.
        """
        images = {
            "Калифорнийский ролл": "static/images/roll.jpg",
            "Пицца": "static/images/pizza.jpg"
        }
        return images.get(dish_name, "Изображение не найдено")

    def create_dish(self, dish_name, description):
        """
        Создает новое блюдо.

        dish_name: Название блюда.
        description: Описание блюда.
        """
        self.data['dish_name'] = dish_name
        self.data['description'] = description

    def create_order_json(self, order_name):
        """
        Создает JSON-файл с информацией о заказе.

        order_name: Название заказа.
        """
        order_info = {
            "order_name": order_name,
            "timestamp": datetime.now().isoformat()
        }

        with open(f"{order_name}.json", "w", encoding="utf-8") as json_file:
            json.dump(order_info, json_file, ensure_ascii=False, indent=4)

    def read_order_json(self, filename):
        """
        Читает информацию о заказе из JSON-файла.

        filename: Путь к JSON-файлу.

         Данные о заказе, если файл успешно прочитан.
         Сообщение об ошибке, если файл не найден или произошла ошибка чтения.
        """
        try:
            with open(filename, "r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return "Файл не найден"
        except json.JSONDecodeError:
            return "Ошибка чтения файла"

    def get_data_from_json(self, level, filename):
        """
        Читает данные из JSON-файла с проверкой уровня доступа.

        level: Уровень доступа.
        filename: Путь к файлу.

        Данные из файла, если доступ разрешен.
        Сообщение об ошибке, если доступ запрещен.
        """
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
        """
        Проверяет уровень доступа.

        level: Уровень доступа.

        True, если доступ разрешен, False - в противном случае.
        """
        return level >= 1