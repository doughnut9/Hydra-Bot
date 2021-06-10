import discord
import os
from discord.ext import commands, tasks



bot = commands.Bot(command_prefix=">")



class Help(commands.Cog):
  def __init__(self, bot):
    self.bot=bot



    #Help
    @bot.command()
    async def help(ctx, *, category=None):
        if category == None:
          embed = discord.Embed(
            colour=discord.Colour.orange(),
            title="Help Commands for Hydra Bot",
            url = "https://docs.google.com/document/d/1p1FBEqOhmvIu4otkF2YuqD_mdAnekWctFBq07UjKxbc/edit?usp=sharing"
          )

          embed.set_author(name="doughnut#3968", url="https://discord.gg/8tcHNurFjp", icon_url="https://sites.google.com/site/12untitled7/_/rsrc/1298297964945/home/sasori/Sasori.jpg")
          embed.set_thumbnail(url="https://i.gifer.com/VR0F.gif")
          embed.add_field(name="Moderation", value = "Moderation Commands, `>help moderation`", inline = False)
          embed.add_field(name="Entertainment", value = "Entertainment Commands, `>help entertainment`", inline = False)
          embed.add_field(name="Ping", value = "Displays the latency of the bot - `>ping`", inline = False)
          embed.add_field(name="Misc", value = "More features coming soon.", inline = True)
          embed.set_footer(text = '----------------------------------------------------------------------------------------------\nThe bot is currently under development and more commands will be added soon!\n[] - Reqired Arguments   &   {} - Optional Arguments\n')

        if category == "moderation":
          embed = discord.Embed(
          colour=discord.Colour.orange(),
          title="Moderation Commands for Hydra Bot",
          url = "https://docs.google.com/document/d/1p1FBEqOhmvIu4otkF2YuqD_mdAnekWctFBq07UjKxbc/edit?usp=sharing"
           )
          embed.add_field(name="Moderation", value = "Kick - Kicks a member\n`>kick [member] {reason}`\n\nBan - Bans a member\n`>ban [member] {reason}`\n\nUnban - Unbans a member\n`>unban [member]`\n\nPurge - Deletes the given amount of messages\n`>purge {amount}`\n\n Mute - Mutes the given member\n`>mute [member] {reason}`\n\n>Prefix - Changes the prefix of the server.\n`>prefix [new prefix]`", inline = False)
          embed.set_footer(text = '----------------------------------------------------------------------------------------------\nThe bot is currently under development and more commands will be added soon!\n[] - Reqired Arguments   &   {} - Optional Arguments\n')

        elif category == "entertainment":
          embed = discord.Embed(
            colour=discord.Colour.orange(),
            title="Entertainment Commands for Hydra Bot",
            url = "https://docs.google.com/document/d/1p1FBEqOhmvIu4otkF2YuqD_mdAnekWctFBq07UjKxbc/edit?usp=sharing"
           )
          embed.add_field(name="Entertainment", value = "8Ball - Tells whether the question you asked is true or false.\n`8b [question]`\n\nAvatar - Displays the avatar of a user\n`>avatar [member]`\n(If no member is provided, it will display the avatar of the user who used the command.", inline = False)
          embed.set_footer(text = '----------------------------------------------------------------------------------------------\nThe bot is currently under development and more commands will be added soon!\n[] - Reqired Arguments   &   {} - Optional Arguments\n')
      
        await ctx.send(embed=embed)
          

def setup(bot):
  bot.add_cog(Help(bot))
