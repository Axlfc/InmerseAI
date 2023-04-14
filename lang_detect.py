from langdetect import detect, DetectorFactory  # pip install langdetect


def langs():
    return ["am", "ar", "eu", "bn", "en-GB", "pt-BR", "bg", "ca", "chr", "h", "cs", "da", "nl", "en", "et", "fil",
            "fi", "fr", "de", "el", "gu", "iw", "hi", "hu", "is", "id", "it", "ja", "kn", "ko", "lv", "lt", "ms",
            "ml", "mr", "no", "pl", "pt-PT", "ro", "ru", "sr", "zh-CN", "sk", "sl", "es", "sw", "sv", "ta", "te",
            "th", "zh-TW", "tr", "ur", "uk", "vi", "cy"]


def detect_language(text):
    DetectorFactory.seed = 0
    lang = detect(text)
    return lang


def is_same_language(first_text, second_text):
    first_lang = detect_language(first_text)
    second_lang = detect_language(second_text)
    return first_lang == second_lang


def main():
    pass


if __name__ == '__main__':
    main()
