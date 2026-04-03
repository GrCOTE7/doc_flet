# from dataclasses import field

from ctypes import alignment

import flet as ft

# @ft.control
# class todo(ft.Container):

# def init(self):
#     self._values: dict[str, int] = {"x": 0}

#     self.bgcolor = "#333333"
#     self.width = 350
#     self.height = 200
#     self.border_radius = ft.BorderRadius.all(12)
#     self.padding = 20
#     self.content = ft.Column(
#         controls=[
#             ft.Row(
#                 controls=[
#                     ft.Text(value="Todo List", color=ft.Colors.WHITE, size=20),
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#             )
#         ],
#         alignment=ft.MainAxisAlignment.CENTER,
#         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#     )

# pass


def todo_list(page: ft.Page):
    page.title = "Todo List"
    page.bgcolor = ft.Colors.BLACK

    # print(dir(ft.Icons))
    icons_ids = dir(ft.Icons)

    print(len(icons_ids))
    # print(*icons_ids[:3], sep=" ")
    print (ft.Icons.ABC)
    # print (ft.Icons.ABC_ROUNDED)
    page.add(ft.IconButton(ft.Icons.ABC, on_click=lambda e: print("ABC clicked")))

    # --- Titre centré ---
    title = ft.Row(
        controls=[ft.Text("Todo List", color=ft.Colors.WHITE, size=32)],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    page.add(title)

    # --- Champ de saisie ---
    new_task = ft.TextField(hint_text="What needs to be done?", expand=True)

    # --- Action bouton ---
    def add_clicked(e):
        if new_task.value.strip() != "":
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            page.update()

    add_button = ft.FloatingActionButton(icon=ft.Icons.ADD_CIRCLE, on_click=add_clicked)

    # --- Ligne d'ajout ---
    page.add(
        ft.Row(controls=[new_task, add_button], alignment=ft.MainAxisAlignment.CENTER)
    )

    page.update()

    # page.add(ft.Text(value="New Todo Item", color=ft.Colors.WHITE, size=20))

    # def add_clicked(e):
    #     page.add(ft.Checkbox(label=new_task.value))
    #     new_task.value = ""

    # # todo_instance = todo()
    # # page.add(todo_instance)
    # new_task = ft.TextField(hint_text="Whats needs to be done?")
    # page.update()

    # page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))


if __name__ == "__main__":

    ft.run(todo_list)
