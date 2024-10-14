class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_info(self):  # показ информации
        data = self.model.get_data()
        self.view.show_info(data)

    def show_dish_image(self, dish_name):  # показ фото блюда
        image_path = self.model.get_dish_image(dish_name)
        self.view.show_dish_image(image_path)

    def update_data(self, new_data):  # обновление данных
        success = self.model.update_data(new_data)
        if success:
            print("Данные успешно обновлены.")
        else:
            print("Ошибка обновления данных.")

    def save_order_to_json(self, order_name):  # сохранение ордера в json

        self.model.create_order_json(order_name)
        self.view.confirm_order_saved(order_name)

    def get_data_from_json(self, filename, user_access_level):  # получение данных от json

        if user_access_level >= 1:  # проверка уровня доступа
            order_data = self.model.read_order_json(filename)
            self.view.display_order_data(order_data)
        else:
            self.view.access_denied()
