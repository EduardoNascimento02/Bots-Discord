import discord
import music
from discord.ext import commands
import Token
import random
from time import sleep
cogs = [music]
activity = discord.Activity(type=discord.ActivityType.watching, name='Seu pai aquele gostoso')

client = commands.Bot(command_prefix='!',intents = discord.Intents.all(), activity = activity, status = discord.Status.idle)

for i in range(len(cogs)):
    cogs[i].setup(client)
#--------------------------on_ready-----------------------
@client.event
async def on_ready():
    print('Pagodeiro ficou on the line')
    print(client.user.name, end=' - ')
    print(client.user.id)

#----------------------------teste------------------------
@client.command()
async def teste(ctx):
  await ctx.send('Bom dia')
#------------------------dado-6---------------------------
@client.command()
async def d6(ctx):
  dado6 = random.randint(1,6)
  await ctx.send('Dado rodando...')
  if dado6 == 1:
    sleep(1)
    await ctx.send(f'Caiu {dado6}')
    await ctx.send('https://cdn.discordapp.com/attachments/891802158209597440/892604430560661504/unknown.png')
  elif dado6 == 2:
    sleep(1)
    await ctx.send(f'Caiu {dado6}')
    await ctx.send('https://cdn.discordapp.com/attachments/891802158209597440/892604854223142962/unknown.png')
  elif dado6 == 3:
    sleep(1)
    await ctx.send(f'Caiu {dado6}')
    await ctx.send('https://cdn.discordapp.com/attachments/891802158209597440/892605059383296090/unknown.png')
  elif dado6 == 4:
    sleep(1)
    await ctx.send(f'Caiu {dado6}')
    await ctx.send('https://cdn.discordapp.com/attachments/891802158209597440/892605317848907786/unknown.png')
  elif dado6 == 5:
    sleep(1)
    await ctx.send(f'Caiu {dado6}')
    await ctx.send('https://cdn.discordapp.com/attachments/891802158209597440/892605458278416384/unknown.png')
  elif dado6 == 6:
    sleep(1)
    await ctx.send(f'Caiu {dado6}')
    await ctx.send('https://cdn.discordapp.com/attachments/891802158209597440/892605655519735828/unknown.png')    
#------------------------dado-20--------------------------
@client.command()
async def d20(ctx):
  dado20 = random.randint(1,20)
  await ctx.send('Dado rodando...')
  if dado20 == 1:  
    sleep(1)
    await ctx.send(f'Caiu {dado20}')
#------------------------CARA-OU-COROA--------------------
@client.command()
async def moeda(ctx):
  await ctx.send('Moeda girando...')
  sleep(1)
  CouC = random.randint(1,2)
  if CouC == 1:
    await ctx.send('Deu cara 😀')
  else:
    await ctx.send('Deu coroa 👑')
#-------------------------COMANDOS------------------------
@client.command()
async def comandos(ctx):
  await ctx.send('''Os comandos para o bot pagodeiro são:
```!moeda - Um cara e coroa 
!d6 - rola um dado de 6 faces
!d20 - rola um dado de 20 faces
!richard - supostamente deveria mandar o Richars ser homofobico
!entrar - ele entra na call, pronto pra tocar um pagode do bom
!play (link) - toca a música perfeitamente
!pause - você realmente quer parar o pagode?
!resume - que o pagode continue!!
!leave - por que vc quer que ele saia?```''')

client.run(Token.seu_token())