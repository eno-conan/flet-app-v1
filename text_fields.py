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
import re


class TextFieldsAndSubmit():
    def __init__(
        self,
        page: Page,
        contents: Column,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page

        def button_clicked(e):
            # if (len(company_name_textfield.value) == 0 or len(contract_name_textfield.value) == 0):
            #     page.update()
            #     return
            try:
                # create POST request
                # url = os.getenv('WORKERS_URL')
                # data = {
                #     'CompanyName': company_name_textfield.value,
                #     'ContactName': contract_name_textfield.value,
                # }
                # data_encode = json.dumps(data)
                # requests.post(url, data=data_encode)

                # clear input values
                company_name_textfield.value = ""
                contract_name_textfield.value = ""
                # category_text.value
                date_textfield.value = ""
                page.banner.open = True
                # page.snack_bar.open = True

                submit_button.disabled = True
                # msg_failed_add_customer.visible = False
                # msg_success_add_customer.visible = True
                page.update()
                # page.go('/')
                # msg_success_add_customer.visible = False
            except Exception as e:
                print(e)
                # msg_failed_add_customer.visible = True
                # page.update()

        def textfield_change(e):
            if company_name_textfield.value == "" or contract_name_textfield.value == "":
                submit_button.disabled = True
            elif len(date_textfield.value) != 10:
                submit_button.disabled = True
            else:
                date_pattern = "^20[0-9]{2}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$"
                res = re.match(date_pattern, date_textfield.value)
                if res is not None:
                    print(date_textfield.value)
                    submit_button.disabled = False
            page.update()

        # text fields
        company_name_textfield = ft.TextField(
            label="Company Name", on_change=textfield_change)
        contract_name_textfield = ft.TextField(
            label="Contract Name", on_change=textfield_change)

        def dropdown_changed(e):
            category_text.value = dd.value
            page.update()

        # DropDown(カテゴリ)
        category_text = ft.Text()
        dd = ft.Dropdown(
            on_change=dropdown_changed,
            bgcolor=ft.colors.BLUE_200,
            options=[
                ft.dropdown.Option("Java"),
                ft.dropdown.Option("Python"),
                ft.dropdown.Option("Flutter"),
                ft.dropdown.Option("React"),
                ft.dropdown.Option("Javascript"),
            ],
            width=300,
        )

        date_textfield = ft.TextField(
            width=300,
            label="Please Input yyyy/mm/dd",
            on_change=textfield_change)

        # Notify=================================
        # https://flet.dev/docs/controls/banner
        # https://flet.dev/docs/controls/snackbar
        # page.snack_bar = ft.SnackBar(
        #     content=ft.Text("Create New Seminar!!",),
        #     action_color=ft.colors.LIME_300,
        #     bgcolor=ft.colors.BLUE_700,
        #     action="Alright!",
        #     duration=5000
        # )

        def close_banner(e):
            page.banner.open = False
            page.update()

        page.banner = ft.Banner(
            content_padding=ft.padding.only(
                left=16.0, top=16.0, right=16.0, bottom=8.0),
            bgcolor=ft.colors.GREEN_100,
            leading=ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE,
                            color=ft.colors.GREEN_500, size=40),
            content=ft.Text(
                "Oops, there were some errors while trying to delete the file. What would you like me to do?",
                font_family=ft.FontWeight.W_500,
                size=18,
            ),
            actions=[
                ft.TextButton("Retry", on_click=close_banner),
            ],
        )

        # Submit
        submit_button = ft.ElevatedButton(
            disabled=True,
            text="Submit", on_click=button_clicked)

        contents.controls.append(
            Column(
                [
                    Container(content=Text("セミナー追加", size=32),
                              margin=ft.margin.symmetric(horizontal=20,
                              vertical=10)),
                    Container(content=Column(
                        [company_name_textfield, contract_name_textfield]
                    ),
                        margin=ft.margin.symmetric(horizontal=30, vertical=10)
                    ),
                    Container(content=Text("ジャンル選択", size=20),
                              margin=ft.margin.symmetric(horizontal=20,)
                              ),
                    Container(content=Column([dd]),
                              margin=ft.margin.symmetric(
                                  horizontal=30, vertical=10)
                              ),
                    Container(content=Text("開催日", size=20),
                              margin=ft.margin.symmetric(horizontal=20,)
                              ),
                    Container(content=date_textfield,
                              margin=ft.margin.symmetric(
                                  horizontal=30, vertical=10)
                              ),
                    Container(content=submit_button,
                              margin=ft.margin.only(right=25),
                              alignment=ft.alignment.center_right
                              ),
                ]
            )
        )
