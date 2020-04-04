from discord.ext import commands
import discord
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()  # 接続に使用するオブジェクト

# 起動時
@client.event
async def on_ready():
    print('ログイン成功')

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


bot.run(token)
# botとしてDiscordに接続(botのトークンを指定)
client.run('TOKEN_OF_YOUR_BOT')
