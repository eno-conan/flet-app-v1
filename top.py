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
        for _ in range(3):
            hosts.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    title=ft.Text(
                                        "Javaは簡単ではない", weight=ft.FontWeight.W_700),
                                    subtitle=ft.Text(
                                        "Javaは決して簡単ではない・・・"
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
