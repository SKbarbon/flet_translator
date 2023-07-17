from easynmt import EasyNMT



def translate_using_opusMT (Translatemodel:EasyNMT, src:str, from_language, into_language):

    if from_language == "auto":
        r = Translatemodel.translate(src, target_lang=into_language, 
                                    perform_sentence_splitting=True)
    else:
        r = Translatemodel.translate(src, target_lang=into_language, source_lang=from_language, 
                                 perform_sentence_splitting=True)
    
    return str(r)


if __name__ == "__main__":
    model = EasyNMT('opus-mt')