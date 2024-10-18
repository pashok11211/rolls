class AdminView:
    """
    Класс для представления администраторского вида ролла.
    """
    def show_admin_view(self, roll):
        """
        Выводит подробную информацию о ролле в администраторском виде.


            roll: Объект класса Roll, представляющий ролл.
        """
        print("Ⓑ* Администраторский вид Ⓑ*")
        print(f"Название: {roll.name}")
        print(f"Основной ингредиент: {roll.main_ingredient}")
        print(f"Вес риса: {roll.rice_weight} грамм")
        print(f"Вес водорослей: {roll.seaweed_weight} грамм")
        print(f"Ингредиенты: {', '.join(roll.fillings)}")
        print(f"Изображение доступно по пути: static/images/roll.jpg")