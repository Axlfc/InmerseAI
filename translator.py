from googletrans import Translator  # pip install googletrans==4.0.0-rc1
import lang_detect
import sys


def translate(text, dest_lang="en"):
    translator = Translator()
    result = translator.translate(text, src=lang_detect.detect_language(text), dest=ensure_language_concordance(dest_lang)).text
    return result


def ensure_language_concordance(lang):
    if lang == "pt-PT":
        return "pt"
    elif lang == "pt-BR":
        return "pt"
    elif lang == "pt":
        return "pt"
    elif lang == "tl":
        return "es"
    elif lang in lang_detect.langs():
        return lang
    else:
        print("ERROR: Language not recognized.")
        print("AVAILABLE LANGUAGES:")
        print(lang_detect.langs())


def main():
    my_text = sys.argv[1]
    dest_lang = sys.argv[2]

    print(translate(my_text, dest_lang))


if __name__ == '__main__':
    main()

