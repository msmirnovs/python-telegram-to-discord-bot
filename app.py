import discord
from telethon.sync import TelegramClient
from telethon import events

# Telegram setup
api_id = #
api_hash = '#'
client = TelegramClient('anon', api_id, api_hash)

# Discord setup
discord_token = '#'
discord_channel_id = #
intents = discord.Intents.default()  # Create a new Intents instance without privileged intents
discord_client = discord.Client(intents=intents)  # Pass the intents to the Client

@discord_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(discord_client))
    await client.start()

@client.on(events.NewMessage(chats=(-100...)))
async def new_message_handler(event):
    message = event.message

    print(f"Received a new message: {message.message}")

    try:
        if message.media is not None:
            # If the message has media, download it
            file_path = await client.download_media(message=message, file='file')
            if file_path is not None:
                # Send both the text and the media in one message
                await discord_client.get_channel(discord_channel_id).send(content=message.message, file=discord.File(file_path))
            else:
                print("Failed to download media")
        else:
            # If the message is just text, send it
            await discord_client.get_channel(discord_channel_id).send(message.message)
    except Exception as e:
        print(f"An error occurred: {e}")


discord_client.run(discord_token)
