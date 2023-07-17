from flet_translator import TranslateFletPage, GoogleTranslateLanguage
import flet as ft

def main(page):
    tp = TranslateFletPage(page=page, into_language=GoogleTranslateLanguage.arabic)
    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Oops, there were some errors while trying to delete the file. What would you like me to do?"
        ),
        actions=[
            ft.TextButton("Retry", on_click=close_banner),
            ft.TextButton("Ignore", on_click=close_banner),
            ft.TextButton("Cancel", on_click=close_banner),
        ],
    )

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    page.add(ft.ElevatedButton("Show Banner", on_click=show_banner_click))
    
    tp.update()

ft.app(target=main)