from discord.ext import commands
import discord
from libs import macro
import aiohttp
import asyncio

class News(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.group(name='news')
    async def news(self, ctx):
        if not ctx.invoked_subcommand:
            await ctx.send(embed=await macro.send(title="News Usage", desc="``p!news search [query]`` - Searches all news by entered keywords.\n``p!news top`` - Gets the top headlines in the US."))
    @news.command(name='headlines', aliases=['top'])
    async def top(self, ctx):
        msg = await ctx.send(embed=await macro.send("Getting news..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://newsapi.org/v2/top-headlines?country=us&apiKey=8ffb86c6f31943f8889b1c84687b48b6') as re:
                re = await re.json()
                embed = discord.Embed(
                    type='rich',
                    title='Top News Headlines for the US',
                    color=discord.Color.blurple()
                )
                embed.add_field(name=f"1. {re['articles'][0]['title']}",
                                value=f"[{re['articles'][0]['description']}]({re['articles'][0]['url']})")
                embed.add_field(name=f"2. {re['articles'][1]['title']}",
                                value=f"[{re['articles'][1]['description']}]({re['articles'][1]['url']})")
                embed.add_field(name=f"3. {re['articles'][2]['title']}",
                                value=f"[{re['articles'][2]['description']}]({re['articles'][2]['url']})")
                await asyncio.sleep(1)
                await msg.edit(embed=embed)
    @news.command(name='search')
    async def search(self, ctx, *, query):
        msg = await ctx.send(embed=await macro.send("Getting news..."))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey=8ffb86c6f31943f8889b1c84687b48b6") as re:
                re = await re.json()
                await asyncio.sleep(1)
                if re['totalResults'] < 3:
                    return await msg.edit(embed=await macro.error(f'No results were found for {query}'))
                embed = discord.Embed(
                    type='rich',
                    title=f'Top News Headlines for {query}',
                    color=discord.Color.blurple()
                )
                embed.add_field(name=f"1. {re['articles'][0]['title']}",
                                value=f"[{re['articles'][0]['description']}]({re['articles'][0]['url']})")
                embed.add_field(name=f"2. {re['articles'][1]['title']}",
                                value=f"[{re['articles'][1]['description']}]({re['articles'][1]['url']})")
                embed.add_field(name=f"3. {re['articles'][2]['title']}",
                                value=f"[{re['articles'][2]['description']}]({re['articles'][2]['url']})")
                await asyncio.sleep(1)
                await msg.edit(embed=embed)



def setup(bot):
    bot.add_cog(News(bot))
