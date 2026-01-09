# pip install flet[all]
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text("Hello world")
    name_input = ft.TextField(label="Введите имя", expand=True)

    #
    greeting_history = []
    greeting_text = ft.Text("История приветствий:")

    
    def on_button_click(tet):
        name = name_input.value.strip()
        if name:
            current_time = datetime.now()
            text_hello.value = f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} - Hello {name}"
            text_hello.color = ft.Colors.GREEN

            greeting_history.append({"name": name, "time": current_time})
            update_history(greeting_history)
        else:
            text_hello.value = "Введите корректное имя"
            text_hello.color = ft.Colors.RED

        name_input.value = ""
        page.update()

    
    def clear_history(tet):
        greeting_history.clear()
        greeting_text.value = "История приветствий:"
        page.update()

    def update_history(history):
        if not history:
            greeting_text.value = "История приветствий:"
        else:
            lines = [
                f"{item['time'].strftime('%H:%M:%S')} - {item['name']}"
                for item in history
            ]
            greeting_text.value = "История приветствий:\n" + "\n".join(lines)

            greeting_history.append({"name": name, "time": current_time})


    
    def filter_morning(tet):
        morning = [item for item in greeting_history if item['time'].hour < 12]
        update_history(morning)
        page.update()

    def filter_evening(tet):
        evening = [item for item in greeting_history if item['time'].hour >= 12]
        update_history(evening)
        page.update()

    

    send_button = ft.ElevatedButton("SEND", icon=ft.Icons.SEND, on_click=on_button_click)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    morning_button = ft.ElevatedButton("Утро (до 12:00)", on_click=filter_morning, )
    evening_button = ft.ElevatedButton("Вечер (после 12:00)", on_click=filter_evening,)

    name_input.on_submit = on_button_click

    page.add(
        ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([name_input, send_button, clear_button]),
        ft.Row([morning_button, evening_button]),
        greeting_text
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
