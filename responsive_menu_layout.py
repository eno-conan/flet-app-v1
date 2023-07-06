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
from text_fields import TextFieldsAndSubmit
from card_list import ScrollCardList
from setting_contents import SettingContents

from flet.auth.providers.google_oauth_provider import GoogleOAuthProvider
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":

    def main(page: Page, title="Basic Responsive Menu"):

        page.title = title
        page.theme_mode = "light"
        menu_button = IconButton(icons.MENU, icon_color=ft.colors.WHITE)
        page.appbar = AppBar(
            title=Text(f"My Flet Sample App", size=32, color=ft.colors.WHITE),
            leading=menu_button,
            center_title=True,
            leading_width=40,
            toolbar_height=70,
            bgcolor=ft.colors.BLUE_ACCENT_700
        )

        pages = [
            (
                dict(
                    icon=ft.icons.HOUSE_OUTLINED,
                    selected_icon=ft.icons.HOUSE,
                    label="Top",
                ),
                create_page(
                    page,
                    "Top",
                ),
            ),
            (
                dict(
                    icon=ft.icons.FEATURED_PLAY_LIST_OUTLINED,
                    selected_icon=ft.icons.FEATURED_PLAY_LIST_ROUNDED,
                    label="Card List",
                ),
                create_page(
                    page,
                    "Card List",
                ),
            ),
            (
                dict(
                    icon=ft.icons.ADD_BOX_OUTLINED,
                    selected_icon=ft.icons.ADD_BOX,
                    label="Add Form",
                ),
                create_page(
                    page,
                    "Add Form",
                ),
            ),
            (
                dict(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon=ft.icons.SETTINGS,
                    label="Setting Your Account",
                ),
                create_page(
                    page,
                    "Minimize to icons",
                ),
            ),
        ]

        menu_layout = ResponsiveMenuLayout(page, pages)
        page.add(menu_layout)
        menu_button.on_click = lambda e: menu_layout.toggle_navigation()

        page.appbar.actions = []
        ToggleDarkLight(page, page.appbar.actions)
        GoogleOAuth(page, page.appbar.actions)
        page.update()

    # main_contentsのレイアウトをこれで統一

    def create_page(page: Page, title: str):
        # ここの分岐とPathのところの分岐を上手く共通化できそう。
        contents = Column(expand=True, auto_scroll=False)
        if title == "Top":
            contents.controls.append(Text("Top画面", size=32))
            img = ft.Image(
                src=f"icons/flet.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
            )
            contents.controls.append(img)
        elif title == "Card List":
            ScrollCardList(page, contents)
        elif title == "Add Form":
            TextFieldsAndSubmit(page, contents)
        else:
            SettingContents(page, contents)
        return contents

    ft.app(target=main, port=8550, assets_dir="assets", view=ft.WEB_BROWSER)
    # def toggle_icons_only(menu: ResponsiveMenuLayout):
    #     menu.minimize_to_icons = not menu.minimize_to_icons
    #     menu.page.update()
    # def toggle_menu_width(menu: ResponsiveMenuLayout):
    #     # Menu\nwidth：クリック時のイベント
    #     # トグルがONの状態のとき、アイコンの横にラベルが表示される
    #     menu.menu_extended = not menu.menu_extended
    #     menu.page.update()
    # Add Button
    # menu_layout.navigation_rail.leading = ElevatedButton(
    #     "Add", icon=icons.ADD, expand=True, on_click=lambda e: print("Add clicked")
    # )
    # page.scroll = "always"
