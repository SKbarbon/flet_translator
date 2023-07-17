


def translate_using_opusMT (Translatemodel, src:str, from_language, into_language):
    try:
        from easynmt import EasyNMT
    except:
        raise ImportError("Please install the easynmt package:\npip install EasyNMT")
    if from_language == "auto":
        r = Translatemodel.translate(src, target_lang=into_language, 
                                    perform_sentence_splitting=True)
    else:
        r = Translatemodel.translate(src, target_lang=into_language, source_lang=from_language, 
                                 perform_sentence_splitting=True)
    
    return str(r)


if __name__ == "__main__":
    from easynmt import EasyNMT
    model = EasyNMT('opus-mt')