import flet as ft
from flet import (
    Container,
    IconButton,
    Page,
    ButtonStyle,
    ProgressBar,
    AppBar,
    Text,
    icons,
)

from time import sleep


class ToggleDarkLight():
    def __init__(
        self,
        page: Page,
        contents: list,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page

        # ADD PROGESSBAR EFFECT WHEN CHANGE LIGHT OR DARK
        page.splash = ProgressBar(visible=False)

        def change_theme(e):
            # page.splash.visible = True
            page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
            page.update()

            # DELAY EFFECT THE ANIMATION
            sleep(0.5)

            # CHANGE THE ICON DARK MODE OR LIGHT MODE
            toggle_dark_light.selected = not toggle_dark_light.selected
            toggle_dark_light.tooltip = f"switch light and dark mode (currently {'dark' if toggle_dark_light.selected else 'light'} mode)"
            # if toggle_dark_light.selected:
            #     page.appbar.title = Text(
            #         f"MyApp", size=32, color=ft.colors.BLACK45)
            #     page.appbar.leading = IconButton(
            #         icons.MENU, icon_color=ft.colors.BLACK45)
            # else:
            #     page.appbar.title = Text(
            #         f"MyApp", size=32, color=ft.colors.BLACK)
            #     page.appbar.leading = IconButton(
            #         icons.MENU, icon_color=ft.colors.BLACK)

            # AND DISABLE AGAIN THE PROGRESSBAR WHEN CHANGE DARK MODE
            page.splash.visible = False
            page.update()

        # CREATE TOGLE BUTTON DARK MODE LIGHT
        toggle_dark_light = IconButton(
            tooltip=f"switch light and dark mode (currently light mode)",
            on_click=change_theme,
            icon="light_mode",
            selected_icon="dark_mode",
            style=ButtonStyle(
                # change color if light and dark
                color={"": ft.colors.ORANGE_300,
                       "selected": ft.colors.YELLOW},
            )
        )

        contents.append(
            Container(
                content=toggle_dark_light,
                margin=ft.margin.only(right=10)
            )
        )
