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
        for _ in range(15):
            lv.controls.append(ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                               ft.ListTile(
                                   leading=ft.Icon(ft.icons.ALBUM),
                                   title=ft.Text("The Enchanted Nightingale"),
                                   subtitle=ft.Text(
                                       "Music by Julie Gable. Lyrics by Sidney Stein."
                                   ),
                               ),
                               ft.Row(
                                   [ft.TextButton("Buy tickets"),
                                    ft.TextButton("Listen")],
                                   alignment=ft.MainAxisAlignment.END,
                               ),
                               ]
                    ),
                    width=400,
                    padding=10,
                    margin=10
                )
            ))

        contents.controls.append(lv)
