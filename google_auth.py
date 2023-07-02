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

def main(page: ft.Page):

    provider = GoogleOAuthProvider(
        client_id=ClientID,
        client_secret=ClientSecret,
        redirect_url="http://localhost:8550/api/oauth/redirect"
    )

    auth_result_text = Column()

    def login_google(e):
        page.login(provider)

    def on_login(e):
        print(page.auth.user)

        auth_result_text.controls.append(
            Column([
                Text(f"name:{page.auth.user['name']}"),
                Text(f"name:{page.auth.user['email']}"),
            ])
        )
        page.update()

    page.on_login = on_login

    page.add(
        Column([
            Text("Login Google", size=30),
            ElevatedButton(
                "Sign Google", bgcolor="blue", color="white", on_click=login_google),
            auth_result_text
        ])
    )


ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
# reference
# https://www.youtube.com/watch?v=t9ca2jC4YTo
