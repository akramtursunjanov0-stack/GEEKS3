import flet as ft


def main(page: ft.Page):
    page.title = "История приветствий"
    page.padding = 20

    greetings = []  # история приветствий

    name_input = ft.TextField(label="Введите имя", width=300)
    history_column = ft.Column()
    info_text = ft.Text("", color="red")

    def update_history():
        history_column.controls.clear()
        for g in greetings:
            history_column.controls.append(ft.Text(g))
        page.update()

    def add_greeting(e):
        name = name_input.value.strip()
        if not name:
            info_text.value = "Введите имя!"
            page.update()
            return

        greetings.append(f"Привет, {name}!")
        name_input.value = ""
        info_text.value = ""
        update_history()

    def delete_last(e):
        if greetings:
            greetings.pop()
            info_text.value = ""
            update_history()
        else:
            info_text.value = "История пуста!"
            page.update()

    page.add(
        name_input,
        ft.ElevatedButton("Добавить приветствие", on_click=add_greeting),
        ft.ElevatedButton("Удалить последнее", on_click=delete_last),
        info_text,
        ft.Divider(),
        history_column,
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)