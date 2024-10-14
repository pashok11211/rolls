from roll.roll import Roll
from views.rollview import RollView, AdminView
from controller.rollcontroll import RollController
from datetime import datetime

def main():
    # Создание ролла
    my_roll = Roll(name="Калифорнийский ролл", main_ingredient="Краб", rice_weight=150, seaweed_weight=10)
    my_roll.add_filling("Авокадо")
    my_roll.add_filling("Огурец")

    # Создание контроллера для работы с роллом
    roll_controller = RollController(my_roll)

    # Создание представлений
    roll_view = RollView()
    admin_view = AdminView()

    # Отображаем информацию о ролле
    roll_view.show_roll(my_roll)
    admin_view.show_admin_view(my_roll)

    # Сохранение заказа в JSON
    order_data = {
        "order_name": "Мой заказ",  # Имя заказа
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Привязка ко времени
        "name": my_roll.get_name(),
        "main_ingredient": my_roll.get_main_ingredient(),
        "rice_weight": my_roll.get_rice_weight(),
        "seaweed_weight": my_roll.get_seaweed_weight(),
        "fillings": my_roll.get_fillings()
    }
    filename = "order.json"

    # Сохранение данных в JSON
    roll_view.save_order_to_json(filename, order_data)

    # Чтение данных из JSON с разрешенным доступом
    level = 1  # Уровень доступа
    data = roll_view.get_data_from_json(level, filename)

    if isinstance(data, dict):
        roll_view.show_info(data)  # Показ информации о заказе
    else:
        print(data)  # Вывод сообщения о недостатке прав доступа

    # Чтение данных из JSON с недостатком доступа
    denied_level = 0  # Уровень доступа, при котором доступ запрещен
    access_denied_message = roll_view.get_data_from_json(denied_level, filename)
    print(access_denied_message)  # Вывод сообщения о запрете доступа

if __name__ == "__main__":  # Исправленная проверка
    main()

