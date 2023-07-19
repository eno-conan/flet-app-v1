import flet as ft
from flet import (
    Container,
    IconButton,
    Page,
    ButtonStyle,
    ProgressBar,
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

        # 切り替え時にプログレスバー表示
        page.splash = ProgressBar(visible=False)

        def change_theme(e):
            # プログレスバー表示
            page.splash.visible = True
            page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
            # ft.Theme()
            page.update()

            # アニメーション適用のための時間確保(1s)
            sleep(1)

            # アイコンの選択状態
            toggle_dark_light.selected = not toggle_dark_light.selected
            # ToolTipの表示文言更新
            toggle_dark_light.tooltip = f"switch light and dark mode (currently {'dark' if toggle_dark_light.selected else 'light'} mode)"
            # if toggle_dark_light.selected:
            #     page.appbar.title = Text(
            #         f"MyApp", size=32, color=ft.colors.YELLOW_500)
            # else:
            #     page.appbar.title = Text(
            #         f"MyApp", size=32, color=ft.colors.WHITE)

            # プログレスバー非表示
            page.splash.visible = False
            page.update()

        # 切り替え用のボタン
        toggle_dark_light = IconButton(
            # ToolTipの表示文言
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
