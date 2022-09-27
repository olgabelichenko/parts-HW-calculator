from unittest import result
from unittest.loader import VALID_MODULE_NAME

import count
import ui

def button_click():
    value_a = ui.get_value1()
    value_b = ui.get_value2()
    action = ui.get_action()
    count.init(value_a, value_b)
    if action == 1:
        result = count.sum()
        ui.ui_data(result)
    elif action == 2:
        result = count.sub()
        ui.ui_data(result)
    elif action == 3:
        result = count.mult()
        ui.ui_data(result)
    elif action == 4:
        result = count. seg()
        ui.ui_data(result)
    else: 
        print(f'Ошибка, попробуйте еще разок. Выбирая действие, введите целое число от 1 до 4')
    exit() 
    
