import discord
from discord.ext import commands,tasks
import random
import time
import use_token
import aiohttp


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.get_channel(1138898309206003855).send(f'Είμαι το {bot.user.display_name} και μόλις ξεκίνησα')

# executes the function hello every x seconds after initiation
@tasks.loop(seconds=30)
async def hello():
    nowtime = time.time()
    print (f"hello the time is {nowtime}")

#initiates the loop of hello function and informs the user
@bot.command()
async def start_loop(ctx,arg):
    if int(arg) == 1:
        hello.start()
        boo = "ok"
        await ctx.send(boo)
        
#stops the loop of hello function and informs the user
@bot.command()
async def stop_loop(ctx,arg):
    if int(arg) == -1:
        hello.cancel()
        boo = "ok"
        await ctx.send(boo)
        
#Producing a random integer of length arg
@bot.command()
async def quik_mafs(ctx,arg):
    rand = int(round(random.random()*10**(int(arg))))
    await ctx.send(rand)



@bot.command()
async def get_data(ctx):
    url = "https://content.guardianapis.com/search?q=music&api-key="+use_token.api_key #mporoume na valoume kai kapoio arg opote na kanei search sygkekrimeno anti gia music
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                
                await ctx.send(f'Status: {"HRTHE!"}')
            else:
                await ctx.send(f'Error: {resp.status}')


bot.run(use_token.token)