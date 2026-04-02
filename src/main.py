import flet as ft
from tools.screen_utils import gc7_rules as gc7
from examples.lv_02_btn import main as btn2

name: str = "Ready"


def main(page: ft.Page):
    gc7(page, name)

    btn2(page, name)


ft.run(main)
