import flet as ft


def bloc_template(text: str, size: int = 14, title=False) -> ft.Control:
    return ft.Container(
        padding=ft.Padding.symmetric(vertical=4, horizontal=12),
        border=ft.Border.all(1, ft.Colors.GREEN_ACCENT_400),
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.BorderRadius.all(7),
        content=ft.Row(
            controls=[
                ft.Text(
                    text,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN_ACCENT_400,
                    size=size + (4 if title else 0),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER if title else ft.MainAxisAlignment.START,
        ),
    )


@ft.control
class rapidTemplate(ft.Column):
    _PRIMLARY_COLOR = ft.Colors.GREEN_ACCENT_400
    _DISABLED_COLOR = ft.Colors.GREY_600
    title_text: str = "RapidTest"
    detail_text: str | None = None

    def init(self):
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 10

        self.controls = [bloc_template(self.title_text, title=True)]

        if self.detail_text:
            self.controls.append(bloc_template(self.detail_text, size=14))
