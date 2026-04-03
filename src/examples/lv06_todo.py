from dataclasses import field

import flet as ft


@ft.control
class todo(ft.Container):
    def init(self):
        self._values: dict[str, int] = {"x": 0}

        self.bgcolor = "#333333"
        self.width = 350
        self.height = 200
        self.border_radius = ft.BorderRadius.all(12)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value="Todo List", color=ft.Colors.WHITE, size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )


def todo_list(page: ft.Page):
    page.title = "Todo List"

    todo_instance = todo()
    page.add(todo_instance)


if __name__ == "__main__":

    ft.run(todo_list)
