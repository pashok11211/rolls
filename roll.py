class Roll:
    def __init__(self, name, main_ingredient, rice_weight, seaweed_weight):
        self.name = name
        self.main_ingredient = main_ingredient
        self.rice_weight = rice_weight
        self.seaweed_weight = seaweed_weight
        self.__fillings = []  # Используем частный атрибут

    def get_name(self):
        return self.name

    def get_main_ingredient(self):
        return self.main_ingredient

    def get_rice_weight(self):
        return self.rice_weight

    def get_seaweed_weight(self):
        return self.seaweed_weight

    def get_fillings(self):
        return self.__fillings

    def set_name(self, name: str):
        self.name = name

    def set_main_ingredient(self, main_ingredient: str):
        self.main_ingredient = main_ingredient

    def set_rice_weight(self, rice_weight: float):
        self.rice_weight = rice_weight

    def set_seaweed_weight(self, seaweed_weight: float):
        self.seaweed_weight = seaweed_weight

    def add_filling(self, filling: str):
        self.__fillings.append(filling)

    def remove_filling(self, filling: str):
        if filling in self.__fillings:
            self.__fillings.remove(filling)

    def update_recipe(self, rice_weight=None, seaweed_weight=None, fillings=None):
        if rice_weight is not None:
            self.rice_weight = rice_weight
        if seaweed_weight is not None:
            self.seaweed_weight = seaweed_weight
        if fillings is not None:
            self.__fillings = fillings

    def create_custom_roll(self, name: str, main_ingredient: str, rice_weight: float, seaweed_weight: float, fillings):
        return Roll(name, main_ingredient, rice_weight, seaweed_weight)

    def __str__(self):
        return (f"Ролл: {self.name}, Основной ингредиент: {self.main_ingredient}, "
                f"Вес риса: {self.rice_weight} г, Вес водорослей: {self.seaweed_weight} г, "
                f"Начинка: {', '.join(self.__fillings)}")