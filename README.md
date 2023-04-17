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


# Telegram bot:

#### Get Your Bot Token

- Search for @botfather in Telegram.
- Start a conversation with BotFather by clicking on the Start button.
- Type /newbot, and follow the prompts to set up a new bot. The BotFather will give you a token that you will use to authenticate your bot and grant it access to the Telegram API.
- Edit the `.env` file of this repository and set the `TELEGRAM_BOT_TOKEN=` variable to your token.


## Install python dependencies

<code>pip install python-dotenv pyTelegramBotAPI</code>

## Start telegram bot:

<code>python main.py</code>

## TODO:
- [ ] Get rid of ugly output from ALSA lib.