# pip install flet[all]
import flet as ft
from datetime import datetime


def main(page: ft.Page):
    text_hello = ft.Text("Hello world")

    name_input = ft.TextField(label="Введи имя")

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            current_time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
            text_hello.value = f"{current_time} - Привет, {name}!"
            text_hello.color=ft.Colors.GREEN
        else:
            text_hello.value = "Введите корректное имя"
            text_hello.color=ft.Colors.RED

        page.update()

    elevated_button = ft.ElevatedButton(
        "SEND",
        icon=ft.Icons.SEND,
        on_click=on_button_click
    )
    name_input.on_submit=on_button_click
    page.add(text_hello, name_input, elevated_button)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)

