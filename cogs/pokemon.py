from discord.ext import commands
import discord
from libs import pokemon


class PokeDex(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name='pokedex')
    async def pokedex(self, ctx):
        if not ctx.invoked_subcommand:
            pass

    @pokedex.command(name='pokemon')
    async def pokemon(self, ctx, identifier):
        poke = pokemon.pokemon(identifier=identifier)
        embed = discord.Embed(
            title=f"{poke.get('name')} | PokeDex entry no. {poke.get('pokedex')}",
            color=discord.Color.blurple()
        )
        stats = poke.get('base_stats')
        embed.add_field(name="Type(s)", value="".join("``" + _type + "``, " for _type in poke.get('types')),
                        inline=True)
        embed.add_field(name='Height', value='``' + poke.get('height') + '``', inline=True)
        embed.add_field(name='Weight', value='``' + poke.get('weight') + '``', inline=True)
        embed.add_field(name='Ability/Abilities',
                        value="".join('``' + ability + '``, ' for ability in poke.get('abilities')), inline=True)
        embed.add_field(name='Game Indices', value="".join('``' + indice + '``, ' for indice in poke.get('indices')),
                        inline=True)
        embed.add_field(name='Base Statistics', value=f"Speed: ``{stats[0]}``, Special-Defense: ``{stats[1]}``, "
                                                      f"Special-Attack: ``{stats[2]}``, Defense: ``{stats[3]}``, "
                                                      f"Attack: ``{stats[4]}``, HP: ``{stats[5]}``", inline=True)
        embed.set_thumbnail(url=poke.get('sprite'))
        await ctx.send(embed=embed)

    @pokedex.command(name='berry')
    async def berry(self, ctx, identifier):
        berri = pokemon.berry(identifier=identifier)
        embed = discord.Embed(
            title=f"{berri.get('name').title()} Berry | ID: {berri.get('id')}",
            color=discord.Color.blurple()
        )
        embed.add_field(name='Firmness', value=berri.get('firmness').title())
        embed.add_field(name='Growth Process', value=f"{berri.get('growth-time')} Max harvest: ``{berri.get('max')}`` berries.")
        embed.add_field(name='Size', value=berri.get('size'))
        embed.add_field(name='Smoothness', value=berri.get('smoothness'))
        embed.add_field(name='Flavors', value=berri.get('flavors'))
        embed.add_field(name='Natural Gift', value=berri.get('natural-gift'))
        await ctx.send(embed=embed)
    @pokedex.command(name='type')
    async def type(self, ctx, identifier):
        typ = pokemon.type(identifier)
        embed = discord.Embed(
            title=f"{typ.get('name').title()} | ID: {typ.get('id')}",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Effective Against", value=typ.get('double_damage_to'), inline=True)
        embed.add_field(name="Not Effective Against", value=typ.get('half_damage_to'), inline=True)
        embed.add_field(name="Not Effecting", value=typ.get('no_damage_to'),inline=True)

        embed.add_field(name='Weak To', value=typ.get('double_damage_from'), inline=True)
        embed.add_field(name='Not Effective To', value=typ.get('half_damage_from'),inline=True)
        embed.add_field(name='Not Effecting To', value=typ.get('no_damage_from'), inline=True)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(PokeDex(bot))
