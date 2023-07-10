from flet import *
import flet as ft
import threading


class State:
    i = 0


s = State()
sem = threading.Semaphore()  # What is This???


class ScrollCardListInfinite():
    def __init__(
        self,
        page: Page,
        contents: Column,
        * args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.page = page

        def my_scroll(e: ft.OnScrollEvent):
            # print(f'e.pixels:{e.pixels}')
            # print(f'e.max_scroll_extent:{e.max_scroll_extent}')
            # e.max_scroll_extent:MAXでスクロールできるピクセル数
            if e.pixels >= e.max_scroll_extent - 100:
                # さらにスクロールされたら、追加で10個表示する感じみたい
                if sem.acquire(blocking=False):
                    try:
                        for _ in range(1, 10):
                            lv.controls.append(
                                ft.Card(
                                    content=Container(
                                        content=ft.Column(
                                            [
                                                ft.ListTile(
                                                    leading=ft.Icon(
                                                        ft.icons.ALBUM),
                                                    title=ft.Text(
                                                        "The Enchanted Nightingale"),
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
                                )
                            )
                            s.i += 1
                            lv.update()
                    finally:
                        sem.release()

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

        contents.controls.append(lv)
        contents.on_scroll = my_scroll

# Column > Container > Column > Container
# https://www.youtube.com/watch?v=Zx4m5-m8Fs4
