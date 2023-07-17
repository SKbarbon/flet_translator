from ..utils.allowed_props_to_translate import allowed_props_to_translate
from ..tools.translate_using_google import translate_using_google
from ..tools.translate_using_opusMT import translate_using_opusMT
import flet, threading


def translate_control_content (TranslateFletPage_class, control:flet.Control, use_internet:bool=True):
    """
    This function translate the control content.

    It create an attr (last_translated_texts:dict) in the control that stores the last translated
    texts so it reduces unnecessary translation requests.
    """
    
    # Check if the control is skiped so not translate it.
    if control in TranslateFletPage_class.skiped_controls: return

    # start translating the control
    for p in allowed_props_to_translate:
        if hasattr(control, str(p)):
            value = getattr(control, str(p))
            if use_internet and value != None:
                r = translate_using_google(
                    src=value, 
                    from_language=TranslateFletPage_class.from_language.value,
                    into_language=TranslateFletPage_class.into_language.value
                )
                setattr(control, str(p), str(r))
            
            elif use_internet == False and value != None:
                r = translate_using_opusMT(
                    Translatemodel=TranslateFletPage_class.opusMT_model,
                    src=value,
                    from_language=TranslateFletPage_class.from_language.value,
                    into_language=TranslateFletPage_class.into_language.value
                )
                setattr(control, str(p), str(r))



    sub_controls_names = ["controls", "tabs", "actions"]
    for i in sub_controls_names:
        if hasattr(control, i):
            for i in getattr(control, str(i)):
                threading.Thread(target=translate_control_content, kwargs={
                    "TranslateFletPage_class" : TranslateFletPage_class,
                    "control" : i,
                    "use_internet" : use_internet
                }, daemon=True).start()
                # translate_control_content(TranslateFletPage_class, i, use_internet)
    
    sub_contents_names = ["content", "leading", "title"]
    for ic in sub_contents_names:
        if hasattr(control, ic):
            threading.Thread(target=translate_control_content, kwargs={
                        "TranslateFletPage_class" : TranslateFletPage_class,
                        "control" : getattr(control, ic),
                        "use_internet" : use_internet
                    }, daemon=True).start()

    if control.page != None:
        control.update()