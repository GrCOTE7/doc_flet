import flet as ft
from dataclasses import dataclass


@dataclass
class Message:
    user: str
    text: str


def main(page: ft.Page):
    page.bgcolor = "#333333"

    chat = ft.Column()
    new_message = ft.TextField()

    def on_message(message: Message):
        chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        page.update()

    page.pubsub.subscribe(on_message)  # Broadcasting

    def send_click(e):
        page.pubsub.send_all(
            Message(user=str(page.session.index), text=new_message.value)
        )
        print(new_message.value)
        new_message.value = ""

    page.add(
        ft.Text(value="Chat Ready.", size=18),
        chat,
        ft.Row(controls=[new_message, ft.Button("Send", on_click=send_click)]),
    )


if __name__ == "__main__":
    ft.run(main)
