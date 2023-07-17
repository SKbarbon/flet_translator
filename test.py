from flet_translator import TranslateFletPage, GoogleTranslateLanguage, OpusmtLanguage
import flet

def main (page:flet.Page):
    tp = TranslateFletPage(page=page, into_language=OpusmtLanguage.ar, use_internet=False)

    c = flet.Container(content=flet.Text("I will be Arabic!"))
    page.add(c)
    
    tp.update()

flet.app(target=main)