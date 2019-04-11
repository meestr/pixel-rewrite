from libs import macro
import aiohttp
from discord.ext import commands


class CAT(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="cat")
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as client_session:
            async with client_session.get("https://api.thecatapi.com/v1/images/search?size=full") as r:
                res = await r.json()
                await ctx.send(
                    embed=await macro.img(res[0].get("url"))
                )
                await client_session.close()

    @commands.command(name="dog")
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as client_session:
            async with client_session.get("https://api.thedogapi.com/v1/images/search?size=full") as r:
                res = await r.json()
                await ctx.send(
                    embed=await macro.img(res[0].get("url"))
                )
                await client_session.close()

    @commands.command(name='bird')
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://shibe.online/api/birds") as r:
                re = await r.json()
                await ctx.send(
                    embed=await macro.img(re[0])
                )
                await cs.close()

    @commands.command(name='shibe', aliases=['shiba', 'doge'])
    async def bir(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true") as r:
                re = await r.json()
                await ctx.send(
                    embed=await macro.img(re[0])
                )
                await cs.close()


def setup(bot: commands.Bot):
    bot.add_cog(CAT(bot=bot))
