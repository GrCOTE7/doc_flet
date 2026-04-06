import flet as ft
from dataclasses import dataclass


@dataclass
class Message:
    user: str
    text: str
    msg_type: str


def main(page: ft.Page):
    page.bgcolor = "#333333"
    title = ft.Text("Chat 22")

    chat = ft.Column()
    new_message = ft.TextField()

    def on_message(message: Message):
        if message.msg_type == "chat_message":
            chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        elif message.msg_type == "login_message":
            chat.controls.append(
                ft.Text(message.text, italic=True, color=ft.Colors.WHITE_54, size=12)
            )
        page.update()

    page.pubsub.subscribe(on_message)  # Broadcasting

    def send_click(e):
        page.pubsub.send_all(
            Message(
                user=page.session.store.get("user_name"),
                text=new_message.value,
                msg_type="chat_message",
            )
        )
        print(new_message.value)
        new_message.value = ""

    user_name = ft.TextField(label="Enter your name", value="Lionel")

    def join_click(e):

        if not user_name.value:
            user_name.error = "Name can't be blank!"
        else:
            page.session.store.set("user_name", user_name.value)
            page.pop_dialog()
            page.pubsub.send_all(
                Message(
                    user=user_name.value,
                    text=f"{user_name.value} has joined the chat.",
                    msg_type="login_message",
                )
            )

        print(f"{user_name.value = }")

    page.show_dialog(
        ft.AlertDialog(
            open=True,
            modal=True,
            title="Welcome!",
            content=ft.Column([user_name], tight=True),
            actions=[
                ft.Button(
                    content="Join chat",
                    on_click=join_click,
                    style=ft.ButtonStyle(
                        mouse_cursor=ft.MouseCursor.CLICK,
                        bgcolor=ft.Colors.BLACK_54,
                        # side=ft.BorderSide(1, ft.Colors.RED),
                        shape=ft.RoundedRectangleBorder(radius=7),
                    ),
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
    )

    page.add(title, chat, ft.Row([new_message, ft.Button("Send", on_click=send_click)]))


if __name__ == "__main__":
    ft.run(main)
