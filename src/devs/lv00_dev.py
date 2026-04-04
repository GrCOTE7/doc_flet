import flet as ft

from .templates import rapidTemplate


@ft.control
class rapidTest(ft.Column):

    def init(self):
        self.controls = [rapidTemplate(detail_text="Ok21")]


def dev(page: ft.Page):
    page.title = "Dev (Rapid Test)"

    page.bgcolor = "#333333"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    page.add(rapidTest())


if __name__ == "__main__":

    ft.run(dev)
