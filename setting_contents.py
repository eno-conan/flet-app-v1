from flet import *
import flet as ft
from flet import (
    Card,
    Column,
    Container,
    Page,
    Row,
    Text,
)


class SettingContents():
    def __init__(
        self,
        page: Page,
        contents: Column,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page

        # タブ「主催セミナー一覧」
        hosts = []
        for i in range(15):
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
                    col={"md": 4, "xl": 6},
                )
            )
        hosts_seminars = Container(
            ft.ResponsiveRow(
                hosts,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            margin=ft.margin.only(top=10, left=20),
        )

        # タブ「参加予定セミナー一覧」
        participates = []
        for i in range(15):
            participates.append(
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
                    col={"md": 4, "xl": 6},
                )
            )
        participate_seminars = Container(
            ft.ResponsiveRow(
                participates,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            margin=ft.margin.only(top=10, left=20),
        )

        # タブ「アカウント削除」
        delete_account_button = ft.ElevatedButton(
            disabled=False,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.RED_500,
            text="アカウント削除",
            # on_click=show_detail
        )

        # 各タブの土台構築
        lv = ft.ListView(expand=True, spacing=5, auto_scroll=False)
        tab_bar_contents = Container(
            margin=ft.margin.only(top=5, left=20),
            content=ft.Tabs(
                selected_index=0,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        text="Check Host seminar",
                        content=hosts_seminars
                    ),
                    ft.Tab(
                        text="Check Participate seminar",
                        # tab_content=ft.Icon(ft.icons.SEARCH),
                        content=participate_seminars),
                    ft.Tab(
                        text="Update User name (password)",
                        # icon=ft.icons.SETTINGS,
                        content=ft.Text("This is Tab 3"),
                    ),
                    ft.Tab(
                        text="Delete Your Account",
                        icon=ft.icons.SETTINGS,
                        content=Container(
                             Column(
                                 controls=[
                                     delete_account_button
                                 ],
                                 expand=True,
                                 scroll=True,
                             ),
                            margin=ft.margin.only(top=20, left=20),
                        ),
                    ),
                ],
                expand=True,
                scrollable=True
            )
        )
        lv.controls.append(tab_bar_contents)
        contents.controls.append(lv)

# 参考（page.views.pop）
# https://flet.dev/docs/guides/python/navigation-and-routing
