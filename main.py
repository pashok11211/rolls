from model.roll import Roll
from views.rollview import RollView, AdminView
from datetime import datetime
import json
import os

def main():
    # Создание ролла
    my_roll = Roll(name="Калифорнийский ролл", main_ingredient="Краб", rice_weight=150, seaweed_weight=10)
    my_roll.add_filling("Авокадо")
    my_roll.add_filling("Огурец")

    roll_view = RollView()
    admin_view = AdminView()

    roll_view.show_roll(my_roll)
    admin_view.show_admin_view(my_roll)

    order = "orders"
    os.makedirs(order, exist_ok=True)

    order_name = "Заказ_клиента_1"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{order}/{order_name}_{timestamp}.json"

    order_data = {
        "name": my_roll.get_name(),
        "main_ingredient": my_roll.get_main_ingredient(),
        "rice_weight": my_roll.get_rice_weight(),
        "seaweed_weight": my_roll.get_seaweed_weight(),
        "fillings": my_roll.get_fillings(),
        "timestamp": timestamp}

    roll_view.save_order_to_json(filename, order_data)

    # логика проверки уровня доступа и чтения данных из JSON
    def get_data_from_json(level, filename):
        if level > 0:
            try:
                with open(filename, 'r') as file:
                    return json.load(file)
            except FileNotFoundError:
                  return "Файл не найден"
        else:
            return "У вас недостаточно прав доступа для чтения файла"

    # Чтение данных из JSON с разрешенным доступом
    level = 1  # Уровень доступа
    data = get_data_from_json(level, filename)

    if isinstance(data, dict):
        roll_view.show_info(data)
    else:
        print(data)  # Вывод сообщения о недостатке прав доступа

    # Чтение данных из json с недостатком доступа
    denied_level = 0
    access_denied_message = get_data_from_json(denied_level, filename)
    print(access_denied_message)


if __name__ == "__main__":
    main()
