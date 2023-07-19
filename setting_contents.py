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
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page
        self.contents = Column(expand=True, auto_scroll=False)

        # タブ「主催セミナー一覧」
        hosts = Column(expand=True,)
        for i in range(10):
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
        hosts_seminars = Container(
            content=hosts,
            margin=ft.margin.only(top=10, left=20),
        )

        # タブ「参加予定セミナー一覧」
        participates = Column(expand=True,)
        for i in range(10):
            participates.controls.append(
                ft.Container(
                    content=ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        title=ft.Text(
                                            "フロントエンド基礎", weight=ft.FontWeight.W_700),
                                        subtitle=ft.Text(
                                            "Reactを学習してみよう"
                                        ),
                                    ),
                                    ft.Row(
                                        [ft.TextButton("詳細確認"),],
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
        participate_seminars = Container(
            content=participates,
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

        def change_tab_event(e):
            pass
            # print(tabs.selected_index)
            # tabs.selected_index = 1
            # page.update()

        tabs = ft.Tabs(
            on_change=change_tab_event,
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Check Participate seminar",
                    # tab_content=ft.Icon(ft.icons.SEARCH),
                    content=participate_seminars),
                ft.Tab(
                    text="Check Host seminar",
                    content=hosts_seminars
                ),
                # ft.Tab(
                #     text="Update User name (password)",
                #     # icon=ft.icons.SETTINGS,
                #     content=ft.Text("This is Tab 3"),
                # ),
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
        )
        self.tabs = tabs
        # 各タブの土台構築
        lv = ft.ListView(expand=True, spacing=5, auto_scroll=False)
        tab_bar_contents = Container(
            margin=ft.margin.only(top=5, left=10),
            content=tabs
        )
        lv.controls.append(tab_bar_contents)
        self.contents.controls.append(lv)

    def get_content(self):
        return self.contents