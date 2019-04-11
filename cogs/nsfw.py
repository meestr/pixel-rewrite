# keep out children

import random
from discord.ext import commands
from libs import macro
import aiohttp
import asyncio
import rule34


class NSFW(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.loop = asyncio.get_event_loop()

    @commands.command(name='hentai')
    async def henai(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://nekobot.xyz/api/image?type=hentai") as res:
                    res = await res.json()
                    await ctx.send(embed=await macro.img(res['message']))
        else:
            await ctx.send(embed=await macro.error(f"You must use this command in an NSFW channel."))

    @commands.command(name='4k')
    async def fourk(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://nekobot.xyz/api/image?type=4k") as res:
                    res = await res.json()
                    await ctx.send(embed=await macro.img(res['message']))
        else:
            await ctx.send(embed=await macro.error(f"You must use this command in an NSFW channel."))

    @commands.command(name='gif')
    async def gif(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://nekobot.xyz/api/image?type=pgif") as res:
                    res = await res.json()
                    await ctx.send(embed=await macro.img(res['message']))
        else:
            await ctx.send(embed=await macro.error(f"You must use this command in an NSFW channel."))

    @commands.command(name='ass')
    async def ass(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://nekobot.xyz/api/image?type=ass") as res:
                    res = await res.json()
                    await ctx.send(embed=await macro.img(res['message']))
        else:
            await ctx.send(embed=await macro.error(f"You must use this command in an NSFW channel."))

    @commands.command(name='gonewild')
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://nekobot.xyz/api/image?type=gonewild") as res:
                    res = await res.json()
                    await ctx.send(embed=await macro.img(res['message']))
        else:
            await ctx.send(embed=await macro.error(f"You must use this command in an NSFW channel."))

    @commands.command(name='rule34', aliases=['34', 'r34'])
    async def rule_thirty_four(self, ctx, *, query):
        if ctx.channel.is_nsfw():
            r34 = rule34.Rule34(loop=self.loop)
            msg = await ctx.send(embed=await macro.send(f"This might take a couple of seconds, standby..."))
            await asyncio.sleep(1)
            if not await r34.getImageURLS(query):
                return await msg.edit(embed=await macro.error(f"I couldn't find anything for ``{query}``"))
            await msg.edit(embed=await macro.img(str(random.choice(await r34.getImageURLS(query)))))
        else:
            await ctx.send(embed=await macro.error(f"You must use this command in an NSFW channel."))
def setup(bot: commands.Bot):
    bot.add_cog(NSFW(bot))
