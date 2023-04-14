import sys
import pyaudio  # WINDOWS: pip install pipwin  # pipwin install pyaudio
from pydub import AudioSegment  # pip install pydub
import wave
import platform
import os
import subprocess


def load_audio_file(audio):
    return wave.open(audio, 'rb')


def open_audio_file(audio):
    # Open the audio file
    my_audio = load_audio_file(audio)
    # Open the audio playback stream
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(my_audio.getsampwidth()),
        channels=my_audio.getnchannels(),
        rate=my_audio.getframerate(),
        output=True,
    )

    # Play the audio
    data = my_audio.readframes(1024)
    while data:
        stream.write(data)
        data = my_audio.readframes(1024)

    # Close the audio playback stream
    stream.stop_stream()
    stream.close()
    p.terminate()


def play_audio(audio):
    if platform.system() == "Windows":
        open_audio_file(audio)
    elif subprocess.check_output(['uname', '-o']).strip() == b'Android':
        command0 = "pulseaudio -D"
        command = "play " + sys.argv[1]
        command1 = "pulseaudio -k"
        os.system(command0)
        os.system(command)
        os.system(command1)
    else:
        open_audio_file(audio)


def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    # check if mp3 file exists
    if not os.path.exists(mp3_file_path):
        print("File not found: ", mp3_file_path)
        return

    # load mp3 file
    audio = AudioSegment.from_mp3(mp3_file_path)

    # export wav file
    audio.export(wav_file_path, format="wav")


def main():
    my_audio = sys.argv[1]
    play_audio(my_audio)


if __name__ == '__main__':
    main()
