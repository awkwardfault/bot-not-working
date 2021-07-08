
import pprint
import requests
import discord
import aiohttp
from discord.ext import commands


class test(commands.Cog):
    def __inti__(self, bot):
        self.bot = bot

    @commands.command()
    async def waifu(self, ctx):
        url = "https://animu.p.rapidapi.com/waifu"
        headers = {
            'auth': "key1",
            'x-rapidapi-key': "key",
            'x-rapidapi-host': "animu.p.rapidapi.com"
        }
        # This needs more work to do more but this is the beginngings of it
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    _names = data['names']
                    _name = _names['en']
                    _images = data['images']
                    _image = _images[0]
                    _data = data['from']
                    _from = _data['name']
                    _type = _data['type']
                    em = discord.Embed()
                    # In order for this to work you need to just do em.add_field(name=<name here>, value=<value here>)
                    em.set_image(url=_image)

                await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(test(bot))
