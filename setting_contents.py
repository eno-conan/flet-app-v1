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

        def show_detail(e):
            self.page.views.append(
                ft.View(
                    "/setting-account",
                    [
                        ft.AppBar(title=ft.Text("Store"),
                                  center_title=True,
                                  leading_width=40,
                                  toolbar_height=70,
                                  bgcolor=ft.colors.BLUE_ACCENT_700
                                  ),
                        # ft.ElevatedButton(
                        #     "Go Home", on_click=lambda _: page.go("/")),
                        ft.Column(
                            # horizontal_alignment="stretch",
                            controls=[
                                ft.Container(
                                    expand=1, content=ft.Text("Header")),
                                ft.Container(
                                    expand=3, content=ft.Text("Body")),
                                ft.Container(
                                    expand=1, content=ft.Text("Footer"))
                            ],
                            expand=True,
                        )
                    ],
                )
            )
            self.page.update()

        submit_button = ft.ElevatedButton(
            disabled=False,
            text="Submit", on_click=show_detail)

        contents.controls.append(
            Row(
                controls=[
                    Column(
                        # horizontal_alignment="stretch",
                        controls=[
                            Card(content=Container(
                                Text("Setting Account", weight="bold", size=32), padding=8)),
                            Text("Update Your Profile..."),
                            submit_button,
                        ],
                        expand=True,
                    ),
                    # Column(
                    #     # horizontal_alignment="stretch",
                    #     controls=[
                    #         ft.Container(expand=1, content=ft.Text("Header")),
                    #         ft.Container(expand=3, content=ft.Text("Body")),
                    #         ft.Container(expand=1, content=ft.Text("Footer"))
                    #     ],
                    #     expand=True,
                    #     # visible=False,
                    # ),
                ],
                expand=True
            )
        )

# 参考（page.views.pop）
# https://flet.dev/docs/guides/python/navigation-and-routing