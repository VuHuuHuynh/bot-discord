import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix=os.getenv('PREFIX'))


@bot.command()
@commands.has_role('Admin')
async def load(ctx, extension):
    try:
        bot.load_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send(f'**ERROR:**{type(e).__name__} - {e}')
    else:
        await ctx.send('**Đã load thành công**')


@bot.command()
@commands.has_role('Admin')
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send(f'**ERROR**:{type(e).__name__} - {e}')
    else:
        # '**Text**' == Ctrl + B(Microsoft Word)
        await ctx.send('**Đã unload thành công!**')


@bot.command()
@commands.has_role('Admin')
async def reload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send(f'**ERROR:**{type(e).__name__} - {e}')
    else:
        await ctx.send('**Đã reload thành công!**')

'''
os.listdir():
- Lấy danh sách tất cả các tệp, thư mục trong thư mục đc chỉ định
- Trả về list
'''
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv('BOT_TOKEN'))
