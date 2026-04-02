import flet as ft
import tools.screen_utils as screen_utils
import datetime

name = "Ready"


def main(page: ft.Page):

    screen_utils.configure_window(page)
    page.theme_mode = ft.ThemeMode.DARK  # Comment to light
    page.title = "Flet Doc officielle | " + name

    page.add(ft.Text("Ready.", size=28))

ft.run(main)
