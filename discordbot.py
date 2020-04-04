from discord.ext import commands
import discord
import os
import traceback
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("はろー"):
        m = "こんにちは、" + message.author.name + "さん"
        await client.send_message(message.channel,m)

client.run('token')


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
    await asyncio.sleep(3600)
    await ctx.send('1時間経ちました！')
    
@bot.command()
async def stoptimer(ctx):
    asyncio.exit:
    
bot.run(token)
