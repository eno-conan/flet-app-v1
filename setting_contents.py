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

        contents.controls.append(
            Row(
                controls=[
                    Column(
                        horizontal_alignment="stretch",
                        controls=[
                            Card(content=Container(
                                Text("Setting Your Account", weight="bold", size=32), padding=8)),
                            Text("Update Your Profile..."),
                        ],
                        expand=True,
                    ),
                ],
                expand=True
            ))
