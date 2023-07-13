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


class ScrollCardList():
    def __init__(
        self,
        page: Page,
        contents: Column,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page
        # page title
        contents.controls.append(ft.Text("一覧画面", size=30, weight="bold"))
        lv = ft.ListView(expand=True, spacing=15, auto_scroll=False)
        hosts = []
        for i in range(30):
            hosts.append(
                ft.Container(
                    content=ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        title=ft.Text(
                                            "The Enchanted Nightingale"),
                                        subtitle=ft.Text(
                                            "Music by Julie Gable. Lyrics by Sidney Stein."
                                        ),
                                    ),
                                    ft.Row(
                                        [ft.TextButton("Check!"),],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            ),
                            width=400,
                            padding=10,
                            margin=10,
                        )
                    ),
                    col={"sm": 6, "md": 6, "xl": 4},
                )
            )
        hosts_seminars = Container(
            ft.ResponsiveRow(
                hosts,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            margin=ft.margin.only(top=10, left=20),
        )
        lv.controls.append(hosts_seminars)

        contents.controls.append(lv)
