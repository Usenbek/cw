# from datetime import date
# from flet import Text, TextField

import flet as ft

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text(value='История приветствий:')

    # greeting_text.value = 'Привет мир'
    # greeting_text.color = ft.Colors.GREEN

    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()

        if name:
            greeting_text.value = f'Hello {name}'
            greeting_text.color = None
            name_input.value = None

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = "История приветствий: \n" + "\n".join(greeting_history)
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    # name_input.expand = False

    elevated_button = ft.ElevatedButton(text="send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

    text_button = ft.TextButton(text='send', on_click=on_button_click, icon=ft.Icons.SEND)

    icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        greeting_text.value = 'История очищена'
        page.update()

    # name_input.on_submit = clear_history

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    # page.add(greeting_text, name_input, text_button, elevated_button, icon_button)

    page.add(greeting_text, ft.Row([name_input, elevated_button, clear_button]), history_text)

ft.app(target=main)
