from re import A

import flet as ft
import datetime
import asyncio
from tools.screen_utils import gc7_rules as gc7


async def main(page: ft.Page):
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

    # Test fonctions asynchones
    if 1:
        from examples.lv07_todo import todo_list as todo7
        from examples.lv06_todo_simple import todo_list as todo6

        async def fini():
            print(
                datetime.datetime.now().strftime("%H:%M:%S"), "> Todos 6 & 7 Ready.\n"
            )

        async def async_fctns():
            print(datetime.datetime.now().strftime("%H:%M:%S"), "> async_fctns")
            # await asyncio.gather(todo6(page), todo7(page)) # ❌ to ar
            await asyncio.gather(todo6(page))
            await fini()

        await async_fctns()

    from examples.lv08_todo import todo_list as todo

    todo(page)

    # from devs.lv02_blocs import blocs as dev
    # dev(page)

    # from devs.lv00_dev import dev as dev
    # dev(page)

    if not page.controls:
        page.add(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                margin=ft.Margin.only(top=25),
                controls=[
                    ft.Text(
                        "No content.",
                        size=30,
                        color=ft.Colors.RED_ACCENT_400,
                    )
                ],
            )
        )


if __name__ == "__main__":
    print(datetime.datetime.now().strftime("%H:%M:%S"), "> ")
    ft.run(main)
