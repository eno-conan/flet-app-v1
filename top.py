import flet as ft
from flet import (
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
    TextButton
)
import datetime
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv()


class Top():
    def __init__(
        self,
        page: Page,
        contents: Column,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page

        # データ取得
        result = [{'CustomerId': 1, 'CompanyName': 'Alfreds Futterkiste', 'ContactName': 'Maria Anders'}, {'CustomerId': 2, 'CompanyName': 'Around the Horn', 'ContactName': 'Thomas Hardy'}, {'CustomerId': 3, 'CompanyName': 'Bs Beverages', 'ContactName': 'Victoria Ashworth'}, {'CustomerId': 4, 'CompanyName': 'Bs Beverages', 'ContactName': 'Random Name'}, {'CustomerId': 36, 'CompanyName': 'add', 'ContactName': 'add'}]
        url = os.getenv('WORKERS_URL')
        response = requests.get(url)
        result = response.json()
        print(result)

        lv = ft.ListView(expand=6, spacing=15, auto_scroll=False)
        img = ft.Image(
            src=f"icons/flet.png",
            width=50,
            height=50,
            fit=ft.ImageFit.CONTAIN,
        )
        contents.controls.append(
            Row(
                [
                    Text("直近の参加予定セミナー", size=24),
                    img
                ]
            ),
        )
        hosts = Column(expand=True)
        for data in result:
            hosts.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    title=ft.Text(
                                        data["CompanyName"], weight=ft.FontWeight.W_700),
                                    subtitle=ft.Text(
                                        data["ContactName"]
                                    ),
                                ),
                                ft.Row(
                                    [ft.TextButton("内容確認"),],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                        padding=5,
                        margin=10,
                    )
                )
            )
        lv.controls.append(hosts)

        def check_detail(e):
            page.go("/setting-account/1")

        check_detail_button = ElevatedButton(
            "もっと確認する",
            color=ft.colors.BLUE_700,
            on_click=check_detail,
            bgcolor=ft.colors.BLUE_50
            )
        lv.controls.append(check_detail_button)

        contents.controls.append(lv)
        contents.controls.append(ft.Divider(height=10, thickness=3))
        contents.controls.append(Text("お知らせ", size=24, expand=4),)

        # recent_seminars = Container(
        #     content=lv,
        #     margin=ft.margin.only(top=10, left=20),
        # )
        # 表示内容
