import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# sanat
trigger_words = ["tulee", "tulossa", "tullaan", "tulen", "tulkaa", "tulos", "tuun", "tuutteko", "tullaa", "saa", "saat", "saan", "saanut",
    "saavun", "saavutaan", "saitteko", "saitte", "saatiin", "sain", "tuli",]

@client.event
async def on_ready():
    print(f'Kirjautunut sisään nimellä {client.user}')
    channel = client.get_channel(936727688108974083)  # <-- tähän oma kanavan ID
    if channel:
        await channel.send("Tirsk-botti on nyt käynnissä!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(word in message.content.lower() for word in trigger_words):
        await message.channel.send('tirsk')

# token
client.run('')
