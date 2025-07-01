# main.py

from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID
from ai_generator import generate_post

# Initialize the bot
bot = Bot(token=TELEGRAM_TOKEN)

# Function to send the post
def send_post():
    message = generate_post()
    bot.send_message(chat_id=CHAT_ID, text=message)
    print("✅ Post sent to Telegram!")

# Run a simple interactive loopppost
if __name__ == "__main__":
    while True:
        user_input = input("\nType 'post' to send an AI-generated message to Telegram, or 'exit' to quit:\n> ").strip().lower()
        
        if user_input == "post":
            send_post()
        elif user_input == "exit":
            print("👋 Exiting the bot.")
            break
        else:
            print("⚠️ Invalid command. Type 'post' or 'exit'.")
