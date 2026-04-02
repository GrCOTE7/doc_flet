import flet as ft
import datetime
from tools.screen_utils import gc7_rules as gc7

# from examples.lv04_calc_ui import calc as calc
from examples.lv05_calc_ui_reusable import calc as calc


def main(page: ft.Page):
    # gc7(page, 'LIGHT')
    gc7(page)

    calc(page)


if __name__ == "__main__":
    print(datetime.datetime.now().strftime("%H:%M:%S"), "> ")
    ft.run(main)
