import random
import discord
from discord.ext import commands


class CommandBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command
    @commands.command(alliases=['bot', 'BOT'])
    async def welcome(self, ctx):
        messeage_reply = [
            'Huynh hiện là chủ server discord này',
            'Huynh và bot chào mừng bạn đến với sever',
            (
                'Rất vui được chào đón bạn,'
                'hãy ở lại và tận hưởng nhé!'
            ),
        ]
        reponse = random.choice(messeage_reply)
        await ctx.send(reponse)

    @commands.command()
    async def purge(self, ctx, amount: int):
        # Nhập vào số kí tự muốn xóa (Syntax: !purge 1000)
        await ctx.channel.purge(limit=amount, check=None, before=None)
        print('Đã xóa thành công!')

    @commands.command()
    @commands.has_role('Admin')
    async def create_channel(self, ctx, *, channel_name='Linh tinh'):
        guild = ctx.guild
        existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Đã tạo 1 channel mới: {channel_name}')
            await guild.create_text_channel(channel_name)
            await ctx.send('Đã tạo channel thành công')

    @commands.command()
    @commands.has_role('Admin')
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Đã kick {member.mention}')

    @commands.command()
    @commands.has_role('Admin')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Đã ban thành công {member.mention}')

    @commands.command()
    @commands.has_role('Admin')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Đã unban {user.mention} thành công')

                return

    '''
    Embed : Nhúng
     - Nhúng link hoặc show các đối tượng từ bên ngoài
    '''
    @commands.command(pass_context=True)
    async def profile(self, ctx):
        # Background derect_message embed
        embed = discord.Embed(
            title='FaceBook',
            url='https://www.facebook.com/quy.ac.921',
            description='Host of this Discord Zoom',
            colour=discord.Colour.blue()
        )
        # Content Embed
        embed.set_footer(text='Enjoin it')
        embed.set_image(url='https://cdn.discordapp.com/avatars/645299985612800020/7d2db4e716b94e71afd8ebf956083770.webp?size=128')
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/645299985612800020/7d2db4e716b94e71afd8ebf956083770.webp?size=128')
        embed.set_author(name='Hyun.', icon_url='https://cdn.discordapp.com/avatars/645299985612800020/7d2db4e716b94e71afd8ebf956083770.webp?size=128')
        embed.add_field(name='Field Name', value='Value Name', inline=False)

        await ctx.author.send(embed=embed)  # Send private direct message outside channel

    '''
    Trả về avatar được get từ discord
    Syntax: '!getav @member'
    '''
    @commands.command(pass_context=True)
    async def getav(self, ctx, user: discord.Member = None):
        embed = discord.Embed(title='Avatar của ' + user.name, colour=discord.Colour(0xffdab9))
        embed.set_image(url=f'{user.avatar_url}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CommandBot(bot))
