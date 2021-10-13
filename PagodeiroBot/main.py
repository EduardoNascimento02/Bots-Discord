import keep_alive
import discord
import music
from discord.ext import commands
import random
import os
import datetime
from datetime import timedelta, timezone, datetime
from time import sleep

listaGuildeID = [
  672496995688120351,
  813177135744679949
]
cogs = [music]

activity = discord.Activity(type=discord.ActivityType.playing,
                          name='!comandos')

client = commands.Bot(command_prefix='!',
                    intents=discord.Intents.all(),
                    activity=activity,
                    status=discord.Status.idle)

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.command()
async def serverID(ctx):
  id = ctx.message.guild.id
  await ctx.send(id)


#--------------------------on_ready-----------------------
@client.event
async def on_ready():
    print('Pagodeiro ficou on the line')
    print(f'{client.user.name} - {client.user.id}')

#-------------------------Juliette------------------------
NomesJuliette = [
    'mobilete', 'juliette',
    'juliete', 'julliete',
    'julliette', 'jul|ette',
    'jull|ette', 'jul|ete',
    'julliette', 'jul1ete',
    'jull1ete', 'jul1ette',
    'jull1ette', 'JuIIiette',
    'juliэtte', 'Jüliette',
]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if isinstance(message.content, str) is True:
        if (message.content).lower() in NomesJuliette:
            await message.channel.send(
                f'Não pode falar J-word,  {message.author.name}!!')
            await message.delete()
    await client.process_commands(message)


# sdjakdçawjdadjowa
@client.command()
async def twink(ctx):
  id = ctx.message.guild.id
  if id in listaGuildeID:
    twinkname = ['Kauã', 'Pedro']
    ofensas = ['padrão','radpass','radtop','bluepill','unbased','jorge','normie']
    await ctx.send(f'O {twinkname[random.randint(0, 1)]} é um twink {ofensas[random.randint(0,6)]}')
#-------------------------------------------------------------

#----------------------- DIAS DE AULA ------------------------
imagensAulas = [
  'https://media.discordapp.net/attachments/893180187901046917/893190742992900146/unknown.png',
  'https://media.discordapp.net/attachments/893180187901046917/893190823041179648/unknown.png',
  'https://media.discordapp.net/attachments/893180187901046917/893190876338192384/unknown.png',
  'https://media.discordapp.net/attachments/893180187901046917/893190917471752263/unknown.png',
  'https://media.discordapp.net/attachments/893180187901046917/893190976301052004/unknown.png'
]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
hours = ['7:00', '7:50', '8:40', '9:30', '10:20', '10:40', '11:30']

materias = ['Artes', 'Biologia', 'Educação Física', 'Filosofia', 'Física', 'Geografia', 'História', 'Língua Inglesa', 'Língua Portuguesa', 'Matemática', 'Programação e Robótica', 'Química', 'Sociologia']
calendarioAulas = [
  ['História', 'Matemática', 'Educação Física', 'Sociologia', 'Intervalo', 'Programação e Robótica', 'Filosofia'],
  ['Química', 'Física', 'Química', 'Língua Portuguesa', 'Intervalo', 'Matemática', 'Língua Inglesa'],
  ['Educação Física', 'Geografia', 'Geografia', 'Eixo Integrador', 'Intervalo', 'Matemática', 'Língua Portuguesa'],
  ['Filosofia', 'Sociologia', 'Artes', 'Física', 'Intervalo', 'Biologia', 'Biologia'],
  ['Português', 'História', 'Língua Inglesa', 'Artes', 'Intervalo', 'Língua Portuguesa', 'Matemática']
]
aulas = list()

professores = {
'Professora Rex': ['Língua Inglesa', 'https://media.discordapp.net/attachments/672496996178984970/890926920030621716/IMG_20210924_084513.jpg?width=355&height=473'],
'Professor Alex': ['Sociologia Filosofia', 'https://media.discordapp.net/attachments/893180187901046917/895074534988865566/image.png'],
'Professora Andreza': ['Física', 'https://media.discordapp.net/attachments/893180187901046917/895074559500369920/image.png'],
'Professor Bruno': ['Biologia', 'https://media.discordapp.net/attachments/893180187901046917/895074590873747486/image.png'],
'Professora Fernanda': ['Matemática Programação e Robótica', 'https://media.discordapp.net/attachments/893180187901046917/895076735928918126/image.png'],
'Professora Kátia': ['Artes', 'https://media.discordapp.net/attachments/893180187901046917/895076758368444447/image.png'],
'Professora Lizandra': ['Geografia', 'https://media.discordapp.net/attachments/893180187901046917/895076781969793074/image.png'],
'Professor Luís Gustavo': ['Química', 'https://media.discordapp.net/attachments/893180187901046917/895076800445706290/image.png'],
'Professora Nádia': ['Língua Portuguesa', 'https://media.discordapp.net/attachments/893180187901046917/895076821379477514/image.png'],
'Professor Ricardo': ['História', 'https://media.discordapp.net/attachments/893180187901046917/895076844821430412/image.png'],
'Professora Tatiane': ['Educação Física', 'https://media.discordapp.net/attachments/893180187901046917/895256744484282389/image.png'],
'Hora do Intervalo!': ['Intervalo', 'https://media.discordapp.net/attachments/893180187901046917/895292678948913162/unknown.png?width=473&height=473']
}


@client.event
async def adviser():
  hoje = datetime.now.strftime("%d")
  for c in range(0, 5):
    if hoje is days[c]:
      aulas = calendarioAulas[c]
      proximaAula = calendarioAulas[c+1]
  inicio = (f'{datetime.now.strftime("%H")}:{datetime.now.strftime("%M")}')
  for professor, materiaFOTO in professores.items():
    for c in range(0, 6):
      if inicio == hours[c]:
        fim = (hours[c+1])
        aulaAtual = aulas[c]
        hora = f'{inicio} - {fim}'
        channel = client.get_channel(894595248213340262)
        embed = discord.Embed(
          title = f'Aula de {aulaAtual}',
          description = "Aviso automático de aulas",
          color = 0xFFCBDB
        )
        embed.set_author(name = client.user.name, icon_url=client.user.avatal_url)
        embed.set_thumbnail("https://media.discordapp.net/attachments/893180187901046917/895313969504456764/04GaB8gAAAABJRU5ErkJggg.png?width=473&height=473")
        embed.ser_footer(text=f'Feito por {client.user.name}', icon_url=client.user.avatar_url)
        # FIELD
        embed.add_field(name='Professor', value=professor)
        embed.add_field(name='Horário da aula', value=hora)
        embed.add_field(name='Próxima aula', value=proximaAula, inline=False)

        embed.set_image(url=materiaFOTO[1])

        await channel.send(embed=embed)
      

@client.command()
async def aula(ctx):
  id = ctx.message.guild.id
  if id in listaGuildeID:
    now = datetime.now()
    hoje = now.strftime("%A")
    for c in range(0, 5):
      if hoje == days[c]:  
          await ctx.send(imagensAulas[c])
      elif hoje not in days:
          await ctx.send('Hoje não tem aula')


#-------------------------- RICHARD -----------------------------
frasesRichard = ['Richard, vá tomar no cu','Richard, vai estudar desocupado','Richard, já pensou em se fuder hoje?','Quem te perguntou Richard? kkkkkj']

@client.command(name='richard')
async def richard(ctx):
  id = ctx.message.guild.id
  if id in listaGuildeID:
      message = frasesRichard[random.randint(0, 3)]

      await ctx.send(message)


#----------------------------teste------------------------
@client.command()
async def teste(ctx):
    await ctx.send('Bom dia')

#------------------------dado-6---------------------------
ImagensDado = [
    'https://cdn.discordapp.com/attachments/891802158209597440/892604430560661504/unknown.png',
    'https://cdn.discordapp.com/attachments/891802158209597440/892604854223142962/unknown.png',
    'https://cdn.discordapp.com/attachments/891802158209597440/892605059383296090/unknown.png',
    'https://cdn.discordapp.com/attachments/891802158209597440/892605317848907786/unknown.png',
    'https://cdn.discordapp.com/attachments/891802158209597440/892605458278416384/unknown.png',
    'https://cdn.discordapp.com/attachments/891802158209597440/892605655519735828/unknown.png'
]



#------------------------ DATA ---------------------------
@client.command()
async def current_time(ctx):
    data_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fusoHorario = timezone(diferenca)
    now = data_hora_atuais.astimezone(fusoHorario)
    now = data_hora_atuais.strftime('%d/%m/%Y às %H:%M:%S')

    await ctx.send(f'Data atual: {now}')

# ----------------------- DADO ---------------------------
@client.command()
async def d6(ctx):
    dado6 = random.randint(0, 5)
    await ctx.send('Dado rodando...')
    for c in range(0, 6):
        if c == dado6:
            sleep(1)
            await ctx.send(f'Caiu {dado6+1}')
            await ctx.send(ImagensDado[c])


#-------------------------Random-image---------------------
@client.command(name='foto')
async def get_random_image(ctx):
  url_image = 'https://picsum.photos/1920/1080'

  embed = discord.Embed(
    title = 'Gerando uma imagem aleatoria',
    description = '--------------------',
    color = 0xffcbdb,
  )
  embed.set_author(name=client.user.name,icon_url=client.user.avatar_url)
  embed.set_footer(text='Gerado por:' + client.user.name,icon_url=client.user.avatar_url)
  embed.set_image(url=url_image)

  embed.add_field(name='API', value='API usada: https://picsum.photos' )
  await ctx.send(embed=embed)
#-------------------------ManipularImagens------------------------
#------------------------dado-20--------------------------
@client.command()
async def d20(ctx):
    dado20 = random.randint(1, 20)
    await ctx.send('Dado rodando...')
    sleep(1)
    await ctx.send(f'Caiu {dado20}')


#------------------------CARA-OU-COROA--------------------
@client.command()
async def moeda(ctx):
    await ctx.send('Moeda girando...')
    sleep(1)
    CouC = random.randint(1, 2)
    if CouC == 1:
        await ctx.send('Deu cara 😀')
    else:
        await ctx.send('Deu coroa 👑')


#--------------------- AVATAR -------------------------



#-----------------------Manipular imagem----------------





class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command






#-------------------------COMANDOS------------------------
@client.command()
async def comandos(ctx):
  await ctx.send('''Os comandos para o bot pagodeiro são:
```
COMANDO                       FUNCIONALIDADE

!moeda                        Um cara e coroa 
!d6                           rola um dado de 6 faces
!d20                          rola um dado de 20 faces
!play (link)                  toca a música do link enviado
!pause                        pausar a música
!resume                       volta a tocar a música pausada
!leave                        sai do canal de voz
```''')
my_secret = os.environ['Toke']
keep_alive.keep_alive()
client.run(my_secret)

