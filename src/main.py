import flet as ft
import datetime
from tools.screen_utils import gc7_rules as gc7


def main(page: ft.Page):
    # gc7(page, 'LIGHT')
    gc7(page)

    # # from examples.lv04_calc_ui import calc as calc
    # from examples.lv05_calc_ui_reusable import calc as calc
    # calc(page)

    # from devs.lv01_icons_list import icons_list as icons_list
    # icons_list(page) # 3 versions dispos

    # # ❌ Finir game NbreX
    # from devs.lv02_nbre_x import game as game
    # game(page)

    # from examples.lv06_todo import todo_list as todo
    # todo(page)

    if not page.controls:
        page.add(
            ft.Text(
                "No content.",
                size=30,
                color=ft.Colors.RED_ACCENT_400,
            )
        )


if __name__ == "__main__":
    print(datetime.datetime.now().strftime("%H:%M:%S"), "> ")
    ft.run(main)
