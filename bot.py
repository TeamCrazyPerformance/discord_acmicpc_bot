import discord
from discord.ext import commands
import os

import requests
from bs4 import BeautifulSoup as bs

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command(name='순위')
async def _rank(ctx):
    message = '오류로 인해 순위를 가져올 수 없습니다.'

    res = requests.get('https://www.acmicpc.net/group/ranklist/3324')
    if res.status_code == 200:
        html = res.text
        parser = bs(html, 'html.parser')
        rows = parser.select('#ranklist > tbody > tr')
        ranks = list(map(lambda row: row.select_one('td:nth-child(1)').text + '등 - ' + row.select_one('td:nth-child(2)').text + ' (' + row.select_one('td:nth-child(4)').text + ')', rows))
        message = '\n'.join(ranks)

    await ctx.send(message)

bot.run(os.environ['DISCORD_TOKEN'])
