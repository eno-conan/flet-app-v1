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

        def reset_state():
            # 入力値初期化
            seminar_name_textfield.value = ""
            description_textfield.value = ""
            dd.value = ""
            start_hour_dd.value = ""
            start_minute_dd.value = ""
            end_hour_dd.value = ""
            end_minute_dd.value = ""
            date_textfield.value = ""
            # モーダル非表示・バナー表示
            page.dialog.open = False
            page.banner.open = True
            # page.snack_bar.open = True
            submit_button.disabled = True

        def button_clicked(e):
            try:
                # POSTリクエスト作成
                # url = os.getenv('WORKERS_URL')
                # data = {
                #     'CompanyName': seminar_name_textfield.value,
                #     'ContactName': description_textfield.value,
                # }
                # data_encode = json.dumps(data)
                # requests.post(url, data=data_encode)
                print(seminar_name_textfield.value,
                      description_textfield.value,
                      category_text.value,
                      date_textfield.value,
                      is_public.value
                      )

                # 初期表示状態に戻す
                reset_state()

                page.update()
            except Exception as e:
                print(e)
                # msg_failed_add_customer.visible = True
                # page.update()

        def update_disable_submit_button():
            # 入力前の段階では非活性確定
            for field in [seminar_name_textfield, description_textfield, participates_textfield, date_textfield]:
                if field.value == "":
                    return
            if invalid_msg_seminar_name_description.visible or invalid_msg_participates.visible or invalid_msg_date.visible:
                return
            else:
                submit_button.disabled = False
            page.update()

        # セミナー名・概要=========================
        invalid_msg_seminar_name_description = Row(
            [
                ft.Text("セミナー名・概要は必須入力です。",
                        size=20, color=ft.colors.RED_500
                        )
            ],
            visible=False
        )

        def change_seminar_name_description(e):
            invalid_msg_seminar_name_description.visible = True
            if not seminar_name_textfield.value == "" and not description_textfield.value == "":
                invalid_msg_seminar_name_description.visible = False
            page.update()
            update_disable_submit_button()

        seminar_name_textfield = ft.TextField(
            height=50,
            cursor_height=20,
            label="Seminar Name", on_change=change_seminar_name_description)
        description_textfield = ft.TextField(
            height=50,
            cursor_height=20,
            label="Description", on_change=change_seminar_name_description)

        # 参加者数=========================
        invalid_msg_participates = Row(
            [
                ft.Text("参加者は0より大きい数で入力してください",
                        size=20, color=ft.colors.RED_500
                        )
            ],
            visible=False
        )

        def change_participates(e):
            invalid_msg_participates.visible = True
            try:
                if int(participates_textfield.value) > 0:
                    invalid_msg_participates.visible = False
            except ValueError:
                pass
            page.update()
            update_disable_submit_button()

        participates_textfield = ft.TextField(
            keyboard_type=ft.KeyboardType.NUMBER,  # for mobile option
            height=50,
            width=200,
            cursor_height=20,
            label="number", on_change=change_participates)

        # カテゴリ=========================
        def category_dropdown_changed(e):
            category_text.value = dd.value
            page.update()

        category_text = ft.Text()
        categories_arr = []
        for category in ['Java', 'Python', 'Flutter', 'React', 'Javascript', 'Docker']:
            categories_arr.append(ft.dropdown.Option(category))
        dd = ft.Dropdown(
            on_change=category_dropdown_changed,
            bgcolor=ft.colors.BLUE_200,
            options=categories_arr,
            width=300,
        )

        # 開催日=========================
        invalid_msg_date = Row(
            [
                ft.Text("日付の形式がyyyy/mm/ddではない、または存在しない日付です。",
                        size=20, color=ft.colors.RED_500
                        )
            ],
            visible=False
        )

        def change_date(e):
            # invalid_msg_date.visible = False
            if len(date_textfield.value) != 10:
                return
            is_exist_date = False
            try:
                date_split_slush = date_textfield.value.split('/')
                if len(date_split_slush) != 3:
                    invalid_msg_date.visible = True
                else:
                    # 存在日付チェック
                    new_data_str = "%04s/%02s/%02s" % (
                        date_split_slush[0], date_split_slush[1], date_split_slush[2])
                    datetime.datetime.strptime(new_data_str, "%Y/%m/%d")
                    is_exist_date = True
                    if is_exist_date:
                        invalid_msg_date.visible = False
            except:
                invalid_msg_date.visible = True
            update_disable_submit_button()
            page.update()

        date_textfield = ft.TextField(
            height=50,
            cursor_height=20,
            width=300,
            label="yyyy/mm/dd",
            on_change=change_date)

        # 開始時間・終了時間=========================
        invalid_msg_datetime = Row(
            [
                ft.Text("開始時刻と終了時刻の前後関係が正しくありません",
                        size=20, color=ft.colors.RED_500
                        )
            ],
            visible=False
        )

        def change_start_end_time():
            invalid_msg_datetime.visible = False
            for t in [start_hour, start_minute, end_hour, end_minute]:
                # print(t.value)
                if t.value is None:
                    return
            if int(start_hour.value) > int(end_hour.value):
                invalid_msg_datetime.visible = True
            else:
                if int(start_minute.value) > int(end_minute.value):
                    invalid_msg_datetime.visible = True
            page.update()

        start_hour = ft.Text()
        end_hour = ft.Text()
        start_hour_arr = []
        end_hour_arr = []

        def start_hour_dropdown_changed(e):
            start_hour.value = start_hour_dd.value
            page.update()
            change_start_end_time()

        def end_hour_dropdown_changed(e):
            end_hour.value = end_hour_dd.value
            page.update()
            change_start_end_time()

        for i in range(1, 25):
            start_hour_arr.append(ft.dropdown.Option(str(i).zfill(2)))  # 0埋め
            end_hour_arr.append(ft.dropdown.Option(str(i).zfill(2)))  # 0埋め
        start_hour_dd = ft.Dropdown(
            on_change=start_hour_dropdown_changed,
            bgcolor=ft.colors.BLUE_200,
            options=start_hour_arr,
            width=75,
        )
        end_hour_dd = ft.Dropdown(
            on_change=end_hour_dropdown_changed,
            bgcolor=ft.colors.BLUE_200,
            options=end_hour_arr,
            width=75,
        )

        start_minute = ft.Text()
        end_minute = ft.Text()
        start_minute_arr = []
        end_minute_arr = []

        def start_minute_dropdown_changed(e):
            start_minute.value = start_minute_dd.value
            page.update()
            change_start_end_time()

        def end_minute_dropdown_changed(e):
            end_minute.value = end_minute_dd.value
            page.update()
            change_start_end_time()

        for i in ['00', '15', '30', '45']:
            start_minute_arr.append(ft.dropdown.Option(i))
            end_minute_arr.append(ft.dropdown.Option(i))
        start_minute_dd = ft.Dropdown(
            on_change=start_minute_dropdown_changed,
            bgcolor=ft.colors.BLUE_200,
            options=start_minute_arr,
            width=75,
        )
        end_minute_dd = ft.Dropdown(
            on_change=end_minute_dropdown_changed,
            bgcolor=ft.colors.BLUE_200,
            options=end_minute_arr,
            width=75,
        )

        # 公開設定=========================
        is_public = ft.Switch(label="", value=False,)  # False：下書き状

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
                "Success! Create Seminar!",
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

        # Submitボタン=========================
        submit_button = ft.ElevatedButton(
            disabled=True,
            text="Submit", on_click=open_dlg_modal)

        lv = ft.ListView(expand=True, spacing=15, auto_scroll=False)
        lv.controls.append(
            Column(
                [
                    Container(content=Text("セミナー追加", size=32),
                              margin=ft.margin.symmetric(horizontal=20,
                                                         vertical=5)),
                    Container(content=Text("セミナー名・概要", size=20),
                              margin=ft.margin.symmetric(horizontal=20,)
                              ),
                    Container(content=Column(
                        [seminar_name_textfield, description_textfield]
                    ),
                        margin=ft.margin.symmetric(horizontal=30, vertical=5)
                    ),
                    Container(content=invalid_msg_seminar_name_description,
                              margin=ft.margin.symmetric(
                                  horizontal=30)
                              ),
                    Container(content=Text("ジャンル選択", size=20),
                              margin=ft.margin.symmetric(horizontal=20,)
                              ),
                    Container(content=Column([dd]),
                              margin=ft.margin.symmetric(
                        horizontal=30, vertical=5)
                    ),
                    Container(content=Text("参加人数", size=20),
                              margin=ft.margin.symmetric(horizontal=20,)
                              ),
                    Container(
                        content=participates_textfield,
                        margin=ft.margin.only(
                            left=30, top=10)
                    ),
                    Container(content=invalid_msg_participates,
                              margin=ft.margin.symmetric(
                                  horizontal=30)
                              ),
                    Container(content=Text("開催日", size=20),
                              margin=ft.margin.symmetric(horizontal=20,)
                              ),
                    Container(content=date_textfield,
                              margin=ft.margin.only(
                                  left=30, top=10)
                              ),
                    Container(content=invalid_msg_date,
                              margin=ft.margin.symmetric(
                                  horizontal=30)
                              ),
                    Container(
                        content=Row(
                            [
                                start_hour_dd, Text(
                                    ':', weight=ft.FontWeight.W_500, size=18),
                                start_minute_dd,
                                Text(' ~ ', weight=ft.FontWeight.W_500, size=18),
                                end_hour_dd, Text(
                                    ':', weight=ft.FontWeight.W_500, size=18),
                                end_minute_dd
                            ]
                        ),
                        margin=ft.margin.symmetric(
                            horizontal=30, vertical=5)
                    ),
                    Container(content=invalid_msg_datetime,
                              margin=ft.margin.symmetric(
                                  horizontal=30)
                              ),
                    Container(content=Text("公開設定", size=20),
                              margin=ft.margin.symmetric(horizontal=20,)
                              ),
                    Container(content=Text("選択：公開 / 非選択：下書き", size=14),
                              margin=ft.margin.symmetric(horizontal=30,)
                              ),
                    Container(content=is_public,
                              margin=ft.margin.symmetric(
                                  horizontal=30)
                              ),
                    Container(content=submit_button,
                              margin=ft.margin.only(right=25, bottom=25),
                              alignment=ft.alignment.center_right
                              ),
                ],
            ))
        # 表示内容
        contents.controls.append(lv)

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
