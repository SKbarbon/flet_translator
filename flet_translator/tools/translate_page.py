from ..utils.google_supported_langaues import GoogleTranslateLanguage
from ..utils.is_rtl import is_rtl_language
from ..tools.translate_control_content import translate_control_content
import flet, threading, os, asyncio


class TranslateFletPage:
    """
    This class will translate the whole page into a specific language. 
    The childs controls, page info (title, appbar, ..), etc..

    if `use_internet` is True (Which is not recomended for some cases), That mean
    the translate model is Google translate API, which may give you block band for spam requests.

    if `use_internet` is False, Thats mean the translate model is `opus-mt`, which is a
    local machine learning that trained for many popular languages. It works localy on the device,
    Its use the device performance. So it can lead to a heavy usage.
    """
    def __init__(self,
                page : flet.Page,
                use_internet = True,
                from_language = GoogleTranslateLanguage.auto, 
                into_language = GoogleTranslateLanguage.auto,
                skiped_controls = None
                ) -> None:
        
        self.page = page
        self.from_language = from_language
        self.into_language = into_language

        if isinstance(skiped_controls, list):
            self.skiped_controls = skiped_controls
        else:
            self.skiped_controls = []

        self.__use_internet = use_internet

        if use_internet == False:
            try:
                from easynmt import EasyNMT
            except:
                raise ImportError("Please install the easynmt package:\npip install EasyNMT")
            # store ML models
            self.opusMT_model = EasyNMT('opus-mt')

            # Activate the model to be faster in the second request.
            self.opusMT_model.translate(
                "Hi", 
                target_lang="en", 
                source_lang="en"
            )



    def translate_child_controls (self, update_in_async:bool):
        if self.page.appbar != None:
            translate_control_content(self, control=self.page.appbar, use_internet=self.__use_internet, update_async=update_in_async)

        if self.page.dialog != None:
            translate_control_content(self, control=self.page.dialog, use_internet=self.__use_internet, update_async=update_in_async)
        
        if self.page.banner != None:
            translate_control_content(self, control=self.page.banner, use_internet=self.__use_internet, update_async=update_in_async)
        
        if self.page.snack_bar != None:
            translate_control_content(self, control=self.page.snack_bar, use_internet=self.__use_internet, update_async=update_in_async)

        if update_in_async:
            for con in self.page.controls:
                translate_control_content(self, con, self.__use_internet, update_in_async)
        else:
            for con in self.page.controls:
                threading.Thread(
                    target=translate_control_content,
                    args=[self],
                    kwargs={
                        "control" : con,
                        "use_internet" : self.__use_internet,
                        "update_async" : update_in_async
                    }
                ).start()
    
    def activate_local_ML_translation (self):
        """This will activate the local machine learning model to be used in future translation requests"""
        try:
            from easynmt import EasyNMT
        except:
            raise ImportError("Please install the easynmt package:\npip install EasyNMT")
        self.__use_internet = False
        # store ML models
        self.opusMT_model = EasyNMT('opus-mt')

        # Activate the model to be faster in the second request.
        self.opusMT_model.translate(
            "Hi", 
            target_lang="en", 
            source_lang="en"
        )
    
    
    def activate_google_translation (self):
        """This will activate the google translation mode, so any future translation requests will be via google API"""
        self.__use_internet = True


    def update(self):
        """This will be called per page.update so it follow the page updates"""
        if is_rtl_language(language=str(self.into_language.value)):
            self.page.rtl = True
        else:
            self.page.rtl = False
        self.page.update()

        self.translate_child_controls(update_in_async=False)
        self.page.update()
    
    async def update_async (self):
        """This will be called per page.update so it follow the page updates"""
        if is_rtl_language(language=str(self.into_language.value)):
            self.page.rtl = True
        else:
            self.page.rtl = False
        await self.page.update_async()

        self.translate_child_controls(update_in_async=True)
        await self.page.update_async()