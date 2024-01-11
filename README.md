# Telegram to Discord Bot

This bot forwards messages from a Telegram channel to a Discord channel.

## Setup

Here are the steps you need to follow to set up the bot:

1. **Create a bot in Telegram:**
    - Open Telegram and find @BotFather.
    - Send him a /start message and follow the instructions to create a new bot.
    - After creating the bot, BotFather will provide you with a token. Save it, you will need it to connect to the Telegram API.

2. **Get API ID and API Hash from Telegram:**
    - Go to https://my.telegram.org/auth and log in to your account.
    - Go to the API development tools section and create a new application.
    - After creating the application, you will get an API ID and API Hash. Save them.

3. **Create a bot in Discord:**
    - Go to https://discord.com/developers/applications and log in to your account.
    - Click on the "New Application" button and enter a name for your application.
    - Go to the Bot section and click on the "Add Bot" button.
    - After creating the bot, you will get a token. Save it.

4. **Get Discord Channel ID:**
    - Open Discord and go to settings (the gear icon at the bottom left).
    - In the "Advanced" section, enable "Developer Mode".
    - Now you can right-click on any channel and select "Copy ID" to get its ID.

5. **Install necessary Python libraries:**
    - Install the discord.py and Telethon libraries using pip:

    ```
    pip install discord.py
    pip install Telethon
    ```

6. **Run the bot:**
    - Replace 'api_id', 'api_hash', 'discord_token', 'discord_channel_id' and 'telegram_channel_id' in the code with the corresponding values.
    - Run the code.

Please note that this code is a simple example and does not handle all possible cases. You will need additional error handling and management of different types of media files.
