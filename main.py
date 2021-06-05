import discord
import os
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import CheckFailure
from discord.ext.commands import MissingPermissions
import random
from alive import alive



intents = discord.Intents.all()
intents.members = True



bot = commands.Bot(command_prefix="$", intents=intents)
bot.remove_command('help')
my_secret = os.environ['Token']



@bot.event
async def on_ready():
    print("Bot is ready.")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Having A Midlife Crisis...'))



#join_message
@bot.event
async def on_member_join(member):
  guild_id = member.guild.id
  av = member.avatar_url
  if guild_id == 842401531171962911:
    channel = bot.get_channel(842407125329903616)
    e = discord.Embed(color = discord.Color.green())
    e.set_thumbnail(url=av)
    e.add_field(name="Welcome!!", value=f"Welcome to the server {member.mention}!! Hope you have a good time! If you need any help regarding discord, please contact and admins or mods. If you need any help regarding questions, don't hesitate to ask in the doubt channels . And at last, please check self-roles at <#842413732167811152>")
    await channel.send(embed=e)
  else:
    print('Currently Thinking.')



#server_leave
@bot.event
async def on_member_remove(member):
  guild_id = member.guild.id
  if guild_id == 842401531171962911:
    channel = bot.get_channel(842607234160525334)
    e = discord.Embed(color = discord.Colour.red())
    e.set_thumbnail(url=member.avatar_url)
    e.add_field(name="Member Left", value = f"{member} Has left the server.")
    await channel.send(embed=e)
  else:
    print("Currently thinking.")




#NoCommandError
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('No such command exists!')



#Welcome
@bot.command()
async def welcome(ctx):
  await ctx.send(f'Welcome to the server!! Hope you have a good time! For help regarding Discord, please go to <#846802868215218177>. For any subject-regarded help please go to the respective doubts channel in the Doubts category. For a general chit-chat with our community, have fun at <#842407125329903616>!')



#CogLoad
@bot.command()
@commands.has_role('Owner')
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')

@load.error
async def load_error(ctx, error):
  if isinstance(error, commands.MissingRole):
    await ctx.send('Sorry, but you do not have perms to use that command!')



#CogUnload
@bot.command()
@commands.has_role('Owner')
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')

@unload.error
async def unload_error(ctx, error):
  if isinstance(error, commands.MissingRole):
    await ctx.send('Sorry, but you do not have perms to use that command!')



#CogReload
@bot.command()
@commands.has_role('Owner')
async def reload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')

@reload.error
async def reload_error(ctx, error):
  if isinstance(error, commands.MissingRole):
    await ctx.send('Sorry, but you do not have perms to use that command!')



#Ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency*1000)}ms.')



for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')



alive()
bot.run(os.getenv('Token'))
