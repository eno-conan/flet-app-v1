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
    icons
)
class ScrollSeminarList():
    def __init__(
        self,
        page: Page,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page
        # page title
        self.contents = Column(expand=True, auto_scroll=False)
        self.contents.controls.append(ft.Text("開催セミナー一覧", size=30, weight="bold"))
        lv = ft.ListView(expand=True, spacing=15, auto_scroll=False)
        seminars_arr = []
        for i in range(30):
            seminars_arr.append(
                ft.Container(
                    content=ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        title=ft.Text(
                                            "Python",weight=ft.FontWeight.W_700),
                                        subtitle=ft.Text(
                                            "Pythonの基礎を理解しよう"
                                        ),
                                    ),
                                    ft.Row(
                                        [ft.TextButton("詳細確認"),],
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
        seminars = Container(
            ft.ResponsiveRow(
                seminars_arr,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            margin=ft.margin.only(top=10, left=20),
        )
        lv.controls.append(seminars)
        self.contents.controls.append(lv)

    def get_content(self):
        return self.contents