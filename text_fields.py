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
            # create POST request
            try:
                # url = os.getenv('WORKERS_URL')
                # data = {
                #     'CompanyName': company_name_textfield.value,
                #     'ContactName': contract_name_textfield.value,
                # }
                # data_encode = json.dumps(data)
                # requests.post(url, data=data_encode)
                # # clear input values
                company_name_textfield.value = ""
                contract_name_textfield.value = ""
                # submit_button.disabled = True
                # msg_failed_add_customer.visible = False
                # msg_success_add_customer.visible = True
                page.update()
                # トーストの使い方が特殊な印象
                # Container(content=Toast(
                #     page,
                #     icons.PERSON_SHARP,
                #     "Toast title",
                #     "Toast description",
                #     submit_button,
                #     ft.colors.AMBER_500,
                #     auto_close=10
                # ).struct()
                # page.go('/')
                # msg_success_add_customer.visible = False
            except Exception as e:
                print(e)
                # msg_failed_add_customer.visible = True
                # page.update()

        def textfield_change(e):
            if company_name_textfield.value == "" or contract_name_textfield.value == "":
                submit_button.disabled = True
            else:
                submit_button.disabled = False
            page.update()

        submit_button = ft.ElevatedButton(
            disabled=True,
            text="Submit", on_click=button_clicked)

        # text fields
        company_name_textfield = ft.TextField(
            label="Company Name", on_change=textfield_change)
        contract_name_textfield = ft.TextField(
            label="Contract Name", on_change=textfield_change)
            
        contents.controls.append(
            Column(
                [
                    Container(content=company_name_textfield,
                              margin=ft.margin.symmetric(horizontal=20)),
                    Container(content=contract_name_textfield,
                              margin=ft.margin.symmetric(horizontal=20)
                              ),
                    Container(content=submit_button,
                              margin=ft.margin.only(right=25),
                              alignment=ft.alignment.center_right),
                ]
            )
        )
