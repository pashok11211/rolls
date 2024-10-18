from controllers.controller import Controller
from model.model import Model
from View import View

class Userinterface:
    """
    Класс для управления пользовательским интерфейсом.
    """
    def __init__(self):
        """
        Инициализирует объекты модели, представления и контроллера.
        """
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model, self.view)

    def start(self):
        """
        Запускает приложение, выполняя основные действия.
        """
        # Вызывает методы контроллера для взаимодействия с моделью и представлением
        self.controller.show_info()
        self.controller.show_dish_image("Пицца")
        self.controller.update_data({"info": "Новая информация"})
        self.controller.update_data("неверный тип данных")