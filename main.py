import telebot
from dotenv import load_dotenv
import os
from datetime import datetime
import requests
import random
import inmers
# import lang_detect
# import translator
import yaml
import re


# Load environment variables
load_dotenv()

# crear el bot
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))


# Function that returns the chat ID of a given message
def get_chat_id(message):
    """
    Returns the chat ID of the given Telegram message object.

    Args:
        message: A message object that contains the chat ID to be retrieved

    Returns:
        The chat ID of the given message
    """
    return message.chat.id


# Function that sends a chat action to a specific chat
def send_chat_action(chat_id, action_string):
    """
    Sends a chat action to the specified chat using the specified action string.

    Args:
        chat_id (int): The ID of the chat to send the action to.
        action_string (str): The string representing the action to send.
            Must be one of the following values: 'typing', 'upload_photo', 'record_video',
            'upload_video', 'record_audio', 'upload_audio', 'upload_document', or 'find_location'.

    Returns:
        None
    """
    bot.send_chat_action(chat_id, action_string)


# Function that sends a text message to a specific chat
def send_msg(chat_id, text):
    """
    Sends a text message to the specified chat.

    Args:
        chat_id (int): The ID of the chat to send the message to.
        text (str): The text of the message to send.

    Returns:
        None
    """
    bot.send_message(chat_id, text)


# Function that sends a reply message to a specific chat
def reply_msg(chat_id, text):
    """
    Sends a reply message to the specified chat.

    Args:
        chat_id (int): The ID of the chat to send the message to.
        text (str): The text of the reply message to send.

    Returns:
        None
    """
    bot.reply_to(chat_id, text)


# Function that edits the text of a message in a specific chat
def edit_msg(new_text, chat_id, message_id):
    """
    Edits the text of a message in the specified chat.

    Args:
        new_text (str): The new text to replace the old text with.
        chat_id (int): The ID of the chat where the message to be edited was sent.
        message_id (int): The ID of the message to be edited.

    Returns:
        None
    """
    bot.edit_message_text(new_text, chat_id, message_id)


# Function that forwards a message from one chat to another
def forward_msg(to_chat_id, from_chat_id, message_id):
    """
    Forwards a message from one chat to another.

    Args:
        to_chat_id (int): The ID of the chat to forward the message to.
        from_chat_id (int): The ID of the chat where the message to be forwarded was sent.
        message_id (int): The ID of the message to be forwarded.

    Returns:
        None
    """
    bot.forward_message(to_chat_id, from_chat_id, message_id)


# Function that sends a photo to a specific chat
def send_photo(image_path, chat_id):
    """
    Sends a photo to the specified chat.

    Args:
        image_path (str): The path to the image file to send.
        chat_id (int): The ID of the chat to send the photo to.

    Returns:
        None
    """
    photo = open(image_path, 'rb')
    bot.send_photo(chat_id, photo)


# Function that sends a photo by ID to a specific chat
def send_photo_by_id(image_id, chat_id):
    """
    Sends a photo by ID to the specified chat.

    Args:
        image_id (str): The ID of the photo to send.
        chat_id (int): The ID of the chat to send the photo to.

    Returns:
        None
    """
    bot.send_photo(chat_id, image_id)


# Function that sends an audio file to a specific chat
def send_audio(audio_path, chat_id):
    """
    Sends an audio file to the specified chat.

    Args:
        audio_path (str): The path to the audio file to send.
        chat_id (int): The ID of the chat to send the audio file to.

    Returns:
        None
    """
    audio = open(audio_path, 'rb')
    bot.send_audio(chat_id, audio)


# Function that sends an audio file by ID to a specific chat
def send_audio_by_id(audio_id, chat_id):
    """
   Sends an audio file by ID to the specified chat.

   Args:
       audio_id (str): The ID of the audio file to send.
       chat_id (int): The ID of the chat to send the audio file to.

   Returns:
       None
   """
    bot.send_audio(chat_id, audio_id)


# Function that sends an audio file with duration, performer, and title information to a specific chat
def send_audio_with_duration_performer_and_title(file_data, duration, performer, title, chat_id):
    """
    Sends an audio file with duration, performer, and title information to the specified chat.

    Args:
        file_data (bytes): The bytes of the audio file to send.
        duration (int): The duration of the audio file in seconds.
        performer (str): The name of the performer.
        title (str): The title of the audio file.
        chat_id (int): The ID of the chat to send the audio file to.

    Returns:
        None
    """
    bot.send_audio(chat_id, file_data, duration, performer, title)


# Function that sends a voice message to a specific chat
def send_voice(voice_path, chat_id):
    """
    Sends a voice message to the specified chat.

    Args:
        voice_path (str): The path to the voice message file to send.
        chat_id (int): The ID of the chat to send the voice message to.

    Returns:
        None
    """
    voice = open(voice_path, 'rb')
    bot.send_voice(chat_id, voice)


# Function that sends a voice message by ID to a specific chat
def send_voice_by_id(voice_id, chat_id):
    """
    Sends a voice message by ID to the specified chat.

    Args:
        voice_id (str): The ID of the voice message to send.
        chat_id (int): The ID of the chat to send the voice message to.

    Returns:
        None
    """
    bot.send_voice(chat_id, voice_id)


# Function that sends a document to a specific chat
def send_document(document_path, chat_id):
    """
    Sends a document to the specified chat using its file path.

    Args:
        document_path (str): The file path of the document.
        chat_id (int): The chat ID to send the document to.

    Returns:
        None
    """
    doc = open(document_path, 'rb')
    bot.send_document(chat_id, doc)


# Function that sends a document by ID to a specific chat
def send_document_by_id(document_id, chat_id):
    """
    Sends a document to the specified chat using its file ID.

    Args:
        document_id (str): The file ID of the document.
        chat_id (int): The chat ID to send the document to.

    Returns:
        None
    """
    bot.send_document(chat_id, document_id)


# Function that sends a sticker to a specific chat
def send_sticker(sticker_path, chat_id):
    """
    Sends a sticker to the specified chat using its file path.

    Args:
       sticker_path (str): The file path of the sticker.
       chat_id (int): The chat ID to send the sticker to.

    Returns:
       None
    """
    sti = open(sticker_path, 'rb')
    bot.send_sticker(chat_id, sti)


# Function that sends a sticker by ID to a specific chat
def send_sticker_by_id(sticker_id, chat_id):
    """
    Sends a sticker to the specified chat using its file ID.

    Args:
        sticker_id (str): The file ID of the sticker.
        chat_id (int): The chat ID to send the sticker to.

    Returns:
        None
    """
    bot.send_sticker(chat_id, sticker_id)


# Function that sends a video to a specific chat
def send_video(video_path, chat_id):
    """
    Sends a video to the specified chat using its file path.

    Args:
        video_path (str): The file path of the video.
        chat_id (int): The chat ID to send the video to.

    Returns:
        None
    """
    video = open(video_path, 'rb')
    bot.send_video(chat_id, video)


# Function that sends a video by ID to a specific chat
def send_video_by_id(video_id, chat_id):
    """
    Sends a video to the specified chat using its file ID.

    Args:
        video_id (str): The file ID of the video.
        chat_id (int): The chat ID to send the video to.

    Returns:
        None
    """
    bot.send_video(chat_id, video_id)


# Function that sends a videonote to a specific chat
def send_videonote(videonote_path, chat_id):
    """
    Sends a video note to the specified chat using its file path.

    Args:
        videonote_path (str): The file path of the video note.
        chat_id (int): The chat ID to send the video note to.

    Returns:
        None
    """
    videonote = open(videonote_path, 'rb')
    bot.send_video_note(chat_id, videonote)


# Function that sends a videonote by ID to a specific chat
def send_videonote_by_id(videonote_id, chat_id):
    """
    Sends a video note to the specified chat using its file ID.

    Args:
        videonote_id (str): The file ID of the video note.
        chat_id (int): The chat ID to send the video note to.

    Returns:
        None
    """
    bot.send_video_note(chat_id, videonote_id)


# Function that sends a location (latitude, longitude) to a specific chat
def send_location(lat, lon, chat_id):
    """
    Sends a location to the specified chat_id.

    Args:
        lat: The latitude of the location.
        lon: The longitude of the location.
        chat_id: The ID or username of the chat to send the location to.

    Returns:
        On success, the sent Message is returned. Returns None on failure.
    """
    bot.send_location(chat_id, lat, lon)


def get_character_greeting(character_name):
    """
    Returns the greeting message of a character.

    Args:
        character_name (str): the name of the character to retrieve the greeting from.

    Returns:
        str: the greeting message of the character.
    """
    # Read the context information from the character file
    character_filename = character_name + ".yaml"
    character_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "characters", character_filename)
    with open(character_file, "r") as f:
        character_data = yaml.safe_load(f)
    return character_data["greeting"]


@bot.message_handler(commands=['start', 'hello', 'hola'])
def send_welcome(message):
    """
    Handles messages containing the /start, /hello, or /hola commands and sends a welcome message to the user.

    Args:
        message: The message to handle.

    Returns:
        None
    """
    reply_msg(message, get_character_greeting("UnAI"))


# Handler for the /insult command
@bot.message_handler(commands=['insult'])
def handle_insult_command(message):
    """
    Handle the /insult command by insulting a user mentioned in the message.

    Args:
        message: the Telegram message object

    Returns:
        None
    """
    # Check if the command is followed by a mention of a user
    from_user = message.from_user.first_name
    try:
        to_user = re.findall('@\w+', message.text)[0]
        # Call the slap API and get a random slap message
        # Call the insult API and get the response
        response = to_user + " " + requests.get("https://insult.mattbas.org/api/insult").text

        # Send the insult as a message to the chat
        send_msg(get_chat_id(message), response)
    except Exception as e:
        reply_msg(message, "You have to mention someone to insult!")


# Handler for the /slap command
@bot.message_handler(commands=['slap'])
def handle_slap_command(message):
    """
    Handles the /slap command by checking if the command is followed by a mention of a user, calling the slap API to get
    a random slap message, formatting the slap message with the usernames, and sending the response as a message to the chat.

    Args:
        message (telegram.Message): The message object representing the command.

    Returns:
        None
    """
    # Check if the command is followed by a mention of a user
    from_user = message.from_user.first_name
    try:
        to_user = re.findall('@\w+', message.text)[0]
        # Call the slap API and get a random slap message
        slap_data = requests.get("https://axljuega.github.io/data/slap_data.txt").text
        slap_message = random.choice(slap_data.split('\n'))[1:-3]
        # Format the slap message with the usernames
        response = f"{from_user} ha abofeteado a {to_user} con {slap_message}."
        # Send the response as a message to the chat
        send_msg(get_chat_id(message), response)
    except Exception as e:
        reply_msg(message, "¡Tienes que mencionar a alguien a quien abofetear!")


# Handler for the /repeat command
@bot.message_handler(commands=['repeat'])
def repeat_message(message):
    """
    Repeats a message in the same chat and thread as the original message.

    Args:
        message (telebot.types.Message): The original message to repeat.

    Returns:
        None
    """
    # Remove the "/repeat " prefix from the message text
    text = message.text.split(' ', 1)[1]
    # Send the repeated message to the same chat and thread as the original message
    sent_message = bot.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id)
    # Add the message IDs to the list of repeated message IDs
    repeated_messages[message.message_id] = sent_message.message_id
    repeated_messages[sent_message.message_id] = message.message_id


@bot.edited_message_handler(func=lambda msg: True)
def edit_repeated_message(message):
    """
    Handler for edited messages to update repeated messages

    Args:
        message: Edited message object

    Returns: None
    """
    # Check if the edited message ID is in the list of repeated message IDs
    if message.message_id in repeated_messages:
        # Get the ID of the original message that was repeated
        original_message_id = repeated_messages[message.message_id]
        # Remove the "/repeat " prefix from the message text
        text = message.text.split(' ', 1)[1]
        # Edit the original message with the edited text
        edit_msg(text, get_chat_id(message), original_message_id)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """
    Handle incoming messages and process them accordingly.

    Args:
        message (telegram.Message): The incoming message object.

    Returns:
        None
    """
    if message.chat.type == 'private':
        send_chat_action(get_chat_id(message), 'typing')
        # Always respond in a private conversation
        response = inmers.inmers_chat(message.text, datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))
        send_msg(get_chat_id(message), response)
    if message.chat.title == "UnAI":
        # Send typing status)
        send_chat_action(get_chat_id(message), 'typing')
        # Send the response in the UnAI topic
        response = inmers.inmers_chat(message.text, datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))
        bot.send_message(message.chat.id, response, parse_mode='Markdown', disable_web_page_preview=True)
    elif re.search(fr'@{bot.get_me().username}', message.text):
        # If the message mentions the bot, process it
        send_chat_action(get_chat_id(message), 'typing')

        # Call inmers_chat with the message text and get the response
        response = inmers.inmers_chat(message.text, datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))

        # Check if the message is a reply to another message
        if message.reply_to_message:
            # Send the response as a reply to the original message, including the citation
            bot.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} {response}",
                             reply_to_message_id=message.reply_to_message.message_id)
        else:
            # Send the response as a regular message
            send_msg(get_chat_id(message), response)
    else:
        # Ignore messages in a group chat that do not mention the bot or are not in the UnAI topic
        pass


# Initialize an empty dictionary to store the message IDs of repeated messages
repeated_messages = {}

# arrancar el bot
bot.polling()
