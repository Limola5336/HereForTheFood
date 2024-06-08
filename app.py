import sys
from configparser import ConfigParser
from chatbot import ChatBot

def main():
    config = ConfigParser()
    config.read('credentials.ini')
    api_key = "AIzaSyBCsDVVifGrIpMnp4fgVIcbg1c1NY1k91E"

    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()

    print("Welcome to BizFinder Chatbot! (type quit to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            #print("Thank you for using Chatbot!")
            sys.exit("Thank you for using BizFinder!")
        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error: {e}")

main()