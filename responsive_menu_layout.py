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
    icons
)
from layout import ResponsiveMenuLayout
from time import sleep
from google_auth import GoogleOAuth
from text_fields import TextFieldsAndSubmit
from card_list import ScrollCardList

from flet.auth.providers.google_oauth_provider import GoogleOAuthProvider
import os
from dotenv import load_dotenv
load_dotenv()

ClientID = os.getenv('ClientID')
ClientSecret = os.getenv('ClientSecret')

if __name__ == "__main__":

    def main(page: Page, title="Basic Responsive Menu"):

        page.title = title

        menu_button = IconButton(icons.MENU)

        page.appbar = AppBar(
            title=Text(f"MyApp", size=32),
            leading=menu_button,
            center_title=True,
            leading_width=40,
            # bgcolor=colors.SURFACE_VARIANT,
            toolbar_height=70,
            bgcolor=ft.colors.LIME_500,
        )

        pages = [
            (
                dict(
                    icon=icons.LANDSCAPE_OUTLINED,
                    selected_icon=icons.LANDSCAPE,
                    label="Menu in landscape",
                ),
                create_page(
                    page,
                    "Menu in landscape",
                    "Menu in landscape is by default shown, side by side with the main content, but can be "
                    "hidden with the menu button.",
                ),
            ),
            (
                dict(
                    icon=icons.PORTRAIT_OUTLINED,
                    selected_icon=icons.PORTRAIT,
                    label="Menu in portrait",
                ),
                create_page(
                    page,
                    "Menu in portrait",
                    "Menu in portrait is mainly expected to be used on a smaller mobile device."
                    "\n\n"
                    "The menu is by default hidden, and when shown with the menu button it is placed on top of the main "
                    "content."
                    "\n\n"
                    "In addition to the menu button, menu can be dismissed by a tap/click on the main content area.",
                ),
            ),
            (
                dict(
                    icon=ft.icons.SETTINGS,
                    selected_icon=icons.INSERT_EMOTICON,
                    label="Setting Your Account",
                ),
                create_page(
                    page,
                    "Minimize to icons",
                    "ResponsiveMenuLayout has a parameter minimize_to_icons. "
                    "Set it to True and the menu is shown as icons only, when normally it would be hidden.\n"
                    "\n\n"
                    "Try this with the 'Minimize to icons' toggle in the top bar."
                    "\n\n"
                    "There are also landscape_minimize_to_icons and portrait_minimize_to_icons properties that you can "
                    "use to set this property differently in each orientation.",
                ),
            ),
        ]

        menu_layout = ResponsiveMenuLayout(page, pages)

        page.appbar.actions = [
            # Text("Login Google"),
            # Container(
            #     content=Switch(
            #         on_change=lambda e: toggle_icons_only(menu_layout)),
            #     margin=ft.margin.only(right=10)
            # )
        ]


        # Add Button
        # menu_layout.navigation_rail.leading = ElevatedButton(
        #     "Add", icon=icons.ADD, expand=True, on_click=lambda e: print("Add clicked")
        # )
        # page.scroll = "always"
        GoogleOAuth(page, page.appbar.actions)
        page.add(menu_layout)

        menu_button.on_click = lambda e: menu_layout.toggle_navigation()

    # main_contentsのレイアウトをこれで統一
    def create_page(page: Page, title: str, body: str):
        # ここの分岐とPathのところの分岐を上手く共通化できそう。
        contents = Column(expand=True, auto_scroll=False)
        if title == "Menu in landscape":
            ScrollCardList(page, contents)
        elif title == "Menu in portrait":
            TextFieldsAndSubmit(page, contents)
        else:
            contents = Row(
                controls=[
                    Column(
                        horizontal_alignment="stretch",
                        controls=[
                            Card(content=Container(
                                Text(title, weight="bold"), padding=8)),
                            Text(body),
                        ],
                        expand=True,
                    ),
                ],
                expand=True
            )
        return contents

    def toggle_icons_only(menu: ResponsiveMenuLayout):
        menu.minimize_to_icons = not menu.minimize_to_icons
        menu.page.update()

    # def toggle_menu_width(menu: ResponsiveMenuLayout):
    #     # Menu\nwidth：クリック時のイベント
    #     # トグルがONの状態のとき、アイコンの横にラベルが表示される
    #     menu.menu_extended = not menu.menu_extended
    #     menu.page.update()

    ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
