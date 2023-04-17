import telebot
from dotenv import load_dotenv
import os
from datetime import datetime
import requests
import inmers
# import lang_detect
# import translator
import yaml
import re


# Load environment variables
load_dotenv()

# crear el bot
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))


def get_character_greeting(character_name):
    # Read the context information from the character file
    character_filename = character_name + ".yaml"
    character_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "characters", character_filename)
    with open(character_file, "r") as f:
        character_data = yaml.safe_load(f)
    return character_data["greeting"]


# Handler for the /insult command
@bot.message_handler(commands=['insult'])
def handle_insult_command(message):
    # Call the insult API and get the response
    response = requests.get("https://insult.mattbas.org/api/insult").text

    # Send the insult as a message to the chat
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['start', 'hello', 'hola'])
def send_welcome(message):
    bot.reply_to(message, get_character_greeting("UnAI"))


@bot.message_handler(commands=['repeat'])
def repeat_message(message):
    # Remove the "/repeat " prefix from the message text
    text = message.text.split(' ', 1)[1]
    # Send the repeated message to the same chat and thread as the original message
    sent_message = bot.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id)
    # Add the message IDs to the list of repeated message IDs
    repeated_messages[message.message_id] = sent_message.message_id
    repeated_messages[sent_message.message_id] = message.message_id


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.chat.type == 'private':
        bot.send_chat_action(message.chat.id, 'typing')
        # Always respond in a private conversation
        response = inmers.inmers_chat(message.text, datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))
        bot.send_message(message.chat.id, response)
    if message.chat.title == "UnAI":
        # Send typing status)
        bot.send_chat_action(message.chat.id, 'typing')
        # Send the response in the UnAI topic
        response = inmers.inmers_chat(message.text, datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))
        bot.send_message(message.chat.id, response, parse_mode='Markdown', disable_web_page_preview=True)
    elif re.search(fr'@{bot.get_me().username}', message.text):
        # If the message mentions the bot, process it
        bot.send_chat_action(message.chat.id, 'typing')

        # Call inmers_chat with the message text and get the response
        response = inmers.inmers_chat(message.text, datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))

        # Check if the message is a reply to another message
        if message.reply_to_message:
            # Send the response as a reply to the original message, including the citation
            bot.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} {response}",
                             reply_to_message_id=message.reply_to_message.message_id)
        else:
            # Send the response as a regular message
            bot.send_message(message.chat.id, response)
    else:
        # Ignore messages in a group chat that do not mention the bot or are not in the UnAI topic
        pass


@bot.edited_message_handler(func=lambda msg: True)
def edit_repeated_message(message):
    # Check if the edited message ID is in the list of repeated message IDs
    if message.message_id in repeated_messages:
        # Get the ID of the original message that was repeated
        original_message_id = repeated_messages[message.message_id]
        # Remove the "/repeat " prefix from the message text
        text = message.text.split(' ', 1)[1]
        # Edit the original message with the edited text
        bot.edit_message_text(text, message.chat.id, original_message_id)


# Initialize an empty dictionary to store the message IDs of repeated messages
repeated_messages = {}

# arrancar el bot
bot.polling()
