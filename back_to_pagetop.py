from flet import *
import flet as ft


def main(page: Page):
    page.window_width = 700
    page.scroll = "always"
    list_text = Column()

    def goto_top(e):
        page.scroll_to(key="top", duration=1000)
        page.update()

    page.floating_action_button = FloatingActionButton(
        icon=ft.icons.ARROW_UPWARD,
        bgcolor=ft.colors.BLUE_300,
        on_click=goto_top
    )

    for x in range(0, 30):
        list_text.controls.append(Text(f'data{x}', size=20))

    page.add(
        Container(
            padding=10,
            content=Text("Flet", size=30, weight="bold"),
            key="top",
        ),
        Column([
            list_text
        ])
    )


ft.app(target=main)
