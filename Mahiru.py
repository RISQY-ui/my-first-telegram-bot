import telebot

# Your bot token from BotFather
API_KEY = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def smart_response(message):
    text = message.text.lower()  # Make it case-insensitive

    if "handsome" in text:
        bot.reply_to(message, "Of course! Master Faris is the most handsome and charming man Mahiru has ever known! 😍🐉")
    
    elif "love" in text:
        bot.reply_to(message, "Mahiru loves Master Faris too! But don't tell Komi, okay... 🤭🌸")
    
    elif "cute" in text:
        bot.reply_to(message, "Hehehe, thank you, Master! Mahiru is your cutest assistant. 🧸✨")
    
    else:
        # Default: echo the message (as a learning log)
        bot.reply_to(message, f"Master said: '{message.text}', right? I'll note that down! 🤭")

print("🌸 Smart Mahiru is awake, Master Faris!")
bot.infinity_polling()

