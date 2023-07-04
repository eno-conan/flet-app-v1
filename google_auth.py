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
# url = os.getenv('WORKERS_URL')


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

        auth_result_text = Column()

        def login_google(e):
            self.page.login(provider)

        def logout_google(e):
            page.logout()
            page.go('/')

        if page.auth is None:
            log_inout_button = Container(
                content=ElevatedButton(
                    "Sign in Google", bgcolor="green", color="white", on_click=login_google),
                margin=ft.margin.only(right=10)
            )
        else:
            log_inout_button = ElevatedButton(
                "Sign out Google", bgcolor="", color="white", on_click=logout_google)

        def on_login(e):
            print(page.auth.user)
            # contents.controls.remove(log_inout_button)
            auth_result_text.controls.append(
                Column([
                    ElevatedButton(
                        "Sign out Google", bgcolor="blue", color="white", on_click=logout_google),
                    Text(f"name:{page.auth.user['name']}"),
                    Text(f"name:{page.auth.user['email']}"),
                ])
            )
            # page.session.set("key", "value")
            page.update()

        page.on_login = on_login

        # contents.controls.append(ft.Text("Login Google", size=30))
        # contents.controls.append(log_inout_button)
        contents.append(log_inout_button)
        # contents.controls.append(auth_result_text)
        # contents.controls.append(
        #     Column([
        #         Text("Login Google", size=30),
        #         log_inout_button,
        #         auth_result_text
        #     ]))

# ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
# reference
# https://www.youtube.com/watch?v=t9ca2jC4YTo
