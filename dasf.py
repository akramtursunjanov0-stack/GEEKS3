import flet 
from flet import Page, Text, ElevatedButton

def main(page: Page):
    def on_click(len):
        txt.value = "Вы нажали кнопку!"
        page.update()

    txt = Text("Нажмите кнопку")
    btn = ElevatedButton("Клик", on_click=on_click)

    page.add(txt, btn)

flet.app(target=main)

