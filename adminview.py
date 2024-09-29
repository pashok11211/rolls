class AdminRollView:
    def show_edit_options(self, roll):

        print("Редактирование ролла:")
        print(f"Текущее название: {roll.get_name()}")
        new_name = input("Введите новое название (или нажмите Enter для сохранения): ")
        if new_name:
            roll.set_name(new_name)

        new_main_ingredient = input("Введите новый основной ingredient (или нажмите Enter для сохранения): ")
        if new_main_ingredient:
            roll.set_main_ingredient(new_main_ingredient)

        new_rice_weight = input("Введите новый вес риса (г) (или нажмите Enter для сохранения): ")
        if new_rice_weight:
            roll.set_rice_weight(float(new_rice_weight))

        new_seaweed_weight = input("Введите новый вес водорослей (г) (или нажмите Enter для сохранения): ")
        if new_seaweed_weight:
            roll.set_seaweed_weight(float(new_seaweed_weight))

        print("Текущие начинки:", ', '.join(roll.get_fillings()))
        fillings = input("Введите новые начинки через запятую (или нажмите Enter для сохранения): ")
        if fillings:
            roll.update_recipe(fillings=[filling.strip() for filling in fillings.split(',')])

        print("Ролл был обновлен.")

    def show_admin_view(self, roll):
        self.show_edit_options(roll)