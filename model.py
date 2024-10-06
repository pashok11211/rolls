class Model:
    def __init__(self):
        self.data = {"info": "Информация о блюде"}

    def update_data(self, new_data):
        if isinstance(new_data, dict):
            self.data.update(new_data)
            return True
        return False

    def get_data(self):
        return self.data

    def get_dish_image(self, dish_name):
        images = {
            "Калифорнийский ролл": "static/images/roll.jpg",
            "Пицца": "static/images/pizza.jpg"
        }
        return images.get(dish_name, "Изображение не найдено")