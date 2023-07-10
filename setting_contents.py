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

        t = Container(
            margin=ft.margin.only(top=5, left=20),
            content=ft.Tabs(
                selected_index=0,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        text="Check Host seminar",
                        content=ft.Container(
                            content=ft.Text("This is Tab 1"),
                        ),
                    ),
                    ft.Tab(
                        text="Check Participate seminar",
                        # tab_content=ft.Icon(ft.icons.SEARCH),
                        content=Container(
                            # alignment=ft.alignment.center,
                             Column(
                                 # horizontal_alignment="stretch",
                                 controls=[
                                     Text("Hello"),
                                     Text("Hello"),
                                     Text("Hello"),
                                     Text("Hello"),
                                 ],
                                 expand=True,
                                 scroll=True,
                             ),
                            margin=ft.margin.only(top=5, left=20),
                        ),
                    ),
                    ft.Tab(
                        text="Update User name (password)",
                        # icon=ft.icons.SETTINGS,
                        content=ft.Text("This is Tab 3"),
                    ),
                    ft.Tab(
                        text="Delete Your Account",
                        icon=ft.icons.SETTINGS,
                        content=ft.Text("Delete Your Account"),
                    ),
                ],
                # expand=True,
            )
        )

        contents.controls.append(t)

# 参考（page.views.pop）
# https://flet.dev/docs/guides/python/navigation-and-routing
