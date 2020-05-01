import traceback
import sys
import discord
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # return True/False
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.CheckFailure):
            return await ctx.send('Bạn không đủ quyền để thực hiện chức năng này')

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} đã bị vô hiệu hóa')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} không thể sử dụng tin nhắn riêng tư')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                return await ctx.send('Không thể tìm thấy thành viên, vui lòng thử lại!')

        elif isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Bạn đã nhập thiếu giá trị cần thiết')

        print('Bỏ qua exception trong lệnh {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
