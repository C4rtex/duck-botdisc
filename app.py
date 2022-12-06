from nextcord.ext import commands
from nextcord import Interaction
from gtts import gTTS
import nextcord, os, uuid,asyncio
intents = nextcord.Intents.all() 
intents.message_content = True
arrPersonas = []
arrTextos =[]
bot = commands.Bot(command_prefix="'",intents=intents)
textoSonando=""
@bot.command()
async def sc(ctx, *, searchword):  
    id= uuid.uuid4().hex
    try:
        channel = ctx.author.voice.channel
        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(channel)
        else:
            await channel.connect()
        voice = ctx.voice_client
        if voice.is_playing():
            print("ya esta en funcion")
        else:
            for txts in arrTextos:
                os.remove(txts)
            language = "es-us"
            if(searchword == "🏳️‍🌈"):
                searchword = "bandera gay"
            if(searchword == "🇻🇪"):
                searchword = "benecos"
            speech = gTTS(text = searchword, lang=language, slow=False)
            speech.save(f"{ctx.author}{id}.mp3")
            voice = ctx.voice_client
            textoSonando =f"{ctx.author}{id}.mp3"
            arrTextos.append(textoSonando)
            print(textoSonando)
            voice.play(nextcord.FFmpegPCMAudio(f"{ctx.author}{id}.mp3"),after = lambda e : elimina())
            def elimina():
                os.remove(f"{ctx.author}{id}.mp3")
    except:
        print("entra primer try")
        os.remove(f"{ctx.author}{id}.mp3")
@bot.command()
async def saludoFiggy(ctx):  
    channel = ctx.author.voice.channel
    if ctx.voice_client is not None:
        await ctx.voice_client.move_to(channel)
    else:
        await channel.connect()
    voice = ctx.voice_client
    if voice.is_playing():
        next
    else:
        voice.play(nextcord.FFmpegPCMAudio(f"saludoffiggy.wav"))
@bot.slash_command(guild_ids=[726202948736253988,440668241807933440])
async def scp(interaction: Interaction, frase):
    channel = interaction.user.voice.channel
    guild = interaction.guild
    if guild.voice_client is not None:
        await guild.voice_client.move_to(channel)
    else:
        await channel.connect()
    voice = guild.voice_client
    if voice.is_playing():
        if(len(arrPersonas)>0):
            await interaction.send(f"espere hq q {arrPersonas[0]} esta hablando")
    else:
        for txts in arrTextos:
                os.remove(txts)
        await interaction.send("Hablando")
        language = "es-us"
        id= uuid.uuid4().hex
        if(frase == "🏳️‍🌈"):
            frase = "bandera gay"
        if(frase == "🇻🇪"):
            frase = "benecos"
        speech = gTTS(text = frase, lang=language, slow=False)
        speech.save(f"{interaction.user}{id}.mp3")
        voice = guild.voice_client
        textoSonando = f"{interaction.user}{id}.mp3"
        arrTextos.append(textoSonando)
        if(len(arrPersonas)==0):
            arrPersonas.append(interaction.user)
        voice.play(nextcord.FFmpegPCMAudio(f"{interaction.user}{id}.mp3"),after = lambda e : elimina())
        def elimina():
            voice.stop()
            os.remove(f"{interaction.user}{id}.mp3")
            arrPersonas.clear()

@bot.slash_command(guild_ids=[726202948736253988,440668241807933440])
async def sal(interaction: Interaction):
    channel = interaction.user.voice.channel
    guild = interaction.guild
    if guild.voice_client is not None:
        await guild.voice_client.move_to(channel)
    else:
        await channel.connect()
    voice = guild.voice_client
    if voice.is_playing():
        next
    else:
        voice.play(nextcord.FFmpegPCMAudio(f"saludoffiggy.wav"))

@bot.command()
async def leave(ctx, help = "deja el canal de voz"):
    voice = ctx.voice_client
    if textoSonando !="":
        voice.pause()
        os.remove(textoSonando)
    await ctx.voice_client.disconnect()
@bot.command()
async def pause(ctx):
    voice = ctx.voice_client
    if textoSonando !="":
         voice.pause()
         os.remove(textoSonando)
    if voice.is_playing() == True:
        voice.pause()
    else:
        print("entra segundo try")
        await ctx.send("el bot no está sonando")
 
@bot.command(aliases = ["skip"])
async def stop(ctx):
    try:
        voice = ctx.voice_client
        if voice.is_playing() == True:
            voice.stop()
        else:
            await ctx.send("el bot no está sonando")
    except:
        if textoSonando !="":
            os.remove(textoSonando)
 
@bot.slash_command()
async def tts(interaction: Interaction, frase):
    channel = interaction.user.voice.channel
    guild = interaction.guild
    if guild.voice_client is not None:
        await guild.voice_client.move_to(channel)
    else:
        await channel.connect()
    voice = guild.voice_client
    if voice.is_playing():
        if(len(arrPersonas)>0):
            await interaction.send(f"espere hq q {arrPersonas[0]} esta hablando")
    else:
        for txts in arrTextos:
                os.remove(txts)
        await interaction.send("Hablando")
        language = "es-us"
        id= uuid.uuid4().hex
        if(frase == "🏳️‍🌈"):
            frase = "bandera gay"
        if(frase == "🇻🇪"):
            frase = "benecos"
        speech = gTTS(text = frase, lang=language, slow=False)
        speech.save(f"{interaction.user}{id}.mp3")
        voice = guild.voice_client
        textoSonando = f"{interaction.user}{id}.mp3"
        arrTextos.append(textoSonando)
        if(len(arrPersonas)==0):
            arrPersonas.append(interaction.user)
        voice.play(nextcord.FFmpegPCMAudio(f"{interaction.user}{id}.mp3"),after = lambda e : elimina())
        def elimina():
            voice.stop()
            os.remove(f"{interaction.user}{id}.mp3")
            arrPersonas.clear()


@scp.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("You have to be connected to a Voice Channel to use this command.")

 
@leave.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")

 
@scp.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")

@tts.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")

@stop.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")

 
@pause.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")

bot.run(os.environ["DISCORD_TOKEN"])
 