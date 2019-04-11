from discord.ext import commands
import discord
import aiohttp
from libs import macro


class Space(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
  @commands.group(name='space')
  async def space(self, ctx):
    if not ctx.invoked_subcommand:
      pass
  @space.command(name='picoftheday', aliases=['apod', 'pod'])
  async def apod(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get("https://api.nasa.gov/planetary/apod?hd=true&api_key=fp1T0XcFRai0RSjAF7uuDKZ6hTRxt6va6qdSrzeX") as res:
        res = await res.json()
        await ctx.send(embed=await macro.img(res['hd_url'], title=f"{res['title']} | {res['date']}", desc=res['explanation']))
  def setup(bot:commands.Bot):
    bot.add_cog(Space(bot))
  
