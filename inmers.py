import os
import sys
import time
import colorama
import platform
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import lang_detect
import translator
import yaml

os.environ['MOZ_HEADLESS'] = '1'

if platform.system() == "Windows":
    firefox_profile_path = os.path.expanduser("~") + os.sep + 'AppData' + os.sep + 'Local' + os.sep + 'Mozilla' + os.sep + 'Firefox' + os.sep + 'Profiles' + os.sep + 'inmersprofile.default-release'
else:
    firefox_profile_path = os.path.expanduser("~") + "/snap/firefox/common/.mozilla/firefox/inmersprofile.default-release"

if not os.path.exists(firefox_profile_path):
    os.mkdir(firefox_profile_path)

# Create a FirefoxOptions object with your profile path
firefox_options = webdriver.FirefoxOptions()

firefox_options.add_argument('--profile')

firefox_options.add_argument(firefox_profile_path)

service = Service(log_path=os.devnull)

# Create a new Firefox driver with your options
try:
    driver = webdriver.Firefox(options=firefox_options, service=service)
except:
    driver.quit()


# Load the Inmers web app
driver.get("https://inmers.com/app")

# Wait for the page to load
time.sleep(4)


def set_character_context(character_name):
    # Read the context information from the character file
    character_filename = character_name + ".yaml"
    character_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "characters", character_filename)
    with open(character_file, "r") as f:
        character_data = yaml.safe_load(f)
    context = character_data["context"]

    # Send the context information as the first message to the bot
    input_box = driver.find_element(By.CSS_SELECTOR, 'textarea')
    input_box.send_keys(context + Keys.RETURN)
    # add_message(context, initial_time)


set_character_context("UnAI")
time.sleep(15)


def add_message(message, initialtime):
    now = datetime.now()
    time = now.strftime("%H-%M-%S")
    date = now.strftime("%Y-%m-%d")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(script_dir, "conversations")

    if platform.system() == "Windows":
        x = repo_dir + "\\" + date
        filepath = x + "\\" + initialtime + ".txt"
    else:
        x = repo_dir + "/" + date
        filepath = x + "/" + initialtime + ".txt"
    if not os.path.exists(x):
        os.mkdir(x)

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(time.strip() + ": " + message.strip() + "\n")


def inmers_chat(message, initial_time):
    try:
        # Read the context information from the character file
        character_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "characters", "UnAI.yaml")
        with open(character_file, "r") as f:
            character_data = yaml.safe_load(f)
        context = character_data["context"]

        # Send the context information as the first message to the bot
        input_box = driver.find_element(By.CSS_SELECTOR, 'textarea')
        input_box.send_keys(context + Keys.RETURN)
        # add_message(context, initial_time)

        # Wait for the bot to respond and ignore its response
        time.sleep(20)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.mwai-text p')))

        input_box = driver.find_element(By.CSS_SELECTOR, 'textarea')
        message_lang = lang_detect.detect_language(message)
        add_message(message, initial_time)
        if message == "exit" or message == "quit":
            driver.quit()
            exit(0)

        input_box.send_keys(message + Keys.RETURN)

        time.sleep(20)

        # Wait for the bot to respond
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.mwai-text p')))
        all_responses = driver.find_elements(By.CSS_SELECTOR, 'div.mwai-reply')

        bot_text_responses = []
        for xd in all_responses:
            if xd.text not in bot_text_responses and "Inmers:" in xd.text and xd.text != "Inmers:\nBienvenido a la inteligencia artificial mas avanzada del mundo, ¿En que te puedo ayudar?":
                bot_text_responses.append(xd.text)

        index = len(bot_text_responses) - 1

        if bot_text_responses[index] == "":
            pass
        else:
            bot_response = bot_text_responses[index].strip("Inmers:\n")
            response_lang = lang_detect.detect_language(bot_response)

            if lang_detect.is_same_language(message_lang, response_lang):
                add_message(bot_response, initial_time)
                print(colorama.Fore.GREEN + "\n" + bot_response)
                print(colorama.Fore.RESET)
            else:
                bot_response = translator.translate(bot_response, message_lang)
                add_message(bot_response, initial_time)
                print(colorama.Fore.GREEN + "\n" + bot_response)
                print(colorama.Fore.RESET)
        if bot_response:
            return bot_response
    except Exception as e:
        print("Exception", repr(e))
        print("CLOSING...")
        driver.quit()
        exit(1)


def inmers(initial_time):
    while True:
        print(colorama.Fore.RED + "Enter your text:" + colorama.Fore.CYAN)
        inmers_chat(input(), initial_time)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(script_dir, "conversations")

    if not os.path.exists(repo_dir):
        os.mkdir(repo_dir)
    initial_time = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")

    if len(sys.argv) == 2:
        inmers_chat(sys.argv[1], initial_time)
    else:
        inmers(initial_time)
        driver.quit()


if __name__ == '__main__':
    main()
