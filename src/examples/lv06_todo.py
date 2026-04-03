# from dataclasses import field

from asyncio.windows_events import INFINITE
from ctypes import alignment

from fastapi import background
import flet as ft


def todo_list(page: ft.Page):
    # _WIDTH = 350
    _WIDTH = INFINITE
    page.title = "Todo List"
    page.bgcolor = "#333333"

    # --- Titre centré ---
    title = ft.Container(
        width=_WIDTH,
        padding=ft.Padding.only(top=10, bottom=10),
        margin=ft.Margin.only(top=25),
        border=ft.Border.all(1, ft.Colors.GREEN_ACCENT_400),
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.BorderRadius.all(12),
        content=ft.Row(
            controls=[
                ft.Text(
                    "GC7 Todo List",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN_ACCENT_400,
                    size=32,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )
    page.add(title)

    # --- Action bouton ---
    def add_clicked(e):
        tasks_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        view.update()

    # --- Champ de saisie ---
    new_task = ft.TextField(
        text_size=18,
        text_style=ft.TextStyle(italic=True),
        hint_text="What needs to be done?",
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.BorderRadius.all(7),
        border_color=ft.Colors.GREEN_ACCENT_400,
        expand=True,  # ❌  comprendre expand
    )

    tasks_view = ft.Column()

    view = ft.Column(
        width=_WIDTH,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=add_clicked,
                        bgcolor=ft.Colors.GREEN_ACCENT_400,
                        scale=0.9,
                    ),
                ],
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


if __name__ == "__main__":

    ft.run(todo_list)
