
import pprint
import requests
import discord
from discord.ext import commands

class test(commands.Cog):
    def __inti__(self,test0):
       self.test0 = test0

    @commands.command()
    async def waifu(self,ctx):

        api_base_url = "https://animu.p.rapidapi.com/waifu"
        headers = {
            'auth': "key1",
            'x-rapidapi-key': "key",
            'x-rapidapi-host': "animu.p.rapidapi.com"
            }    

        r= requests.get(api_base_url,headers=headers)

        data=r.json()
        _names= data['names']
        _name=_names['en']
        _images= data['images']
        _image=_images[0]
        _data= data['from']
        _from= _data['name']
        _type= _data['type']
        em= discord.Embed()
        em.set_image(url = _image)

        await ctx.send(embed =em)

def setup(test0):
    test0.add_cog(test(test0))
