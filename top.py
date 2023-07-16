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
        lv = ft.ListView(expand=True, spacing=15, auto_scroll=False)
        contents.controls.append(Text("Top画面", size=32))
        img = ft.Image(
            src=f"icons/flet.png",
            width=100,
            height=100,
            fit=ft.ImageFit.CONTAIN,
        )
        contents.controls.append(img)
        hosts = Column(expand=True,)
        for _ in range(3):
            hosts.controls.append(
                ft.Container(
                    content=ft.Card(
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
                            padding=10,
                            margin=10,
                        )
                    ),
                )
            )

        lv.controls.append(hosts)

        def check_detail(e):
            page.go("/setting-account/1")

        check_detail_button = ElevatedButton(
            "もっと確認する", on_click=check_detail)
        lv.controls.append(check_detail_button)

        recent_seminars = Container(
            content=lv,
            margin=ft.margin.only(top=10, left=20),
        )
        # 表示内容
        contents.controls.append(lv)
