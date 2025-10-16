import discord
from discord.ext import commands
from games import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('ciao'):
        await message.channel.send("ciao, come va?")
    elif message.content.startswith('arrivederci'):
        await message.channel.send("ciao ciao :)")
    elif message.content.startswith('flip'):
        await message.channel.send(f"ho lanciato la moneta... {flip_coin().lower()}")
    elif message.content.startswith('dice'):
        await message.channel.send(f"il dado dice {roll_dice()}")
    elif message.content.startswith('8ball'):
        await message.channel.send(eight_ball().lower())
    elif message.content.startswith('yesno'):
        question = message.content[7:].strip()
        try:
            response = yes_or_no(question)
            await message.channel.send(response.lower())
        except Exception:
            await message.channel.send("ehm, domanda non supportata... prova tipo: ananas va sulla pizza?, esistono rocce?, l'acqua è bagnata?, il fuoco è caldo?, il cielo è blu?, gli esseri umani sono robot?")
    elif message.content.startswith('chicken'):
        await message.channel.send(f"why did the chicken cross the road? boh, {why_did_the_chicken_cross_the_road().lower()}")
    elif message.content.startswith('genpass'):
        try:
            length = int(message.content.split()[1])
            if length <= 0:
                await message.channel.send("la lunghezza deve essere positiva, tipo 5 o 10")
            else:
                password = gen_pass(length)
                await message.channel.send(f"ecco la password: {password}")
        except (IndexError, ValueError):
            await message.channel.send("scrivi tipo: ?genpass 8, ok?")
    elif message.content.startswith('?help'):
        help_message = (
            "comandi che puoi usare:\n"
            "ciao - ti saluto\n"
            "arrivederci - emoji sorridente\n"
            "flip - lancio una moneta\n"
            "dice - tiro un dado\n"
            "8ball - rispondo a caso\n"
            "yesno <domanda> - rispondo sì o no a domande predefinite\n"
            "chicken - rispondo alla domanda del pollo\n"
            "genpass <lunghezza> - ti do una password random\n"
            "help - ti mostro questo messaggio\n"
            "turnoff - spegne il bot (solo admin)"
        )
        await message.channel.send(help_message)
    elif message.content.startswith('turnoff'):
        if message.author.guild_permissions.administrator:
            await message.channel.send("ok, sto spegnendo il bot...")
            await bot.close()
        else:
            await message.channel.send("ehm, non hai i permessi per spegnere il bot, sorry")
    else:
        await message.channel.send(message.content.lower())

    await bot.process_commands(message)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

# token: no.

bot.run("metti tuo token qui")
