from copy import deepcopy

import flet as ft
from flet import (
    AppBar,
    Card,
    Column,
    Container,
    ElevatedButton,
    IconButton,
    NavigationRail,
    NavigationRailDestination,
    Page,
    Row,
    Stack,
    Switch,
    Text,
    VerticalDivider,
    colors,
    icons
)
from flet.utils import slugify


class ResponsiveMenuLayout(Row):
    def __init__(
        self,
        page: Page,
        pages,
        *args,
        support_routes=True,
        menu_extended=True,
        minimize_to_icons=False,
        landscape_minimize_to_icons=False,
        portrait_minimize_to_icons=False,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page
        self.page.window_width = 700
        self.pages = pages

        self._minimize_to_icons = minimize_to_icons
        self._landscape_minimize_to_icons = landscape_minimize_to_icons
        self._portrait_minimize_to_icons = portrait_minimize_to_icons
        self._support_routes = support_routes
        self.expand = True
        self.navigation_items = [
            navigation_item for navigation_item, _ in pages]
        # slugify：'Menu in landscape' to 'menu-in-landscape'
        self.routes = [
            f"/{item.pop('route', None) or slugify(item['label'])}"
            for item in self.navigation_items
        ]
        self.navigation_rail = self.build_navigation_rail()
        self.update_destinations()
        self._menu_extended = menu_extended
        self.navigation_rail.extended = menu_extended
        page_contents = [page_content for _, page_content in pages]
        self.menu_panel = Row(
            controls=[self.navigation_rail, VerticalDivider(width=1)],
            spacing=0,
            tight=True,
        )

        self.content_area = Column(page_contents, expand=True)
        self._was_portrait = self.is_portrait()
        self._panel_visible = self.is_landscape()

        self.set_navigation_content()

        # supports_routes：多分ルーティングの検知をサポートするか、ってために用意した変数かと。
        if support_routes:
            self._route_change(page.route)
            self.page.on_route_change = self._on_route_change
        self._change_displayed_page()

        self.page.on_resize = self.handle_resize

    def select_page(self, page_number):
        # タブから各ページ選択
        self.navigation_rail.selected_index = page_number
        self._change_displayed_page()

    @property
    def minimize_to_icons(self) -> bool:
        return self._minimize_to_icons or (
            self._landscape_minimize_to_icons and self._portrait_minimize_to_icons
        )

    @minimize_to_icons.setter
    def minimize_to_icons(self, value: bool):
        self._minimize_to_icons = value
        self.set_navigation_content()

    @property
    def landscape_minimize_to_icons(self) -> bool:
        return self._landscape_minimize_to_icons or self._minimize_to_icons

    @landscape_minimize_to_icons.setter
    def landscape_minimize_to_icons(self, value: bool):
        self._landscape_minimize_to_icons = value
        self.set_navigation_content()

    @property
    def portrait_minimize_to_icons(self) -> bool:
        return self._portrait_minimize_to_icons or self._minimize_to_icons

    @portrait_minimize_to_icons.setter
    def portrait_minimize_to_icons(self, value: bool):
        self._portrait_minimize_to_icons = value
        self.set_navigation_content()

    @property
    def menu_extended(self) -> bool:
        return self._menu_extended

    @menu_extended.setter
    def menu_extended(self, value: bool):
        self._menu_extended = value

        dimension_minimized = (
            self.landscape_minimize_to_icons
            if self.is_landscape()
            else self.portrait_minimize_to_icons
        )
        if not dimension_minimized or self._panel_visible:
            self.navigation_rail.extended = value

        # タブ切り替えで実行
    def _navigation_change(self, e):
        # 画面の表示内容更新
        self._change_displayed_page()
        # self.check_toggle_on_select()
        self.page.update()

    def _change_displayed_page(self):
        # 以下の実装のような形にしてもいいかもしれない
        #   if troute.match("/"):
        #     self.page.go("/boards")
        # elif troute.match("/board/:id"):
        #     if int(troute.id) > len(self.store.get_boards()):
        #         self.page.go("/")
        #         return
        #     self.layout.set_board_view(int(troute.id))
        # elif troute.match("/boards"):
        #     self.layout.set_all_boards_view()
        # elif troute.match("/members"):
        #     self.layout.set_members_view()
        # self.page.update()
        # クリックしたタブに合わせて表示内容更新
        page_number = self.navigation_rail.selected_index
        # ここはタブを変える度に実行できるから、ここでデータ取得する処理を入れ
        if self._support_routes:
            self.page.route = self.routes[page_number]
            if (page_number == 1):
                pass
                # print(self.content_area.controls[-1])
            if (page_number == 2):
                pass
                # self.content_area.controls[-1] = Text("Update")
        for i, content_page in enumerate(self.content_area.controls):
            content_page.visible = page_number == i

    def _route_change(self, route):
        print(route)
        try:
            page_number = self.routes.index(route)
        except ValueError:
            page_number = 0
        # print(page_number)

        self.select_page(page_number)

    def _on_route_change(self, event):
        self._route_change(event.route)
        self.page.update()

    # initで定義するだけ
    def build_navigation_rail(self):
        # print("build_navigation_rail")
        return NavigationRail(
            selected_index=0,
            label_type="none",
            on_change=self._navigation_change,
        )

    def update_destinations(self, icons_only=False):
        # icons_only:Trueならiconと文字列をセットで表示
        # Minimize to iconsのトグルクリック時のイベント
        navigation_items = self.navigation_items
        if icons_only:
            navigation_items = deepcopy(navigation_items)
            for item in navigation_items:
                item.pop("label")

        self.navigation_rail.destinations = [
            NavigationRailDestination(**nav_specs) for nav_specs in navigation_items
        ]
        # self.navigation_rail.label_type = "none" if icons_only else "all"

    def handle_resize(self, e):
        if self._was_portrait != self.is_portrait():
            self._was_portrait = self.is_portrait()
            self._panel_visible = self.is_landscape()
            self.set_navigation_content()
            self.page.update()

    # appbarのアイコンクリック時のアクション
    def toggle_navigation(self, event=None):
        self._panel_visible = not self._panel_visible
        self.set_navigation_content()
        self.page.update()

    # トグル選択時のアクション
    def check_toggle_on_select(self):
        # self._panel_visible：アイコン下の文字が見えるときTrue
        if self.is_portrait() and self._panel_visible:
            self.toggle_navigation()

    # ナビゲーションの表示形式を決める
    def set_navigation_content(self):
        if self.is_landscape():
            self.add_landscape_content()
        else:
            self.add_portrait_content()

    '''
    高さと幅に関する処理
    '''
    # 画面の幅 > 高さのとき

    def add_landscape_content(self):
        self.controls = [self.menu_panel, self.content_area]
        if self.landscape_minimize_to_icons:
            self.update_destinations(icons_only=not self._panel_visible)
            self.menu_panel.visible = True
            if not self._panel_visible:
                self.navigation_rail.extended = False
            else:
                self.navigation_rail.extended = self.menu_extended
        else:
            self.update_destinations()
            self.navigation_rail.extended = self._menu_extended
            self.menu_panel.visible = self._panel_visible

    # 画面の幅 < 高さのとき
    def add_portrait_content(self):
        if self.portrait_minimize_to_icons and not self._panel_visible:
            self.controls = [self.menu_panel, self.content_area]
            self.update_destinations(icons_only=True)
            self.menu_panel.visible = True
            self.navigation_rail.extended = False
        else:
            if self._panel_visible:
                dismiss_shield = Container(
                    expand=True,
                    on_click=self.toggle_navigation,
                )
                self.controls = [
                    Stack(
                        controls=[self.content_area,
                                  dismiss_shield, self.menu_panel],
                        expand=True,
                    )
                ]
            else:
                self.controls = [
                    Stack(controls=[self.content_area,
                          self.menu_panel], expand=True)
                ]
            self.update_destinations()
            self.navigation_rail.extended = self.menu_extended
            self.menu_panel.visible = self._panel_visible

    # 縦長の状態か判定
    def is_portrait(self) -> bool:
        # Return true if window/display is narrow
        # return self.page.window_height >= self.page.window_width
        return self.page.height >= self.page.width

    # 横長の状態か判定
    def is_landscape(self) -> bool:
        # Return true if window/display is wide
        return self.page.width > self.page.height
