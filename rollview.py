class RollView:
    def show_roll(self, roll):

        print("Информация о ролле:")
        print(f"Название: {roll.get_name()}")
        print(f"Основной ингредиент: {roll.get_main_ingredient()}")
        print(f"Вес риса: {roll.get_rice_weight()} г")
        print(f"Вес водорослей: {roll.get_seaweed_weight()} г")
        print(f"Начинки: {', '.join(roll.get_fillings())}")

    def show_rolls_list(self, rolls):

        print("Список роллов:")
        for roll in rolls:
            print(f"- {roll.get_name()}: {roll.get_main_ingredient()}")

class AdminView:
        def show_edit_options(self, roll):

            print("Редактирование ролла:")
            print(f"Текущее название: {roll.get_name()}")
            new_name = input("Введите новое название : ")
            if new_name:
                roll.set_name(new_name)

            new_main_ingredient = input("Введите новый основной ингридиент : ")
            if new_main_ingredient:
                roll.set_main_ingredient(new_main_ingredient)

            new_rice_weight = input("Введите новый вес риса (г) : ")
            if new_rice_weight:
                roll.set_rice_weight(float(new_rice_weight))

            new_seaweed_weight = input("Введите новый вес водорослей (г) : ")
            if new_seaweed_weight:
                roll.set_seaweed_weight(float(new_seaweed_weight))

            print("Текущие начинки:", ', '.join(roll.get_fillings()))
            fillings = input("Введите новые начинки через запятую : ")
            if fillings:
                roll.update_recipe(fillings=[filling.strip() for filling in fillings.split(',')])

            print("Ролл был обновлен.")

        def show_admin_view(self, roll):
            self.show_edit_options(roll)

