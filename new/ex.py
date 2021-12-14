import discord
import json
import requests

async def fox(atx):
    response = requests.get('https://somoskudasai.com/wp-content/uploads/2019/03/sewayakikitsunenosenkosan.jpg')
    json_data = json.loads(response.text)
    
    embed = discord.Embed(title='Fox', description='', color=0xff9900)
    embed.set_image(url=json_data['url'])
    await atx.send(embed=embed)