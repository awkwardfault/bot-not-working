import aiohttp
import asyncio
import json

import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandError

class kitsu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #aiohttp mode
    async def kitsu(query, num):
        num = num - 1
        api_link = 'https://kitsu.io/api/edge/anime?filter[text]=%s' % query
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(api_link) as r:
                    try:
                        data = await r.json()
                    except ValueError:
                        return 'ERROR: Something bad happening with the result, try again.'
            except aiohttp.ClientError:
                return "ERROR: Connection Timeout."
            if aiohttp.ClientResponse.status != 200:
                if aiohttp.ClientResponse.status == 404:
                    return "ERROR: Not Found"
                elif aiohttp.ClientResponse.status == 500:
                    return "ERROR: Internal Server Error"
            try:
                entry = data["data"][num]
            except IndexError:
                return "ERROR: No Result."

            title = entry['attributes']['titles']['en_jp']
            synop = entry['attributes']['synopsis']
            rate = entry['attributes']['averageRating']
            start = entry['attributes']['startDate']
            end = entry['attributes']['endDate']
            status = entry['attributes']['status']
            epTotal = entry['attributes']['episodeCount']
            dataLen = len(data['data'])
            img = entry['attributes']['posterImage']['small']
            finalResult = {"title": title, "episode": epTotal, 'status': status, 'score': rate, 'startDate': start, 'endDate': end, 'posterImg': img, 'synopsis': synop, 'dataLength': dataLen}
            return finalResult

    

    @commands.command(pass_context=True)
    async def animu(self,ctx, *, title):
        title = title.replace(' ', '%20')
        init = await (title, 1)
        if type(init) is str:
            await ctx.say(init)
            return 'No result'
        else:
            pass

        maxPage = int(init['dataLength'])
        firstRun = True
        while True:
            if firstRun:
                firstRun = False
                num = 1
                find = await kitsu (title, num)
                embed=discord.Embed(title="Anime Info", color=0x81e28d)
                embed.set_image(url=find['posterImg'])
                embed.add_field(name='Title', value=find['title'], inline=False)
                embed.add_field(name='Episode', value=find['episode'], inline=True)
                embed.add_field(name='Status', value=find['episode'], inline=True)
                embed.add_field(name='Score', value=find['score'], inline=True)
                embed.add_field(name='Start Date', value=find['startDate'], inline=True)
                embed.add_field(name='End Date', value=find['endDate'], inline=True)
                msg = await ctx.say(embed=embed)
                msg2 = await ctx.say('```{}```'.format(str(find['synopsis'])))	

            if maxPage == 1 and num == 1:
                print('{}/{}'.format(str(num),str(maxPage)))
                toReact = ['✅']
            elif num == 1:
                print('{}/{}'.format(str(num),str(maxPage)))
                toReact = ['⏩', '✅']
            elif num == maxPage:
                print('{}/{}'.format(str(num),str(maxPage)))
                toReact = ['⏪', '✅']
            elif num > 1 and num < maxPage:
                print('{}/{}'.format(str(num),str(maxPage)))
                toReact = ['⏪', '⏩', '✅']
            for reaction in toReact:
                await ctx.add_reaction(msg2, reaction)
            #feel free to change ✅ to 🆗 or the opposite
            def checkReaction(reaction, user):
                e = str(reaction.emoji)
                return e.startswith(('⏪', '⏩', '✅'))

            res = await ctx.wait_for_reaction(message=msg2, user=ctx.message.author, timeout=10, check=checkReaction)
            if res is None:
                await ctx.delete_message(ctx.message)
                await ctx.delete_message(msg)
                await ctx.delete_message(msg2)
                break
            elif '⏪' in str(res.reaction.emoji):
                num = num - 1
                find = await kitsu(title, num)
                embed=discord.Embed(title="Anime Info", color=0x81e28d)
                embed.set_image(url=find['posterImg'])
                embed.add_field(name='Title', value=find['title'], inline=False)
                embed.add_field(name='Episode', value=find['episode'], inline=True)
                embed.add_field(name='Status', value=find['episode'], inline=True)
                embed.add_field(name='Score', value=find['score'], inline=True)
                embed.add_field(name='Start Date', value=find['startDate'], inline=True)
                embed.add_field(name='End Date', value=find['endDate'], inline=True)
                fmtSyn = '```{}```'.format(str(find['synopsis']))
                await ctx.delete_message(msg)
                await ctx.delete_message(msg2)
                msg = await ctx.say(embed=embed)
                msg2 = await ctx.say(fmtSyn)
            elif '⏩' in str(res.reaction.emoji):
                num = num + 1
                find = await kitsu (title, num)
                embed=discord.Embed(title="Anime Info", color=0x81e28d)
                embed.set_image(url=find['posterImg'])
                embed.add_field(name='Title', value=find['title'], inline=False)
                embed.add_field(name='Episode', value=find['episode'], inline=True)
                embed.add_field(name='Status', value=find['episode'], inline=True)
                embed.add_field(name='Score', value=find['score'], inline=True)
                embed.add_field(name='Start Date', value=find['startDate'], inline=True)
                embed.add_field(name='End Date', value=find['endDate'], inline=True)
                fmtSyn = '```{}```'.format(str(find['synopsis']))
                await ctx.delete_message(msg)
                await ctx.delete_message(msg2)
                msg = await ctx.say(embed=embed)
                msg2 = await ctx.say(fmtSyn)
            elif '✅' in str(res.reaction.emoji):
                await ctx.delete_message(ctx.message)
                await ctx.delete_message(msg)
                await ctx.delete_message(msg2)
                break

    @animu.error
    async def animu_handler(self,error, ctx):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.say("Correct argument are:\n**{}animu <title>**".format)

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Kitsu1 connected')


def setup(bot):
    bot.add_cog(kitsu(bot))   

   