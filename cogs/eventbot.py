from discord.ext import commands
import discord


class EventBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    '''
    Event trong COGs:
    Syntax: @commands.Cog.listener()
    '''
    @commands.Cog.listener()
    async def on_ready(self):
        # Change status của bot
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('Bot\'s Hyun| !help'))
        print('Bot has connected to Discord!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f'Welcome {member.mention} to my channel')

    @commands.command()
    async def Ehelp(self, ctx):
        embed = discord.Embed(
            title='Event Help',
            description='Chức năng EventBot',
            colour=discord.Colour(0x99dd44)
        )
        embed.set_footer(text='!Ehelp')
        embed.add_field(name='Member join', value='Send private direct message', inline=False)
        embed.add_field(name='Check permission', value='Return check error', inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(EventBot(bot))
