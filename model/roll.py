import json

class Roll:
    """
    Класс, представляющий ролл.
    """
    def __init__(self, name, main_ingredient, rice_weight, seaweed_weight):
        """
        Инициализирует объект Roll.

        name: Название ролла.
        main_ingredient: Основной ингредиент.
        rice_weight: Вес риса в граммах.
        seaweed_weight: Вес водорослей в граммах.
        """
        self.name = name
        self.main_ingredient = main_ingredient
        self.rice_weight = rice_weight
        self.seaweed_weight = seaweed_weight
        self.__fillings = []  # Используем частный атрибут

    def get_name(self):
        """
        Возвращает название ролла.
        """
        return self.name

    def get_main_ingredient(self):
        """
        Возвращает основной ингредиент.
        """
        return self.main_ingredient

    def get_rice_weight(self):
        """
        Возвращает вес риса.
        """
        return self.rice_weight

    def get_seaweed_weight(self):
        """
        Возвращает вес водорослей.
        """
        return self.seaweed_weight

    def get_fillings(self):
        """
        Возвращает список начинок.
        """
        return self.__fillings  # Здесь также используем частный атрибут

    def set_name(self, name: str):
        """
        Устанавливает новое название ролла.
        """
        self.name = name

    def set_main_ingredient(self, main_ingredient: str):
        """
        Устанавливает новый основной ингредиент.
        """
        self.main_ingredient = main_ingredient

    def set_rice_weight(self, rice_weight: float):
        """
        Устанавливает новый вес риса.
        """
        self.rice_weight = rice_weight  # Исправляем доступ к атрибуту

    def set_seaweed_weight(self, seaweed_weight: float):
        """
        Устанавливает новый вес водорослей.
        """
        self.seaweed_weight = seaweed_weight  # Исправляем доступ к атрибуту

    def add_filling(self, filling: str):
        """
        Добавляет начинку в ролл.
        """
        self.__fillings.append(filling)

    def remove_filling(self, filling: str):
        """
        Удаляет начинку из ролла.
        """
        if filling in self.__fillings:
            self.__fillings.remove(filling)

    def update_recipe(self, rice_weight=None, seaweed_weight=None, fillings=None):
        """
        Обновляет рецепт ролла.

        rice_weight: Новый вес риса. Defaults to None.
        seaweed_weight: Новый вес водорослей. Defaults to None.
        fillings: Новый список начинок. Defaults to None.
        """
        if rice_weight is not None:
            self.rice_weight = rice_weight  # Исправляем доступ к атрибуту
        if seaweed_weight is not None:
            self.seaweed_weight = seaweed_weight  # Исправляем доступ к атрибуту
        if fillings is not None:
            self.__fillings = fillings

    def create_custom_roll(self, name: str, main_ingredient: str, rice_weight: float, seaweed_weight: float, fillings):
        """
        Создает новый объект Roll с заданными параметрами.

        name: Название ролла.
        main_ingredient: Основной ингредиент.
        rice_weight: Вес риса.
        seaweed_weight: Вес водорослей.
        fillings: Список начинок.
        roll: Новый объект Roll.
        """
        return Roll(name, main_ingredient, rice_weight, seaweed_weight)

    def __str__(self):
        """
        Возвращает строковое представление объекта Roll.
        """
        return (f"Ролл: {self.name}, Основной ингредиент: {self.main_ingredient}, "
                f"Вес риса: {self.rice_weight} г, Вес водорослей: {self.seaweed_weight} г, "
                f"Начинка: {', '.join(self.__fillings)}")

    def save_order_to_json(self, filename,data):
        """
        Сохраняет данные в JSON-файл.

        filename: Путь к файлу.
        data: Данные для сохранения.
        """
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def get_data_from_json(self, level, filename):
        """
        Читает данные из JSON-файла.

        level: Уровень доступа.
        filename: Путь к файлу.

        Данные из файла, если доступ разрешен.
        Сообщение об ошибке, если доступ запрещен.
        """
        if level < 1:
            return "Доступ запрещен."

        try:
            with open(filename, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return "Файл не найден."