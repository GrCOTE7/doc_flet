import flet as ft
from asyncio.windows_events import INFINITE
from ctypes import alignment


@ft.control
class TodoApp(ft.Column):

    def init(self):

        self._width = INFINITE  # 350

        # --- Titre centré ---
        self.title = ft.Container(
            width=self._width,
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

        # --- Champ de saisie ---
        self.new_task = ft.TextField(
            text_size=20,
            text_style=ft.TextStyle(italic=True),
            hint_text="What needs to be done?",
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(7),
            border_color=ft.Colors.GREEN_ACCENT_400,
            expand=True,
            mouse_cursor=ft.MouseCursor.CLICK,
        )

        self.tasks_view = ft.Column()

        self.controls = [
            self.title,
            ft.Row(
                controls=[
                    self.new_task,
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        icon_color=ft.Colors.GREEN_ACCENT_400,
                        icon_size=28,
                        width=55,
                        height=55,
                        on_click=self.add_clicked,
                        mouse_cursor=ft.MouseCursor.CLICK,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLACK,
                            side=ft.BorderSide(1, ft.Colors.GREEN_ACCENT_400),
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                ],
            ),
            self.tasks_view,
        ]

    # --- Action bouton ---
    def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()


def todo_list(page: ft.Page):
    page.title = "To-Do App"

    page.bgcolor = "#333333"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    todo = TodoApp()
    # add application's root control to the page
    page.add(todo)

    # # create application instance
    # app1 = TodoApp()
    # app2 = TodoApp()
    # # add application's root control to the page
    # page.add(app1, app2)


if __name__ == "__main__":

    ft.run(todo_list)
