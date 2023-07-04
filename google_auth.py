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
from flet.auth.providers.google_oauth_provider import GoogleOAuthProvider
import os
from dotenv import load_dotenv
load_dotenv()

ClientID = os.getenv('ClientID')
ClientSecret = os.getenv('ClientSecret')

class GoogleOAuth():
    def __init__(
        self,
        page: Page,
        contents: list,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page

        provider = GoogleOAuthProvider(
            client_id=ClientID,
            client_secret=ClientSecret,
            redirect_url="http://localhost:8550/api/oauth/redirect"
        )

        def login_google(e):
            self.page.login(provider)

        def logout_google(e):
            page.logout()
            contents.pop()
            log_inout_button = login_button
            contents.append(log_inout_button)
            page.update()
            page.go('/')

        # ログインボタン
        login_button = Container(
            content=ElevatedButton(
                "Sign in Google", bgcolor=ft.colors.LIGHT_BLUE_500, color=ft.colors.WHITE, on_click=login_google,
            ),
            margin=ft.margin.only(right=10)
        )

        # ログアウトボタン
        logout_button = Container(
            content=ElevatedButton(
                "Sign out Google", bgcolor=ft.colors.RED_300, color=ft.colors.WHITE, on_click=logout_google),
            margin=ft.margin.only(right=10)
        )

        if page.auth is None:
            log_inout_button = login_button

        def on_login(e):
            print(page.auth.user['name'], page.auth.user['email'])
            contents.pop()
            log_inout_button = logout_button
            contents.append(log_inout_button)
            # page.session.set("key", "value")
            page.update()
            page.go('/')

        page.on_login = on_login

        contents.append(log_inout_button)

# reference
# https://www.youtube.com/watch?v=t9ca2jC4YTo
