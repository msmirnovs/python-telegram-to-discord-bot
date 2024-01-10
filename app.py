import discord
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

# Telegram setup
api_id = 'your_telegram_api_id'
api_hash = 'your_telegram_api_hash'
token = 'your_telegram_token'

client = TelegramClient('anon', api_id, api_hash)

# Discord setup
discord_token = 'your_discord_token'
discord_channel_id = 'your_discord_channel_id'
discord_client = discord.Client()

@discord_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(discord_client))

    await client.start(bot_token=token)
    channel = await client.get_entity('telegram_channel_id')

    # Get the last 10 messages
    messages = await client(GetHistoryRequest(
        peer=channel,
        limit=10,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))

    for message in messages.messages:
        if message.media is not None:
            # If the message has media, download it
            await client.download_media(message=message, file='file')
            await discord_client.get_channel(discord_channel_id).send(file=discord.File('file'))
        else:
            # If the message is just text, send it
            await discord_client.get_channel(discord_channel_id).send(message.message)

    await client.disconnect()

discord_client.run(discord_token)