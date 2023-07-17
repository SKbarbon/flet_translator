from deep_translator import GoogleTranslator



def translate_using_google (src:str, from_language:str, into_language:str):
    sents = []
    
    current_sent = ""
    num = 0
    for i in src:
        if num >= 250:
            sents.append(current_sent)
            current_sent = ""
            num = 0
        current_sent = current_sent + i
        num = num + 1
    
    sents.append(current_sent)
    res = GoogleTranslator(source=from_language, target=into_language).translate_batch(sents)

    full_res = ""
    for i in res:
        full_res = full_res + i

    return str(full_res)