import flet as ft


def title_template(title) -> ft.Control:
    return ft.Container(
        padding=ft.Padding.symmetric(vertical=4, horizontal=12),
        border=ft.Border.all(1, ft.Colors.GREEN_ACCENT_400),
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.BorderRadius.all(12),
        content=ft.Row(
            controls=[
                ft.Text(
                    title,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN_ACCENT_400,
                    size=24,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


@ft.control
class rapidTemplate(ft.Column):
    _PRIMLARY_COLOR = ft.Colors.GREEN_ACCENT_400
    _DISABLED_COLOR = ft.Colors.GREY_600

    def init(self):
        # --- Titre centré ---
        self.title = title_template("RapidTest")
        self.controls = [
            self.title,
        ]
