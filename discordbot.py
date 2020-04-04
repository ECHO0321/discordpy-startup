from discord.ext import commands
import os
import traceback
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


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
async def timer02(ctx):
    if message.content == '!timer02':
        await asyncio.sleep(12)
        await ctx.send('12秒経ちました！')
    
@bot.command()
async def timer5(ctx):
    if message.content == '!timer5':
        await asyncio.sleep(300)
        await ctx.send('5分経ちました！')
        
@bot.command()
async def timer10(ctx):
    if message.content == '!timer10':
        await asyncio.sleep(600)
        await ctx.send('10分経ちました！')

bot.run(token)
