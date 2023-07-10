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
        host_seminars = Column(expand=True, auto_scroll=False)
        # host_seminars.controls.append(
        #     ft.Text("開催予定のセミナー一覧", size=30, weight="bold"))
        lv = ft.ListView(expand=True, spacing=5, auto_scroll=False)
        for _ in range(5):
            lv.controls.append(
                ft.Card(
                    color=ft.colors.AMBER_100,
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.ALBUM),
                                    title=ft.Text(
                                        "The Enchanted Nightingale"),
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
                        # width=400,
                        # height=100,
                        padding=5,
                        margin=ft.margin.symmetric(
                            vertical=10, horizontal=20)
                    )
                ),
            )
        host_seminars.controls.append(lv)

        # タブ「参加予定セミナー一覧」
        participate_seminars = Container(
            ft.ResponsiveRow(
                [
                    ft.Container(
                        ft.Text("Column 1"),
                        height=100,
                        padding=5,
                        bgcolor=ft.colors.YELLOW,
                        col={"md": 4, "xl": 2},
                    ),
                    ft.Container(
                        ft.Text("Column 2"),
                        height=100,
                        padding=5,
                        bgcolor=ft.colors.GREEN,
                        col={"md": 4, "xl": 2},
                    ),
                    ft.Container(
                        ft.Text("Column 3"),
                        height=100,
                        padding=5,
                        bgcolor=ft.colors.BLUE,
                        col={"md": 4, "xl": 2},
                    ),
                    ft.Container(
                        ft.Text("Column 4"),
                        height=100,
                        padding=5,
                        bgcolor=ft.colors.PINK_300,
                        col={"md": 4, "xl": 2},
                    ),
                    ft.Container(
                        ft.Text("Column 5"),
                        height=100,
                        padding=5,
                        bgcolor=ft.colors.PURPLE_300,
                        col={"md": 4, "xl": 2},
                    ),
                ],
            ),
            #  Column(
            #      # horizontal_alignment="stretch",
            #      controls=[
            #          Text("Hello"),
            #      ],
            #      expand=True,
            #      scroll=True,
            #  ),
            margin=ft.margin.only(top=5, left=20),
        )
        # def show_detail(e):
        #     self.page.views.append(
        #         ft.View(
        #             "/setting-account-detail",
        #             [
        #                 ft.AppBar(
        #                     title=Text(f"Manage Your Seminar",
        #                                size=32, color=ft.colors.WHITE),
        #                     center_title=True,
        #                     leading_width=40,
        #                     toolbar_height=70,
        #                     bgcolor=ft.colors.BLUE_ACCENT_700
        #                 ),
        #                 ft.Column(
        #                     # alignment=ft.alignment.center,
        #                     # horizontal_alignment="stretch",
        #                     controls=[
        #                         ft.Container(
        #                             expand=1, content=ft.Text("your host seminars", size=20)),
        #                         ft.Container(
        #                             margin=ft.margin.symmetric(horizontal=20),
        #                             expand=3,
        #                             # content=images
        #                             content=ft.ResponsiveRow(
        #                                 [
        #                                     ft.Container(
        #                                         ft.Text("Column 1"),
        #                                         height=100,
        #                                         padding=5,
        #                                         bgcolor=ft.colors.YELLOW,
        #                                         col={"md": 4, "xl": 2},
        #                                     ),
        #                                     ft.Container(
        #                                         ft.Text("Column 2"),
        #                                         height=100,
        #                                         padding=5,
        #                                         bgcolor=ft.colors.GREEN,
        #                                         col={"md": 4, "xl": 2},
        #                                     ),
        #                                     ft.Container(
        #                                         ft.Text("Column 3"),
        #                                         height=100,
        #                                         padding=5,
        #                                         bgcolor=ft.colors.BLUE,
        #                                         col={"md": 4, "xl": 2},
        #                                     ),
        #                                     ft.Container(
        #                                         ft.Text("Column 4"),
        #                                         height=100,
        #                                         padding=5,
        #                                         bgcolor=ft.colors.PINK_300,
        #                                         col={"md": 4, "xl": 2},
        #                                     ),
        #                                 ],
        #                             )
        #                         ),
        #                         ft.Container(
        #                             expand=1, content=ft.Text("Footer")),
        #                     ],
        #                     expand=True,
        #                 )
        #             ],
        #         )
        #     )
        #     self.page.update()

        # check_host_seminar = ft.ElevatedButton(
        #     disabled=False,
        #     text="Submit", on_click=show_detail)

        # タブ「アカウント削除」
        delete_account_button = ft.ElevatedButton(
            disabled=False,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.RED_500,
            text="アカウント削除",
            # on_click=show_detail
        )

        # 各タブ
        t = Container(
            margin=ft.margin.only(top=5, left=20),
            content=ft.Tabs(
                selected_index=0,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        text="Check Host seminar",
                        content=host_seminars
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
                            # alignment=ft.alignment.center,
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
        contents.controls.append(t)

# 参考（page.views.pop）
# https://flet.dev/docs/guides/python/navigation-and-routing
