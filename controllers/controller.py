class Controller:
    """
    Класс-контроллер, отвечающий за взаимодействие между моделью и представлением.
    """
    def __init__(self, model, view):
        """
        Инициализирует объект Controller.

        model: Объект класса Model, представляющий модель данных.
        view: Объект класса View, представляющий пользовательский интерфейс.
        """
        self.model = model
        self.view = view

    def show_info(self):
        """
        Отображает информацию о блюде.
        """
        data = self.model.get_data()
        self.view.show_info(data)

    def show_dish_image(self, dish_name):
        """
        Отображает изображение блюда.

        dish_name: Название блюда.
        """
        image_path = self.model.get_dish_image(dish_name)
        self.view.show_dish_image(image_path)

    def update_data(self, new_data):
        """
        Обновляет данные в модели и выводит сообщение об успехе или ошибке.

        new_data: Новые данные для обновления.
        """
        success = self.model.update_data(new_data)
        if success:
            print("Данные успешно обновлены.")
        else:
            print("Ошибка обновления данных.")

    def save_order_to_json(self, order_name):
        """
        Сохраняет информацию о заказе в JSON-файл.

        order_name: Название заказа.
        """
        self.model.create_order_json(order_name)
        self.view.confirm_order_saved(order_name)

    def get_data_from_json(self, filename, user_access_level):
        """
        Читает информацию о заказе из JSON-файла с проверкой уровня доступа.

        filename: Путь к JSON-файлу.
        user_access_level: Уровень доступа пользователя.
        """
        if user_access_level >= 1:
            order_data = self.model.read_order_json(filename)
            self.view.display_order_data(order_data)
        else:
            self.view.access_denied()