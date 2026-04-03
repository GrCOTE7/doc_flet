import flet as ft
from asyncio.windows_events import INFINITE
from ctypes import alignment


@ft.control
class TodoApp(ft.Column):

    _PRIMLARY_COLOR = ft.Colors.GREEN_ACCENT_400
    _DISABLED_COLOR = ft.Colors.GREY_600

    def init(self):
        self._width = INFINITE  # 350

        # --- Titre centré ---
        self.title = ft.Container(
            width=self._width,
            padding=ft.Padding.only(top=10, bottom=10),
            margin=ft.Margin.only(top=25),
            border=ft.Border.all(1, self._PRIMLARY_COLOR),
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(12),
            content=ft.Row(
                controls=[
                    ft.Text(
                        "GC7 Todo List",
                        weight=ft.FontWeight.BOLD,
                        color=self._PRIMLARY_COLOR,
                        size=32,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

        # --- Champ de saisie ---
        self.new_task = ft.TextField(
            text_size=18,
            hint_style=ft.TextStyle(italic=True, color=self._DISABLED_COLOR),
            color=ft.Colors.WHITE,
            hint_text="What needs to be done?",
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(7),
            border_color=self._PRIMLARY_COLOR,
            expand=True,
            mouse_cursor=ft.MouseCursor.CLICK,
            on_change=self.task_changed,
            on_submit=self.add_clicked,
            autofocus=True,
        )

        # --- Bouton ajouter (désactivé par défaut) ---
        self.add_btn = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_color=self._DISABLED_COLOR,
            icon_size=28,
            width=55,
            height=55,
            disabled=True,
            mouse_cursor=ft.MouseCursor.BASIC,
            on_click=self.add_clicked,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLACK,
                side=ft.BorderSide(1, self._DISABLED_COLOR),
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        )

        self.tasks_view = ft.Column(
            controls=[
                ft.Checkbox(label="Exemple: 1e première tâche"),
            ]
        )

        self.controls = [
            self.title,
            ft.Row(
                controls=[
                    self.new_task,
                    self.add_btn,
                ],
            ),
            self.tasks_view,
        ]

        # Afficher les tâches au démarrage
        self.show_tasks()

    # --- Mise à jour du bouton selon le champ ---
    def task_changed(self, e):
        has_text = bool(self.new_task.value)
        self.add_btn.disabled = not has_text
        self.add_btn.mouse_cursor = (
            ft.MouseCursor.CLICK if has_text else ft.MouseCursor.BASIC
        )
        self.add_btn.icon_color = (
            self._PRIMLARY_COLOR if has_text else self._DISABLED_COLOR
        )
        self.add_btn.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLACK,
            side=ft.BorderSide(
                1, self._PRIMLARY_COLOR if has_text else self._DISABLED_COLOR
            ),
            shape=ft.RoundedRectangleBorder(radius=8),
        )
        self.add_btn.update()

        # print("TodoApp tasks_view :", [task.label for task in self.tasks_view.controls])

    # --- Action bouton ---
    async def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.tasks_view.update()
        self.new_task.value = ""
        self.add_btn.disabled = True
        self.add_btn.mouse_cursor = ft.MouseCursor.BASIC
        self.add_btn.icon_color = self._DISABLED_COLOR
        self.add_btn.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLACK,
            side=ft.BorderSide(1, self._DISABLED_COLOR),
            shape=ft.RoundedRectangleBorder(radius=8),
        )
        self.show_tasks()
        await self.new_task.focus()
        self.update()

    def show_tasks(self):
        print(f"\n📋 Tâches ({len(self.tasks_view.controls)}):")
        for i, task in enumerate(self.tasks_view.controls, 1):
            label = getattr(task, "label", "?")
            print(f"  {i}. {label}")


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
