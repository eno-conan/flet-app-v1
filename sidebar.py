from flet import (
    UserControl,
    Column,
    Container,
    IconButton,
    Row,
    Text,
    IconButton,
    NavigationRail,
    NavigationRailDestination,
    TextField,
    alignment,
    border_radius,
    colors,
    icons,
    padding,
    margin,
)
import flet as ft


class Sidebar(UserControl):

    def __init__(self, app_layout, page):
        super().__init__()
        self.app_layout = app_layout
        self.nav_rail_visible = True
        self.top_nav_items = [
            NavigationRailDestination(
                label_content=Text("Top",size=16),
                label="Top",
                icon=ft.icons.HOUSE_OUTLINED,
                selected_icon=ft.icons.HOUSE,
            ),
            NavigationRailDestination(
                label_content=Text("New Customer",size=16),
                label="New Customer",
                icon=icons.PERSON,
                selected_icon=icons.PERSON
            ),
            NavigationRailDestination(
                label_content=Text("Add Form",size=16),
                label="Add Form",
                icon=ft.icons.ADD_BOX_OUTLINED,
                selected_icon=ft.icons.ADD_BOX,
            ),
            NavigationRailDestination(
                label_content=Text("Setting Account",size=16),
                label="Setting Account",
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
            ),
        ]
        self.top_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor=colors.BLUE_GREY_100,
            extended=True,
            height=200
        )
        self.bottom_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.bottom_nav_change,
            extended=True,
            expand=True,
            bgcolor=colors.BLUE_GREY_100,
        )
        self.toggle_nav_rail_button = IconButton(icons.ARROW_BACK)

    def build(self):
        self.view = Container(
            content=Column([
                Row([
                    Text("Contents",weight=ft.FontWeight.W_500,size=20),
                ], alignment="spaceBetween"),
                # divider
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=220
                ),
                self.top_nav_rail,
                # divider
                # Container(
                #     bgcolor=ft.colors.BLACK26,
                #     border_radius=border_radius.all(30),
                #     height=1,
                #     alignment=alignment.center_right,
                #     width=220
                # ),
                self.bottom_nav_rail,
            ], tight=True),
            padding=padding.all(15),
            margin=margin.all(0),
            width=250,
            expand=True,
            bgcolor=colors.BLUE_GREY_100,
            visible=self.nav_rail_visible,
        )
        return self.view

    def sync_board_destinations(self):
        self.bottom_nav_rail.destinations = []
        self.view.update()

    def toggle_nav_rail(self, e):
        self.view.visible = not self.view.visible
        self.view.update()
        self.page.update()

    def top_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.bottom_nav_rail.selected_index = None
        self.top_nav_rail.selected_index = index
        self.view.update()
        if index == 0:
            self.page.route = "/top"
        elif index == 1:
            self.page.route = "/seminars"
        elif index == 2:
            self.page.route = "/add-form"
        elif index == 3:
            self.page.route = "/setting-account"
        self.page.update()

    def bottom_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.top_nav_rail.selected_index = None
        self.bottom_nav_rail.selected_index = index
        self.page.route = f"/board/{index}"
        self.view.update()
        self.page.update()
