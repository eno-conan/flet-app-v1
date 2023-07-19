# import ssl
from card_list_infinite import ScrollCardListInfinite
from card_list import ScrollSeminarList
from _temp_view import TempView
from setting_contents import SettingContents
from add_form import AddForm
from _members_view import MembersView
from top import Top
from time import sleep
from flet import (
    ButtonStyle,
    Column,
    Container,
    Control,
    Page,
    Row,
    Text,
    padding,
    Stack
)
import requests
from sidebar import Sidebar
import urllib3
import flet as ft
import json
import os
from dotenv import load_dotenv
load_dotenv()


class AppLayout(Row):
    def __init__(
        self, app,
        page: Page,
        menu_extended=True,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        # self.page = page.auth
        print(self.page.auth)
        # print(page.session.get("auth"))
        self.sidebar = Sidebar(self, page)
        self._was_portrait = self.is_portrait()
        self._panel_visible = self.is_landscape()
        self.expand = True
        self._menu_extended = menu_extended
        self.page.on_resize = self.handle_resize
        # self.navigation_rail.extended = menu_extended

        self._active_view = self.fetch_data_top_view()
        # self.top_view = top_view_obj.get_content()

        # Members View
        members_view_obj = MembersView(page)
        self.members_view = members_view_obj.get_content()

        # Seminars View
        seminars_view_obj = ScrollSeminarList(page)
        self.seminars_view = seminars_view_obj.get_content()

        # Add Seminar Form
        add_form_view_obj = AddForm(page)
        self.add_form_view = add_form_view_obj.get_content()

        # Setting View
        setting_view_obj = SettingContents(page)
        self.setting_view = setting_view_obj.get_content()

        # Temp View
        temp_view_obj = TempView(page)
        self.temp_view = temp_view_obj.get_content()

        self.controls = [self.sidebar, self.active_view]

    @ property
    def active_view(self):
        return self._active_view

    @ active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.controls[-1] = self._active_view
        self.sidebar.sync_board_destinations()
        self.update()

    def fetch_data_top_view(self):
        try:
            # url = os.getenv('WORKERS_URL')
            # response = requests.get(url)
            # result = response.json()
            print("Dummy Data")
            result = [{'CustomerId': 1, 'CompanyName': 'Alfreds Futterkiste', 'ContactName': 'Maria Anders'}, {'CustomerId': 2, 'CompanyName': 'Around the Horn', 'ContactName': 'Thomas Hardy'}, {
                'CustomerId': 3, 'CompanyName': 'Bs Beverages', 'ContactName': 'Victoria Ashworth'}, {'CustomerId': 4, 'CompanyName': 'Bs Beverages', 'ContactName': 'Random Name'}]
            top_view_obj = Top(self.page, result)
            return top_view_obj.get_content()
        except Exception as e:
            print(e)
            return None

    # top view
    def set_top_view(self):
        # self.active_view = self.top_view
        self.active_view = self.fetch_data_top_view()
        self.hydrate_all_boards_view()
        self.sidebar.top_nav_rail.selected_index = 0
        self.sidebar.bottom_nav_rail.selected_index = None
        self.sidebar.update()
        self.page.update()

    # check seminars view
    def set_seminars_view(self):
        self.active_view = self.seminars_view
        self.sidebar.top_nav_rail.selected_index = 1
        self.sidebar.bottom_nav_rail.selected_index = None
        self.sidebar.update()
        self.page.update()

        # add seminar view
    def set_add_form_view(self):
        self.active_view = self.add_form_view
        self.sidebar.top_nav_rail.selected_index = 2
        self.sidebar.bottom_nav_rail.selected_index = None
        self.sidebar.update()
        self.page.update()

    def set_setting_view(self):
        self.active_view = self.setting_view
        # self.active_view = self.members_view
        self.sidebar.top_nav_rail.selected_index = 3
        self.sidebar.bottom_nav_rail.selected_index = None
        self.sidebar.update()
        self.page.update()

    # def temp_create_view(self):
    #     self.active_view = self.temp_view
    #     self.sidebar.top_nav_rail.selected_index = 5
    #     self.sidebar.bottom_nav_rail.selected_index = None
    #     self.sidebar.update()
    #     self.page.update()

    # ページサイズ更新時の処理
    def handle_resize(self, e):
        if self._was_portrait != self.is_portrait():
            self._was_portrait = self.is_portrait()
            self._panel_visible = self.is_landscape()
            self.set_navigation_content()
            self.page.update()

    # アイコンクリック時
    def toggle_navigation(self, event=None):
        self._panel_visible = not self._panel_visible
        self.set_navigation_content()
        self.page.update()

    # ナビゲーションの表示形式
    def set_navigation_content(self):
        if self.is_landscape():
            self.add_landscape_content()
        else:
            self.add_portrait_content()

    # 画面の幅 > 高さのとき
    def add_landscape_content(self):
        if self._panel_visible:
            self.controls = [self.sidebar, self.active_view]
        else:
            self.controls = [self.active_view]

    # 画面の高さ > 幅のとき
    def add_portrait_content(self):
        if self._panel_visible:
            self.controls = [
                Stack(
                    controls=[self.active_view,
                              self.sidebar],
                    expand=True,
                )
            ]
        else:
            self.controls = [self.active_view]

    # 縦長の状態か判定
    def is_portrait(self) -> bool:
        return self.page.height >= self.page.width

    # 横長の状態か判定
    def is_landscape(self) -> bool:
        return self.page.width > self.page.height

    def hydrate_all_boards_view(self):
        self.sidebar.sync_board_destinations()
