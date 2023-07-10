from flet import *
import flet as ft
import threading


class State:
    i = 0


s = State()
sem = threading.Semaphore()  # What is This???


def main(page: Page):

    def my_scroll(e: OnScrollEvent):
        print(f'e.pixels:{e.pixels}')
        print(f'e.max_scroll_extent:{e.max_scroll_extent}')
        # e.max_scroll_extent:MAXでスクロールできるピクセル数
        if e.pixels >= e.max_scroll_extent - 100:
            # さらにスクロールされたら、追加で10個表示する感じみたい
            if sem.acquire(blocking=False):
                try:
                    for _ in range(1, 10):
                        body.controls.append(
                            Container(
                                bgcolor="white",
                                border_radius=30,
                                margin=ft.margin.only(left=30, right=30),
                                padding=10,
                                content=Text(f'you data is {s.i}', size=20)
                            )
                        )
                        s.i += 1
                        body.update()
                finally:
                    sem.release()

    body = Column(
        width=page.window_width,
        height=500,
        scroll="always",
        on_scroll_interval=0,  # ??
        on_scroll=my_scroll

    )

    for _ in range(0, 20):
        body.controls.append(
            Container(
                bgcolor="white",
                border_radius=30,
                margin=ft.margin.only(left=30, right=30),
                padding=10,
                content=Text(f"you data - {s.i}", size=20)
            )
        )

        s.i += 1

    page.add(
        Column([
            Text("Infinity scroll", weight="bold", size=30),
            Container(bgcolor="blue", padding=10, content=body)
        ])
    )

# https://www.youtube.com/watch?v=Zx4m5-m8Fs4
