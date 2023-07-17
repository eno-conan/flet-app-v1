from copy import deepcopy

import flet as ft
from flet import (
    AppBar,
    Card,
    Column,
    Container,
    ElevatedButton,
    IconButton,
    Page,
    Row,
    Switch,
    Text,
    icons,
)
from layout import ResponsiveMenuLayout
from google_auth import GoogleOAuth
from switch_right_dark import ToggleDarkLight
from add_form import TextFieldsAndSubmit
from card_list import ScrollCardList
from card_list_infinite import ScrollCardListInfinite
from setting_contents import SettingContents
from top import Top

from flet.auth.providers.google_oauth_provider import GoogleOAuthProvider
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":

    def main(page: Page, title="Flet Seminar App"):

        page.title = title
        page.theme_mode = "light"
        menu_button = IconButton(icons.MENU, icon_color=ft.colors.WHITE)
        page.appbar = AppBar(
            title=Text(f"Flet App", size=32, color=ft.colors.WHITE),
            leading=menu_button,
            center_title=True,
            leading_width=40,
            toolbar_height=70,
            bgcolor=ft.colors.BLUE_ACCENT_700
        )

        menu_layout = ResponsiveMenuLayout(page)
        page.add(menu_layout)
        menu_button.on_click = lambda e: menu_layout.toggle_navigation()

        page.appbar.actions = []
        ToggleDarkLight(page, page.appbar.actions)
        GoogleOAuth(page, page.appbar.actions)
        page.update()

    # main_contentsのレイアウトをこれで統一

    ft.app(target=main, port=8550, assets_dir="assets", view=ft.WEB_BROWSER)
