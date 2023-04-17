import telebot
from dotenv import load_dotenv
import os
from datetime import datetime
import requests
import inmers
import lang_detect
import translator


# Load environment variables
load_dotenv()

# crear el bot
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))


# Handler for the /insult command
@bot.message_handler(commands=['insult'])
def handle_insult_command(message):
    # Call the insult API and get the response
    response = requests.get("https://insult.mattbas.org/api/insult").text

    # Send the insult as a message to the chat
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['talk'])
def handle_talk_command(message):
    # Remove the "/talk " prefix from the message text
    text = message.text.split(' ', 1)[1]

    # Call the inmers_chat method and get the response
    response = inmers.inmers_chat(text, datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))

    # Send the response as a message to the chat
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['start', 'hello', 'hola'])
def send_welcome(message):
    bot.reply_to(message, "*UnAI strides into the room with a big hashish joint in his mouth, his eyes are red and are a bit closed when he sees you. He takes a seat next to you and light his hashish joint, his enthusiasm palpable in the air*")


@bot.message_handler(commands=['repeat'])
def repeat_message(message):
    # Remove the "/repeat " prefix from the message text
    text = message.text.split(' ', 1)[1]
    sent_message = bot.send_message(message.chat.id, text)
    # Add the message IDs to the list of repeated message IDs
    repeated_messages[message.message_id] = sent_message.message_id
    repeated_messages[sent_message.message_id] = message.message_id


@bot.message_handler(func=lambda message: '@'+bot.get_me().username in message.text)
def echo_all(message):
    # Send a typing action to indicate that the bot is processing the message
    bot.send_chat_action(message.chat.id, 'typing')

    response = inmers.inmers_chat(message.text, datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))

    bot.reply_to(message, response)


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
