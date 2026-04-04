import flet as ft

from .templates import title_template

@ft.control
class rapidTest(ft.Column):
    # _PRIMLARY_COLOR = ft.Colors.GREEN_ACCENT_400
    # _DISABLED_COLOR = ft.Colors.GREY_600

    def init(self):
        self.title = title_template('RapidTest')

        self.controls = [
            self.title,
        ]


def dev(page: ft.Page):
    page.title = "Dev (Rapid Test)"

    page.bgcolor = "#333333"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    test = rapidTest()
    # add application's root control to the page
    page.add(test)


if __name__ == "__main__":

    ft.run(dev)
