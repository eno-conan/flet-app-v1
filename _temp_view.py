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
import json
import os
import requests

class TempView():
    def __init__(
        self,
        page: Page,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page
        self.contents = Column(expand=True, auto_scroll=False)
        self.contents.controls.append( Container(
                Text
                (
                    value="Add New Customers",
                    style=ft.FontWeight.W_500,
                    size=28
                ),
                expand=False,
                padding=ft.padding.only(top=15),
            ))

    def get_content(self):
        return self.contents