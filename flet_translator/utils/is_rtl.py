


def is_rtl_language (language:str):
    all_RTLs = [
        "arabic", "hebrew", "persian (farsi)", "pashto", "sindhi", "dhivehi",
        "kurdish (kurmanji)", "uyghur", "yiddish", "ar", "he", "fa", "ps", "sd", "dv",
        "ku", "ug", "yi"
    ]

    if str(language) in all_RTLs:
        return True
    
    return False