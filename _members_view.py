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
from time import sleep

class MembersView():
    def __init__(
        self,
        page: Page,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page
# event when changed textfield values
        def textfield_change(e):
            if company_name_textfield.value == "" or contract_name_textfield.value == "":
                submit_button.disabled = True
            else:
                submit_button.disabled = False
            self.page.update()

        # display Message to fail create new customer
        msg_failed_add_customer = Row(
            [
                ft.Text("Sorry... Failed to send new customer. Retry Access few minutes Later.",
                        size=24, color=ft.colors.RED_500
                        )
            ],
            visible=False
        )

        # display Message to success create new customer
        msg_success_add_customer = Row(
            [
                ft.Text("Success to create new customer!",
                        size=24, color=ft.colors.BLUE_900,
                        )
            ],
            visible=False
        )

        # click submit button
        def button_clicked(e):
            if (len(company_name_textfield.value) == 0 or len(contract_name_textfield.value) == 0):
                page.update()
                return
            # create POST request
            try:
                url = os.getenv('WORKERS_URL')
                data = {
                    'CompanyName': company_name_textfield.value,
                    'ContactName': contract_name_textfield.value,
                }
                data_encode = json.dumps(data)
                requests.post(url, data=data_encode)
                # clear input values
                company_name_textfield.value = ""
                contract_name_textfield.value = ""
                submit_button.disabled = True
                msg_failed_add_customer.visible = False
                msg_success_add_customer.visible = True
                page.update()
                # sleep(1)
                # page.go('/')
                msg_success_add_customer.visible = False
            except Exception as e:
                print(e)
                msg_failed_add_customer.visible = True
                page.update()

        # text fields
        company_name_textfield = ft.TextField(
            label="Company Name", on_change=textfield_change)
        contract_name_textfield = ft.TextField(
            label="Contract Name", on_change=textfield_change)

        # button to add customer
        submit_button = ft.ElevatedButton(
            disabled=True,
            text="Submit", on_click=button_clicked)

        self.contents = Column(controls=[
             Container(
                Text
                (
                    value="Add New Customers",
                    style=ft.FontWeight.W_500,
                    size=28
                ),
                expand=False,
                padding=ft.padding.only(top=15),
            ),
            Row(
                [
                    Container(
                        Text(value="Company Name"),
                        width=150,
                        expand=False,
                        padding=ft.padding.only(left=10),
                    ),
                    company_name_textfield
                ]
            ),
            Row(
                [
                    Container(
                        Text(value="Contract Name"),
                        width=150,
                        expand=False,
                        padding=ft.padding.only(left=10),
                    ),
                    contract_name_textfield
                ]
            ),
            msg_failed_add_customer,
            msg_success_add_customer,
            Row(
                [
                    submit_button
                ]
            )
        ],
        expand=True, auto_scroll=False
        )

    def get_content(self):
        return self.contents