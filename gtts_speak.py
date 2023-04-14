import os
import sys
import playaudio
import lang_detect
from gtts import gTTS  # pip install gtts


def load_audio_file(audio):
    return playaudio.load_audio_file(audio)


def open_audio_file(audio):
    playaudio.open_audio_file(audio)


def play_audio(audio):
    playaudio.play_audio(audio)


def generate_audiofile(audiofile_name, mytext, language='en'):
    gTTS(text=mytext, lang=language, slow=False).save(audiofile_name)


def detect_language(text):
    if lang_detect.detect_language(text) == "pt":
        return "pt"
    if lang_detect.detect_language(text) == "tl":
        return "es"
    elif lang_detect.detect_language(text) not in lang_detect.langs():
        return "en"
    else:
        return lang_detect.detect_language(text)


def speak(text):
    mp3_file = "inmers.mp3"
    wav_file = "inmers.wav"
    generate_audiofile(mp3_file, text, detect_language(text))
    playaudio.convert_mp3_to_wav(mp3_file, wav_file)
    play_audio(wav_file)
    os.remove(wav_file)
    os.remove(mp3_file)


def say(text):
    speak(text)


def main():
    say(sys.argv[1])


if __name__ == '__main__':
    main()
