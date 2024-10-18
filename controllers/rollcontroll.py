class RollController:
    """
    Класс-контроллер для управления объектом Roll.
    """
    def __init__(self, roll, roll_model):
        """
        Инициализирует объект RollController.

        roll: Объект класса Roll.
        roll_model: Объект класса RollModel, используемый для сохранения и загрузки данных.
        """
        self.roll = roll
        self.roll_model = roll_model

    def restaurant_view(self):
        """
        Возвращает представление данных о ролле для ресторана.

        Строка с информацией о ролле.
        """
        return f"Ролл: {self.roll.get_name()}, Основной ингредиент: {self.roll.get_main_ingredient()}"

    def website_view(self):
        """
        Возвращает представление данных о ролле для сайта.

        Строка с информацией о ролле.
        """
        return (f"Ролл: {self.roll.get_name()}, Основной ингредиент: {self.roll.get_main_ingredient()}, "
                f"Начинка: {', '.join(self.roll.get_fillings())}")

    def update_roll(self, rice_weight=None, seaweed_weight=None, fillings=None):
        """
        Обновляет данные о ролле.

        rice_weight: Новый вес риса. Defaults to None.
        seaweed_weight: Новый вес водорослей. Defaults to None.
        fillings: Новый список начинок. Defaults to None.
        """
        if rice_weight is not None:
            self.roll.set_rice_weight(rice_weight)
        if seaweed_weight is not None:
            self.roll.set_seaweed_weight(seaweed_weight)
        if fillings is not None:
            self.roll.update_recipe(fillings=fillings)

    def check_access(self, access_level):
        """
        Проверяет уровень доступа.

        access_level: Уровень доступа.

        True, если доступ разрешен, False - в противном случае.
        """
        return access_level == "admin"

    def save_roll(self, filename):
        """
        Сохраняет данные о ролле в файл.

        filename: Имя файла для сохранения.
        """
        roll_data = {
            "name": self.roll.get_name(),
            "main_ingredient": self.roll.get_main_ingredient(),
            "rice_weight": self.roll.get_rice_weight(),
            "seaweed_weight": self.roll.get_seaweed_weight(),
            "fillings": self.roll.get_fillings()
        }
        self.roll_model.save_roll_data(filename, roll_data)

    def load_roll(self, filename, access_level):
        """
        Загружает данные о ролле из файла.

        filename: Имя файла для загрузки.
        access_level: Уровень доступа.

        Сообщение о результате загрузки.
        """
        if self.check_access(access_level):
            roll_data = self.roll_model.load_roll_data(filename)
            if roll_data:
                self.roll.set_name(roll_data["name"])
                self.roll.set_main_ingredient(roll_data["main_ingredient"])
                self.roll.update_recipe(fillings=roll_data["fillings"])
                self.roll.set_rice_weight(roll_data["rice_weight"])
                self.roll.set_seaweed_weight(roll_data["seaweed_weight"])
                return "Данные ролла успешно загружены."
            else:
                return "Файл не найден или данные ролла не обнаружены."
        else:
            return "Недостаточно прав доступа для чтения данных."