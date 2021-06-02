import discord
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from discord.ext.commands import CheckFailure
from discord.ext.commands import MissingPermissions



bot = commands.Bot(command_prefix="$")



class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot=bot



  #Mute
  @bot.command()
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")



  #ban
  @bot.command(aliases=["b"])
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(str(member) + " has been banned. \n" + "Reason - " + str(reason) )

  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
      await ctx.send('Please mention the user to be banned.')
    if isinstance (error, commands.MissingPermissions):
      await ctx.send('Aha comrade, that one is not for you.')



  #purge
  @bot.command(aliases=["clean", "delete", "p"])
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, amount : int):
    if amount < 0:
      await ctx.send("Please enter a valid value.")
    if amount > 0:
      await ctx.channel.purge(limit=amount)
      await ctx.send(str(amount) + ' messages have been deleted.')

  @purge.error
  async def purge_error(self, ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
      await ctx.send('Please tell number of messages to be deleted.')
    if isinstance (error, commands.MissingPermissions):
      await ctx.send('Aha comrade, that one is not for you.')



  #kick
  @bot.command(aliases=["k"])
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(str(member) + " has been kicked. \n" + "Reason - " + str(reason) )

  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
      await ctx.send('Please mention the user to be kicked.')
    if isinstance (error, commands.MissingPermissions):
      await ctx.send('Aha comrade, that one is not for you.')



  #unban
  @bot.command(aliases=["u"])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user=ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
        return

  @unban.error
  async def unban_error(self, ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
      await ctx.send('Please mention the user to be unbanned.')
    if isinstance (error, commands.MissingPermissions):
      await ctx.send('Aha comrade, that one is not for you.')



def setup(bot):
  bot.add_cog(Moderation(bot))
