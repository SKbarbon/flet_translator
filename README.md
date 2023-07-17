# flet_translator

**flet_tranlator**, An easy-to-use package for make your flet app support multiple languages without effecting any of your original flet code! Code your app in your native language like for example German, then with one simple line of code your app will be ready in any of your target language, English, France or Arabic you say it!!.

## Installation

You can install `flet_translator` using pip:

```bash
pip install flet_translator --upgrade
```

## Example and Usage
There is two modes of translation with this package. The first one is with `use_internet = True`, this will use Google Translation API for all translation requests. The second one is with `use_internet = False` this will use a local Machine learning translation model for all translation requests.


This is an example usage of using `TranslateFletPage` class with Google translation API:
```python
from flet_translator import TranslateFletPage, GoogleTranslateLanguage
import flet

def main(page: flet.Page):
    # Create a TranslateFletPage instance
    tp = TranslateFletPage(page=page, into_language=GoogleTranslateLanguage.turkish, use_internet=True)

    c = flet.Container(content=flet.Text("I will be Turkish!"))
    page.add(c)

    # This will update the translations and page at the same time.
    tp.update()


flet.app(target=main)
```

This is an example of using `TranslateFletPage` class with local translation model:
```python
from flet_translator import TranslateFletPage, OpusmtLanguage
import flet

def main (page:flet.Page):
    # Create a TranslateFletPage instance
    tp = TranslateFletPage(page=page, into_language=OpusmtLanguage.ar, use_internet=False)

    c = flet.Container(content=flet.Text("I will be Arabic!"))
    page.add(c)
    
    # This will update the translations and page at the same time.
    tp.update()

flet.app(target=main)
```
Its really simple and easy 😃!

## `TranslateFletPage` properties
- `use_internet` (You can set this once with the --init--): If you set this to `True`, then all translation requests will be using Google translation API. But if you set it to `False` then all the translation requests will be using the local machine learning that trained for translating.
- `from_language`: The main language, the language that are the contents written with. With `use_internet = True` you can set this to `GoogleTranslateLanguage.auto`.
- `skiped_controls.append (control)`: A property list containing all controls you choose that will be skipped as they will not be translated.
- `into_language`: The target langauge, the language that the app should be translated to.
- `activate_google_translation()`: A function property for switching the translation mode into `use_internet = True`.
- `activate_local_ML_translation()`: A function property for switching the translation mode into `use_internet = False`.

# suggestions
While using Google API for translating can be stable if you have a stable internet, trusted results and fast. But it needs internet, also google servers may give you a temporarily block if you did spam the translation requests.

The local ML translation model is also can be reliable and fast and super stable. But it takes a storage in the client side, also it need a device performence for translating the app.

So the best choice for you can depend on the project app needs and requirements. I think if your flet app is a website and it run on a server side, then using the local machine learning will be much better as your server is have a good performence and will expect multiple translation requests.