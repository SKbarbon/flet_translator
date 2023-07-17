from flet_translator import TranslateFletPage, GoogleTranslateLanguage
import flet as ft

def main(page: ft.Page):
    tp = TranslateFletPage(page=page, use_internet=True, into_language=GoogleTranslateLanguage.arabic)
    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Text("This is Tab 1")
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )
    ft.Text()

    page.add(t)
    tp.update()

ft.app(target=main)