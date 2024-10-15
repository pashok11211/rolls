class RollController:
    def __init__(self, roll, roll_model):  # Inject RollModel
        self.roll = roll
        self.roll_model = roll_model  # Instance of RollModel

    def restaurant_view(self):
        return f"Ролл: {self.roll.get_name()}, Основной ингредиент: {self.roll.get_main_ingredient()}"

    def website_view(self):
        return (f"Ролл: {self.roll.get_name()}, Основной ингредиент: {self.roll.get_main_ingredient()}, "
                f"Начинка: {', '.join(self.roll.get_fillings())}")

    def update_roll(self, rice_weight=None, seaweed_weight=None, fillings=None):
        if rice_weight is not None:
            self.roll.set_rice_weight(rice_weight)
        if seaweed_weight is not None:
            self.roll.set_seaweed_weight(seaweed_weight)
        if fillings is not None:
            self.roll.update_recipe(fillings=fillings)

    def check_access(self, access_level):
        return access_level == "admin"

    def save_roll(self, filename):
        roll_data = {
            "name": self.roll.get_name(),
            "main_ingredient": self.roll.get_main_ingredient(),
            "rice_weight": self.roll.get_rice_weight(),
            "seaweed_weight": self.roll.get_seaweed_weight(),
            "fillings": self.roll.get_fillings()
        }
        self.roll_model.save_roll_data(filename, roll_data)

    def load_roll(self, filename, access_level):
        if self.check_access(access_level):
            roll_data = self.roll_model.load_roll_data(filename)
            if roll_data:
                self.roll.set_name(roll_data["name"])
                self.roll.set_main_ingredient(roll_data["main_ingredient"])
                return "Данные ролла успешно загружены."
            else:
                return "Файл не найден или данные ролла не обнаружены."
        else:
            return "Недостаточно прав доступа для чтения данных."