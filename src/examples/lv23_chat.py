import flet as ft
from dataclasses import dataclass
import asyncio, random, time


@dataclass
class Message:
    user: str
    text: str
    msg_type: str


@ft.control
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.message = message
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(self.message.user)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(self.message.user),
            ),
            ft.Column(
                tight=True,
                spacing=5,
                controls=[
                    ft.Text(self.message.user, weight=ft.FontWeight.BOLD),
                    ft.Text(self.message.text, selectable=True),
                ],
            ),
        ]

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"  # or any default value you prefer

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.RED,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


def main(page: ft.Page):

    page.bgcolor = "#333333"
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    title = ft.Text(
        "Flet Chat 23", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE
    )

    chat = ft.Column()

    new_message = ft.TextField(
        bgcolor="#111111", color=ft.Colors.WHITE, border_color="#777777"
    )
    new_message.expand = True

    # def on_message(message: Message):
    #     if message.msg_type == "chat_message":
    #         # chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
    #         m = ChatMessage(message)
    #     elif message.msg_type == "login_message":
    #         m = ft.Text(message.text, italic=True, color=ft.Colors.WHITE_54, size=14)
    #     chat.controls.append(m)
    #     page.update()

    def on_message(message: Message):
        if message.msg_type == "chat_message":
            chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        elif message.msg_type == "login_message":
            chat.controls.append(
                ft.Text(message.text, italic=True, color=ft.Colors.WHITE_54, size=14)
            )
        page.update()

    page.pubsub.subscribe(on_message)  # Broadcasting

    def send_click(e):
        page.pubsub.send_all(
            Message(
                user=page.session.store.get("user_name"),  # 2ar # type: ignore
                text=new_message.value,
                msg_type="chat_message",
            )
        )
        print(user_name.value, "→", new_message.value)
        new_message.value = ""

    def join_click(e):

        if not user_name.value:
            user_name.error = "Name can't be blank!"
        else:
            msg = f"{user_name.value} has joined the chat."
            page.session.store.set("user_name", user_name.value)
            page.pop_dialog()
            page.pubsub.send_all(
                Message(
                    user=user_name.value,
                    text=msg,
                    msg_type="login_message",
                )
            )
            print(msg)

    user_name = ft.TextField(label="Enter your name", value="Lionel")

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
            bgcolor="#252525",
            shape=ft.RoundedRectangleBorder(radius=12),
        )
    )

    # Simule le clic sur "Join chat" avec le champ deja rempli.
    join_click(None)

    async def simuMsgs():

        users = ["Alice", "Bob", "Charlie", "Diana"]
        messages = [
            "Hello everyone!",
            "How's it going?",
            "Anyone up for a game?",
            "What's the plan for today?",
            "Did you see the news?",
        ]

        random.shuffle(users)
        selected_messages = random.sample(messages, k=len(users))

        for user, text in zip(users, selected_messages):
            await asyncio.sleep(random.randint(2, 5))
            page.pubsub.send_all(
                Message(
                    user=user,
                    text=text,
                    msg_type="chat_message",
                )
            )
            print(user, "→", text)

        if not page.session.store.get("user_name"):
            join_click(None)

    page.run_task(simuMsgs)

    page.add(
        title,
        chat,
        ft.Container(
            margin=ft.margin.only(top=5, bottom=5),
            padding=ft.padding.only(top=6),
            content=ft.Row(
                [
                    new_message,
                    ft.Button(
                        content="Send",
                        height=46,
                        on_click=send_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=4),
                        ),
                    ),
                ]
            ),
        ),
    )

    # # Add everything to the page
    # page.add(
    #     ft.Container(
    #         content=chat,
    #         border=ft.Border.all(1, ft.Colors.OUTLINE),
    #         border_radius=5,
    #         padding=10,
    #         expand=True,
    #     ),
    #     ft.Row(
    #         controls=[
    #             new_message,
    #             ft.IconButton(
    #                 icon=ft.Icons.SEND_ROUNDED,
    #                 tooltip="Send message",
    #                 on_click=send_message_click,
    #             ),
    #         ]
    #     ),
    # )

    # time.sleep(15)
    # print(hash("Lionel") % 13)  # → BLUE ❌ Vérif


if __name__ == "__main__":
    ft.run(main)
