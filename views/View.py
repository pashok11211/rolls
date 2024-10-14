class View:
    def show_info(self, data):  # информация

        print("Информация о блюде:", data)

    def show_dish_image(self, image_path):  # показывает фото

        print(f"Изображение расположено по пути: {image_path}")

    def confirm_order_saved(self, order_name):  # сохранение ордера

        print(f"Заказ '{order_name}' успешно сохранён.")

    def display_order_data(self, order_data):  # данные

        print("Данные о заказе:", order_data)

    def access_denied(self):  # проверка прав для показа

        print("У вас нет прав доступа к этой информации.")