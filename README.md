# InmerseAI
Inmerse AI chatbot terminal port for Inmers 

# Set up dependencies:
- Install Mozilla Firefox
- Install python3
- Install python3 dependencies:

## GNU/Linux

<code>pip3 install colorama python-dotenv selenium langdetect googletrans==4.0.0-rc1</code>

## Windows
<code>pip install colorama python-dotenv selenium langdetect googletrans==4.0.0-rc1</code>

# Usage:
Run in the repository folder:

## GNU/Linux

<code>python3 inmerse.py</code>

## Windows

<code>python inmerse.py</code>

# Inmers_talk

## Windows

<code>pip install gtts pipwin</code>
<code>pipwin install pyaudio</code>

## GNU/Linux

<code>sudo apt-get install -y libasound-dev portaudio19-dev ffmpeg</code>
<code>pip3 install gtts pyaudio</code>

# Usage:
Run in the repository folder:

## GNU/Linux

<code>python3 inmerse_talk.py</code>

## Windows

<code>python inmerse_talk.py</code>

## TODO:
- [ ] Get rid of ugly output from ALSA lib.