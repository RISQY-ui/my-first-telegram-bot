# 🤖 Mahiru Bot - Telegram Bot Project

A simple Telegram bot created using Python and the pyTelegramBotAPI library. This bot was built to learn automation and API integration.

## How to Create This Bot

This documentation explains the steps I followed to bring my bot to life.

### 1. The "Birth" Phase (BotFather)

- Search for `@BotFather` on Telegram.
- Use the `/newbot` command to create a new bot.
- Give the bot a **Name** and a **Username** (must end with `_bot`).
- **Save the Token!** This is the most important key.

### 2. Setting Up the "Kitchen" (Termux)

1. Update the system:  
   `pkg update && pkg upgrade`
2. Install Python:  
   `pkg install python`
3. Install the library:  
   `pip install pyTelegramBotAPI`

### 3. Writing the Code (Nano Editor)

1. Create a new file:  
   `nano mahiru.py`
2. Paste the Python code into the editor.
3. Save the file:  
   - Press `CTRL + O` (Write Out).  
   - Press `ENTER` to confirm.  
   - Press `CTRL + X` to exit.

### 4. Running the Bot

- Run the script:  
  `python mahiru.py`
- If you see `"🌸 Mahiru is awake..."`, the bot is alive.

> The bot will only work while Termux is open and your internet is stable.

### 5. The Grand Launch (on Telegram)

- Open your bot on Telegram.
- Click the **START** button.
- If the bot replies, congratulations! You are a **Master Developer**!

## Author

**Faris** – [Your GitHub Profile Link]
code: import telebot

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

