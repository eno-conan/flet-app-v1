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
    icons
)
import datetime


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
        page.dialog = ft.AlertDialog()

        def button_clicked(e):
            try:
                # create POST request
                # url = os.getenv('WORKERS_URL')
                # data = {
                #     'CompanyName': seminar_name_textfield.value,
                #     'ContactName': description_textfield.value,
                # }
                # data_encode = json.dumps(data)
                # requests.post(url, data=data_encode)

                # 入力値初期化
                seminar_name_textfield.value = ""
                description_textfield.value = ""
                category_text.value = None
                date_textfield.value = ""
                # Modal
                page.dialog.open = False
                page.banner.open = True
                # page.snack_bar.open = True
                submit_button.disabled = True
                page.update()
            except Exception as e:
                print(e)
                # msg_failed_add_customer.visible = True
                # page.update()

        # 不正日付のメッセージ表示
        msg_invalid_date_text = ft.Text()
        msg_invalid_date = Row(
            [
                ft.Text("日付の形式がyyyy/mm/ddではない、または存在しない日付です。",
                        size=20, color=ft.colors.RED_500
                        )
            ],
            visible=False
        )

        def textfield_change(e):
            msg_invalid_date.visible = False
            if seminar_name_textfield.value == "" or description_textfield.value == "":
                submit_button.disabled = True
            elif len(date_textfield.value) != 10:
                submit_button.disabled = True
            else:
                is_exist_date = False
                try:
                    date_split_slush = date_textfield.value.split('/')
                    if len(date_split_slush) != 3:
                        # スラッシュ分割で、配列の大きさが3ではない場合、フォーマット不正
                        # msg_invalid_date_text.value = '日付の入力形式が正しくないです'
                        msg_invalid_date.visible = True
                    else:
                        # 存在日付チェック
                        new_data_str = "%04s/%02s/%02s" % (
                            date_split_slush[0], date_split_slush[1], date_split_slush[2])
                        datetime.datetime.strptime(new_data_str, "%Y/%m/%d")
                        is_exist_date = True
                        if is_exist_date:
                            submit_button.disabled = False
                except:
                    # msg_invalid_date_text.value = '日付の入力形式が正しくないです'
                    msg_invalid_date.visible = True
            page.update()

        # text fields
        seminar_name_textfield = ft.TextField(
            label="Seminar Name", on_change=textfield_change)
        description_textfield = ft.TextField(
            label="Description", on_change=textfield_change)

        def dropdown_changed(e):
            category_text.value = dd.value
            page.update()

        # DropDown(カテゴリ)
        category_text = ft.Text()
        categories_arr = []
        for category in ['Java', 'Python', 'Flutter', 'React', 'Javascript', 'Docker']:
            categories_arr.append(ft.dropdown.Option(category))
        dd = ft.Dropdown(
            on_change=dropdown_changed,
            bgcolor=ft.colors.BLUE_200,
            options=categories_arr,
            width=300,
        )

        # 開催日（テキストフィールド）
        date_textfield = ft.TextField(
            width=300,
            label="Please Input yyyy/mm/dd",
            on_change=textfield_change)

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
                ft.TextButton("Close", on_click=close_banner),
            ],
        )

        def open_dlg_modal(e):
            page.dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Confirm Create Seminar"),
                content=ft.Container(
                    height=150,
                    width=200,
                    content=Column(
                        [
                            ft.Text(seminar_name_textfield.value),
                            ft.Text(description_textfield.value),
                            ft.Text(category_text.value),
                            ft.Text(date_textfield.value),
                        ]
                    )),
                actions=[
                    ft.TextButton("Create Seminar!", on_click=button_clicked),
                    ft.TextButton("Fix", on_click=close_dlg),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )
            page.dialog.open = True
            page.update()

        def close_dlg(e):
            page.dialog.open = False
            page.update()

        # Submit
        submit_button = ft.ElevatedButton(
            disabled=True,
            text="Submit", on_click=open_dlg_modal)

        # 表示内容
        contents.controls.append(
            Column(
                [
                    Container(content=Text("セミナー追加", size=32),
                              margin=ft.margin.symmetric(horizontal=20,
                              vertical=10)),
                    Container(content=Column(
                        [seminar_name_textfield, description_textfield]
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
                              margin=ft.margin.only(
                                  left=30, top=10)
                              ),
                    Container(content=msg_invalid_date,
                              margin=ft.margin.symmetric(
                                  horizontal=30)
                              ),
                    Container(content=submit_button,
                              margin=ft.margin.only(right=25),
                              alignment=ft.alignment.center_right
                              ),
                ]
            )
        )

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
