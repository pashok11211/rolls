class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_info(self):
        data = self.model.get_data()
        self.view.show_info(data)

    def show_dish_image(self, dish_name):
        image_path = self.model.get_dish_image(dish_name)
        self.view.show_dish_image(image_path)

    def update_data(self, new_data):
        success = self.model.update_data(new_data)
        if success:
            print("Данные успешно обновлены.")
        else:
            print("Ошибка обновления данных.")