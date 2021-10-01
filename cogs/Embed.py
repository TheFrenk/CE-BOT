import discord
from discord.ext import commands

class Embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='embed-say',
                    aliases=['embed'],
                    usage='<Заголовок> [Описание] [Авторы] [Цвет]',
                    description=f'''Правильно будет, конечно, использовать в таком формате: embed-say "Заголовок" "Описание" "Авторы" "HEX-цвет" (**Обязательно в кавычках!!!**).\nПоследние пункты (Описание, авторы, цвет) - опционально.''')
    async def _embed_say(self, ctx, title: str=None, description: str=None, authors: str=None, color: discord.Color=None):
        embed = discord.Embed()
        if description is None:
            embed.title = title
        elif authors is None:
            embed.title = title
            embed.description = description
        elif color is None:
            embed.title = title
            embed.description = description
            embed.set_footer(text=authors, icon_url=ctx.author.avatar_url)
        else:
            embed.title = title
            embed.description = description
            embed.set_footer(text=authors, icon_url=ctx.author.avatar_url)
            embed.color = color
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Embed(client))