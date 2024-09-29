from roll import Roll
from rollcontroll import RollController
from rollview import RollView, AdminView

if __name__ == "__main__":
    my_roll = Roll(name="Калифорнийский ролл", main_ingredient="Краб", rice_weight=150, seaweed_weight=10)
    my_roll.add_filling("Авокадо")
    my_roll.add_filling("Огурец")

    roll_controller = RollController(my_roll)

    roll_view = RollView()
    roll_view.show_roll(my_roll)

    admin_view = AdminView()
    admin_view.show_admin_view(my_roll)

    roll_view.show_roll(my_roll)
