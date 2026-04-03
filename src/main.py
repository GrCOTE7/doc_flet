import flet as ft
import datetime
from tools.screen_utils import gc7_rules as gc7


def main(page: ft.Page):
    # gc7(page, 'LIGHT')
    gc7(page)

    # # from examples.lv04_calc_ui import calc as calc
    # from examples.lv05_calc_ui_reusable import calc as calc
    # calc(page)

    # # ❌ Finir game NbreX
    # from devs.lv01_nbre_x import game as game
    # game(page)
    
    from examples.lv06_todo import todo_list as todo
    todo(page)


if __name__ == "__main__":
    print(datetime.datetime.now().strftime("%H:%M:%S"), "> ")
    ft.run(main)
