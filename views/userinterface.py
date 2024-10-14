from controller import Controller
from model.model import Model
from View import View

class Userinterface:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model, self.view)

    def start(self):  # старт
        self.controller.show_info()
        self.controller.show_dish_image("Пицца")
        self.controller.update_data({"info": "Новая информация"})
        self.controller.update_data("неверный тип данных")