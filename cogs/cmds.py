import discord
import traceback
import sys
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('CMDS has connected to Bot!')

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        try:
            await ctx.channel.purge(limit=amount)
        except:
            await ctx.channel.purge(limit=2)

    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await ctx.send(F"{member.name} has been kicked from the Server, Because: {reason}")
        await member.kick(reason=reason)

    @commands.command(aliases=['b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await ctx.send(F"{member.name} has been banned from the Server, Because: {reason}")
        await member.ban(reason=reason)


def setup(bot):
    bot.add_cog(Example(bot))
