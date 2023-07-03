import discord
from discord.ext import commands
import os
import random
import webbrowser as web
import vlc
import time
import requests

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak

intents = discord.Intents.default()

# Mesajları okuma ayrıcalığını etkinleştirelim

intents.message_content = True

# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım

client = discord.Client(intents=intents)
       

client = commands.Bot(intents=intents,command_prefix="!")

@client.command()
async def mem(ctx):
    secilen_dosya = random.choice(os.listdir('images'))

    f = open(f'images/{secilen_dosya}', "rb")

    mem = discord.File(f)

    await ctx.send(file=mem)

@client.command()
async def müzik(ctx):
    secilen_dosya = random.choice(os.listdir('musics'))

    f = open(f'musics/{secilen_dosya}', "rb")

    musics = discord.File(f)

    await ctx.send(file=musics)

def köpeks():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json() 
    return data['url']
   

@client.command('köpek')
async def köpek(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = köpeks()
    await ctx.send(image_url)
def ördeks():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@client.command("ördek")
async def ördek(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = ördeks()
    await ctx.send(image_url)




