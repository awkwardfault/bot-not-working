import pprint as pp
from discord.ext import commands
import aiohttp
from discord.ext.commands.core import command


class moviedb(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="movie")
    async def movie(self, context, search_query):
        api_key = 'api_key'
        url = "https://api.themoviedb.org/3/search/movie"

        params = {
            'api_key': f"{api_key}",
            'query': f"{search_query}",
            'page': '1',
            "include_adult": "true"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    results = data['results']
                    movie_info = results[0]
                    for movie in movie_info:
                        _description = movie['overview']
                        print(_description)
                        await context.send(_description)


def setup(bot):
    bot.add_cog(moviedb(bot))
