from flet_translator import TranslateFletPage, GoogleTranslateLanguage, OpusmtLanguage
import flet

async def main(page:flet.Page):
    tp = TranslateFletPage(page=page, into_language=GoogleTranslateLanguage.arabic, use_internet=True)
    
    t = flet.Text("Hello, world!")
    await page.add_async(t)

    await tp.update_async()
    print("Done")
    await tp.update_async()

flet.app(target=main)