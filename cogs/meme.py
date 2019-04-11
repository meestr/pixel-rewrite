from libs import macro
from discord.ext import commands
import aiohttp
from asyncio import sleep


class MemesAndShitDude(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.endpoint = "https://nekobot.xyz/api/imagegen?type="

    @commands.command(name='threats')
    async def threats(self, ctx, url: str = None):
        if not url:
            url = ctx.message.author.avatar_url
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}threats&url={url}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))

    @commands.command(name='clyde')
    async def clyde(self, ctx, *, text):
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}clyde&text={text}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))

    @commands.command(name='whowouldwin')
    async def epic_victory_royale(self, ctx, user1: str = None, user2: str = None):
        assert user1 and user2, "You need to add arguments for either ``user1`` or ``user2``!\nCorrect usage: ``p!whowouldwin [user1 url] [user2 url]"
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}whowouldwin&user1={user1}&user2={user2}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))

    @commands.command(name='changemymind')
    async def change(self, ctx, *, text):
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}changemymind&text={text}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))

    @commands.command(name='jpeg')
    async def jpeg(self, ctx, url: str = None):
        if not url:
            url = ctx.message.author.avatar_url
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}jpeg&url={url}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))

    @commands.command(name='trump')
    async def trump(self, ctx, *, text):
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}trumptweet&text={text}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))


    @commands.command(name='phcomment', aliases=['ph'])
    async def ph(self, ctx, *, text):
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    f"{self.endpoint}phcomment&image={ctx.message.author.avatar_url}&text={text}&username={ctx.message.author.name}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))
    @commands.command(name='trash')
    async def trash(self, ctx, url: str = None):
        if not url:
            url = ctx.message.author.avatar_url
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}trash&url={url}") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))
    @commands.command(name='magik')
    async def magick(self, ctx, url: str, intensity: int = 10):
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}magik&image={url}&intensity={intensity}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))
    @commands.command(name='deepfry')
    async def df(self, ctx, url: str = None):
        if not url:
            url = ctx.message.author.avatar_url_as(format='png')
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}deepfry&image={url}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))
    @commands.command(name='iphonex', aliases=['iphone'])
    async def ix(self, ctx, url: str = None):
        if not url:
            url = ctx.message.author.avatar_url
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}iphonex&url={url}") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))
    @commands.command(name='captcha', aliases=['cp'])
    async def cp(self, ctx, url, text):
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    f"{self.endpoint}captcha&url={url}&username={text}&raw=2") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))
    @commands.command(name='fact')
    async def fact(self, ctx, *, text: str = None):
        if not text:
            text = f"fucking {ctx.message.author.name} didn't give any arguments so now theyre left with this gay ass meme (BTw: use 'text' argument next time)"
        msg = await ctx.send(embed=await macro.send("This might take a couple of seconds, standby..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{self.endpoint}fact&text={text}") as re:
                res = await re.json()
                await sleep(1)
                await msg.edit(embed=await macro.img(image=res['message']))

def setup(bot: commands.Bot):
    bot.add_cog(MemesAndShitDude(bot))
