from roll import Roll
class RollController:
    def __init__(self, roll):
        self.roll = roll

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
