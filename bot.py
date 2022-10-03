import discord
from asgiref.sync import sync_to_async
from discord.ext import commands, tasks
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "discord_acmicpc_bot.settings")
import django

django.setup()
from acmicpc.models import Member

import requests
from bs4 import BeautifulSoup as bs

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@tasks.loop(seconds=5)
async def worker1():
    res = requests.get('https://www.acmicpc.net/group/ranklist/3324')
    if res.status_code == 200:
        html = res.text
        parser = bs(html, 'html.parser')
        rows = parser.select('#ranklist > tbody > tr')
        for row in rows:
            user_id = row.select_one('td:nth-child(2)').text
            solved = row.select_one('td:nth-child(4)').text
            member = Member(user_id, solved)
            await sync_to_async(member.save, thread_sensitive=True)()


@tasks.loop(seconds=1)
async def worker2():
    print('worker2')
    channel = bot.get_channel(int(os.environ['DISCORD_CHANNEL_ID']))
    # await channel.send('test')


@bot.command(name='활성화')
async def _activate(ctx):
    worker1.start()
    worker2.start()
    await ctx.send('활성화되었습니다.')


@bot.command(name='순위')
async def _rank(ctx):
    members = await sync_to_async(list)(Member.objects.all().order_by('-solved'))
    ranks = []
    rank = 1
    for member in members:
        ranks.append(f'{rank}등 - {member.user_id} ({member.solved})')
        rank = rank + 1
    await ctx.send('\n'.join(ranks))


bot.run(os.environ['DISCORD_TOKEN'])
