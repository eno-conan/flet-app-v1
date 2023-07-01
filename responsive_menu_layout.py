from copy import deepcopy

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
from layout import ResponsiveMenuLayout
from time import sleep


if __name__ == "__main__":

    def main(page: Page, title="Basic Responsive Menu"):

        page.title = title

        menu_button = IconButton(icons.MENU)

        page.appbar = AppBar(
            title=Text(f"MyApp", size=32),
            leading=menu_button,
            center_title=True,
            leading_width=40,
            # bgcolor=colors.SURFACE_VARIANT,
            toolbar_height=70,
            bgcolor=ft.colors.LIME_500,
        )

        pages = [
            (
                dict(
                    icon=icons.LANDSCAPE_OUTLINED,
                    selected_icon=icons.LANDSCAPE,
                    label="Menu in landscape",
                ),
                create_page(
                    page,
                    "Menu in landscape",
                    "Menu in landscape is by default shown, side by side with the main content, but can be "
                    "hidden with the menu button.",
                ),
            ),
            (
                dict(
                    icon=icons.PORTRAIT_OUTLINED,
                    selected_icon=icons.PORTRAIT,
                    label="Menu in portrait",
                ),
                create_page(
                    page,
                    "Menu in portrait",
                    "Menu in portrait is mainly expected to be used on a smaller mobile device."
                    "\n\n"
                    "The menu is by default hidden, and when shown with the menu button it is placed on top of the main "
                    "content."
                    "\n\n"
                    "In addition to the menu button, menu can be dismissed by a tap/click on the main content area.",
                ),
            ),
            (
                dict(
                    icon=ft.icons.SETTINGS,
                    selected_icon=icons.INSERT_EMOTICON,
                    label="Setting Your Account",
                ),
                create_page(
                    page,
                    "Minimize to icons",
                    "ResponsiveMenuLayout has a parameter minimize_to_icons. "
                    "Set it to True and the menu is shown as icons only, when normally it would be hidden.\n"
                    "\n\n"
                    "Try this with the 'Minimize to icons' toggle in the top bar."
                    "\n\n"
                    "There are also landscape_minimize_to_icons and portrait_minimize_to_icons properties that you can "
                    "use to set this property differently in each orientation.",
                ),
            ),
        ]

        menu_layout = ResponsiveMenuLayout(page, pages)

        page.appbar.actions = [
            Row(
                [
                    # Text("Minimize\nto icons"),
                    # Container(
                    #     content=Switch(
                    #         on_change=lambda e: toggle_icons_only(menu_layout)),
                    #     margin=ft.margin.only(right=10)
                    # )
                    # Text("Menu\nwidth"),
                    # Switch(
                    #     value=True, on_change=lambda e: toggle_menu_width(menu_layout)
                    # ),
                ]
            )
        ]

        # Add Button
        # menu_layout.navigation_rail.leading = ElevatedButton(
        #     "Add", icon=icons.ADD, expand=True, on_click=lambda e: print("Add clicked")
        # )
        # page.scroll = "always"
        page.add(menu_layout)

        menu_button.on_click = lambda e: menu_layout.toggle_navigation()

    # main_contentsのレイアウトをこれで統一している
    def create_page(page: Page, title: str, body: str):
        if title == "Menu in landscape":
            # base
            contents = Column(expand=True,auto_scroll=False)
            # # page title
            contents.controls.append(ft.Text("一覧画面", size=30, weight="bold"),)
            # # contents
            lv = ft.ListView(expand=True, spacing=15, auto_scroll=False)
            for _ in range(15):
                lv.controls.append(ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.ALBUM),
                                    title=ft.Text("The Enchanted Nightingale"),
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
                        width=400,
                        padding=10,
                        margin=10
                    )
                ))
            # lv = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=False)
            # count = 1
            # for i in range(0, 60):
            #     lv.controls.append(ft.Text(f"Line {count}"))
            #     count += 1

            contents.controls.append(lv)

            return contents
        elif title == "Menu in portrait":
            # base
            contents = Column()

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
            # まとめ方が悪いのかもしれないけど、以下でまとめると、テキストフィールドに値を入力してもSubmitボタンが活性状態にならない
            # Container(Column(controls=[company_name_textfield,company_name_textfield]))
            contents.controls.append(company_name_textfield)
            contents.controls.append(contract_name_textfield)
            contents.controls.append(submit_button)

            return contents
            # page.add(lv) #今更だけど、page.addって何？
            # https://flet.dev/docs/guides/python/getting-started
        else:
            return Row(
                controls=[
                    Column(
                        horizontal_alignment="stretch",
                        controls=[
                            Card(content=Container(
                                Text(title, weight="bold"), padding=8)),
                            Text(body),
                        ],
                        expand=True,
                    ),
                ],
                expand=True
                # wrap=True, scroll="always", expand=True
            )

    # def toggle_icons_only(menu: ResponsiveMenuLayout):
    #     menu.minimize_to_icons = not menu.minimize_to_icons
    #     menu.page.update()

    # def toggle_menu_width(menu: ResponsiveMenuLayout):
    #     # Menu\nwidth：クリック時のイベント
    #     # トグルがONの状態のとき、アイコンの横にラベルが表示される
    #     menu.menu_extended = not menu.menu_extended
    #     menu.page.update()

    ft.app(target=main, port=8080, view=ft.WEB_BROWSER)
