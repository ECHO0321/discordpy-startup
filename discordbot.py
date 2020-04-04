from discord.ext import commands
import discord
import os
import traceback
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

voice = None
player = None

client = discord.Client()  # 接続に使用するオブジェクト

@client.event
async def on_message(message):
    global voice, player
    msg = message.content
    if message.author.bot:
        return
    
    if msg == '/join':
        if message.author.voice_channel is None:
            await client.send_message(message.channel ,'ボイスチャンネルに参加してからコマンドを打ってください。')
            return
        if voice == None:
            # ボイスチャンネルIDが未指定なら
            if discord_voice_channel_id == '':
                voice = await client.join_voice_channel(message.author.voice_channel)
            # ボイスチャンネルIDが指定されていたら
            else:
                voice = await client.join_voice_channel(client.get_channel(discord_voice_channel_id))
        # 接続済みか確認
        elif(voice.is_connected() == True):
            # 再生中の場合は一度停止
            if(player.is_playing()):
                player.stop()
            # ボイスチャンネルIDが未指定なら
            if discord_voice_channel_id == '':
                await voice.move_to(message.author.voice_channel)
            # ボイスチャンネルIDが指定されていたら
            else:
                await voice.move_to(client.get_channel(discord_voice_channel_id))

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    print("\007")

#テスト
@bot.command()
async def timer15s(ctx):
    await ctx.send('15秒計測します！')
    await asyncio.sleep(15)
    await ctx.send('15秒経ちました！')
    
@bot.command()
async def timer30s(ctx):
    await ctx.send('30秒計測します！')
    await asyncio.sleep(30)
    await ctx.send('30秒経ちました！')
    
@bot.command()
async def timer5m(ctx):
    await ctx.send('5分計測します！')
    await asyncio.sleep(300)
    await ctx.send('5分経ちました！')
        
@bot.command()
async def timer10m(ctx):
    await ctx.send('10分計測します！')
    await asyncio.sleep(600)
    await ctx.send('10分経ちました！')
        
@bot.command()
async def timer20m(ctx):
    await ctx.send('20分計測します！')
    await asyncio.sleep(1200)
    await ctx.send('20分経ちました！')

@bot.command()
async def timer30m(ctx):
    await ctx.send('30分計測します！')
    await asyncio.sleep(1800)
    await ctx.send('30分経ちました！')
    
@bot.command()
async def timer1h(ctx):
    await ctx.send('1時間計測します！')
    await asyncio.sleep(1800)
    await ctx.send('あと30分です！')
    await asyncio.sleep(1800)
    await ctx.send('1時間経ちました！')
    
    
       # botをボイスチャットから切断させる
    if msg == '/disconnect':
        if voice is not None:
            await voice.disconnect()
            voice = None
            return

bot.run(token)
# botとしてDiscordに接続(botのトークンを指定)
client.run('TOKEN_OF_YOUR_BOT')
