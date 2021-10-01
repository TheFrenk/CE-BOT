import json
from typing import Text
import discord
from discord.ext import commands
from apis.code_compiler import compiler
import os

class PythonComiler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def runpy(self, ctx, *args):
        format_args = list(args)

        if not format_args[1].startswith('def'):
            short_code_snipet = ' '.join(format_args[1:-1])
            text_file = open('./databases/source_code.py', 'w')
            text_file.write(short_code_snipet)
            text_file.close()

            os.system("black ./databases/source_code.py")
        else:
            long_code_snippet = ' '.join(format_args[1:-2])
            code_callback_snippet = ''.join(format_args[-2])

            text_file = open('./databases/source_code.py', 'w')
            text_file.write(f'{long_code_snippet}\n{code_callback_snippet}')
            text_file.close()

            os.system("black ./databases/source_code.py")

        text_file = open('./databases/source_code.py', 'r')
        await ctx.send(f"**Вывод**\n```yaml\n{compiler(code=text_file.read())['output']}```")

def setup(client):
    client.add_cog(PythonComiler(client))