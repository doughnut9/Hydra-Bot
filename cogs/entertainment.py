import discord
import os
from discord.ext import commands
import random


bot = commands.Bot(command_prefix="$")

class Entertainment(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  #Avatar
  @bot.command(aliases=["av"])
  async def Avatar(self, ctx,*, member : discord.Member=None):
      useravatar = member.avatar_url
      embed = discord.Embed(Colour = discord.Colour.orange(), title = f"Avatar for {member}", url = useravatar)
      embed.set_image(url = f"{useravatar}")
      await ctx.send(embed=embed)


  #8Ball
  @bot.command(aliases=['8ball', '8b'])
  async def _8ball(self, ctx, *, question):
      responses = ["It is certain",
                   "It is decidedly so",
                   "Without a doubt",
                   "Yes, definitely",
                   "You may rely on it",
                   "As I see it, yes",
                   "Most likely",
                   "Outlook good",
                   "Yes",
                   "Signs point to yes",
                   "Reply hazy try again",
                   "Ask again later",
                   "Better not tell you now",
                   "Cannot predict now",
                   "Concentrate and ask again",
                   "Don't count on it",
                   "My reply is no",
                   "My sources say no",
                   "Outlook not so good",
                   "Very doubtful"]
      await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

  @_8ball.error
  async def _8ball_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please ask a question.')


def setup(bot):
  bot.add_cog(Entertainment(bot))
