from PIL import Image, ImageDraw, ImageFont, ImageOps

avatar = Image.open('pagodeirobit.png')
avatar = avatar.resize((120,120))
bigavatar = (avatar.size[0]*3, avatar.size[1]*3)
mascara = Image.new('L', bigavatar, fill=255)
recortar = ImageDraw.Draw(mascara)
recortar.ellipsis((0,0)+ bigavatar, fill=255)
mascara= mascara.resize(avatar.size, Image.ANTIALIAS)
avatar.putalpha(mascara)

saida = ImageOps.fit(avatar, mascara.size, centering=(0.5,0.5))
saida.putalpha(mascara)
saida.save('avatar.png')


img = Image.open('template.png')
fonte = ImageFont.truetype('fonte.tff',40)
escrever = ImageDraw.Draw(img)
escrever.text(xy=(180,160), text="Richard", fill=(0,0,0), font=fonte)
img.paste(avatar,(40,90), avatar)
