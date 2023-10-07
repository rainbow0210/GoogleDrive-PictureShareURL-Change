import discord
import os
from dotenv import load_dotenv
from discord.commands import Option

bot = discord.Bot()
load_dotenv()

@bot.event
async def on_ready():
    print(f'{bot.user} connect success!')


@bot.slash_command(description="Google drive picture share link change embeddable link. (Use example: html <img tag>)")
async def change_url(
    ctx,
    share_url: Option(str, 'Google Drive Share link typing'),
):
    url = share_url
    if url[0:25] == 'https://drive.google.com/':
        # debug message start
        print('-Change start-')
        print('')

        print(url)
        print('')

        url = url[32:]
        print(url)
        print('')

        url = url[:-20]
        print(url)
        print('')

        url = 'http://drive.google.com/uc?export=view&id=' + url
        print(url)
        print('')

        print('-Change finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Success!", description=":o:Change URL!:o:", color=0x00ff2a)
        embed.add_field(name="This copy Link!", value=url, inline=True)
        embed.set_footer(text="※If this link doesn't work, it's possible that the link you entered wasn't for the image.")
        await ctx.respond(embed=embed)
    
    else:
        # debug message start
        print('-Change start!-')
        print('')

        print('Error!')
        print('')

        print('-Change finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Error!", description=":x:Not Google Drive Link!:x:", color=0xff0000)
        await ctx.respond(embed=embed)

bot.run(os.environ['token'])