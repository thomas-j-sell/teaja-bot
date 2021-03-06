from config import bot
from command_utils import CommandGenerator


@bot.command(name='socials', aliases=['social'])
async def socials(ctx):
    await ctx.send("Hey! Listen! If you want to keep up with me on social media you can follow on these platforms: twitter.com/teaja | tiktok.com/@dredgen_teaja | instagram.com/dredgen_teaja")

# individual socials
social_commands = {
        'twitter':   'twitter.com/teaja',
        'tiktok':    'tiktok.com/@dredgen_teaja',
        'instagram': 'instagram.com/dredgen_teaja'
        }

for cmd, response in social_commands.items():
    CommandGenerator(cmd, response)

##################
# gaming accounts
# TODO determine if I actually want to invite viewers to friend me
##################
# @bot.command(name='accounts', aliases=['account'])
# async def accounts(ctx):
#     await ctx.send('PSN: teaja, Epic: dredgen_teaja, Activision: teaja#7667376, riot: TBD')

# gaming_account_commands = {
#         'psn'        : 'PSN: teaja',
#         'epic'       : 'Epic: dredgen_teaja',
#         'activision' : 'Activision: teaja7667376'
#         }

# # use command generator to build commands
# for cmd, response in gaming_account_commands.items():
#     CommandGenerator(cmd, response)


########################
# team pyramid commands
########################
@bot.command(name='pyramid', aliases=['pyrmd'])
async def pyramid(ctx):
    await ctx.send("You can connect with and support Team Pyramid by: joining the discord https://discord.gg/FwMhsgp -- using the Epic creator code: pyrmd -- buying merch: https://pyrmd-design.myshopify.com/ -- or most importanly, just hanging out in stream.")

team_commands = {
        'cc' : 'You can support Team Pyramid by using the Epic creator code: "pyrmd"',
        'discord' : 'Come hang out with Teaja and the other members of Team Pyramid in our Discord! https://discord.gg/FwMhsgp',
        }

# use command generator to build commands
for cmd, response in team_commands.items():
    CommandGenerator(cmd, response)


################
# gear commands
################
@bot.command(name='pc', aliases=['specs'])
async def pc(ctx):
    await ctx.send('NZXT Streaming PC --- CASE: NZXT H510 (Black) --- MOTHERBOARD: MSI B450 TOMAHAWK --- CPU: AMD Ryzen 7 3700X 8-Core 3.6GHz --- CPU COOLING: AMD Wraith Prism --- GPU: GIGABYTE GeForce RTX 2070 Super WINDFORCE OC 3X 8G --- RAM: Team T-FORCE Vulcan Z 16GB (2 x 8GB) 3200MHz --- SSD: Intel 660p (1.0 TB) --- POWER SUPPLY: 650W Bronze PSU')

gear_commands = {
        'monitor'    : 'ASUS VG278QR 27" 1080p 165Hz 0.5ms',
        'camera'     : 'Razer Kiyo',
        'headphones' : 'HyperX Cloud II',
        'controller' : 'Scuf Impact',
        'keyboard'   : 'Logitech Pro',
        'mouse'      : 'Logitech G502 Lightspeed',
        'mic'        : 'Blue Yeti X'
        }

# use command generator to build commands
for cmd, response in gear_commands.items():
    CommandGenerator(cmd, response)


#####################
# Story game commands
#####################
@bot.command(name='recap')
async def recap(ctx):
    await ctx.send("I need a recap please. (use !recap if you are ever lost or confused about the current story and Teaja will do his best to catch you up.)")

@bot.command(name='safeword')
async def safeword(ctx):
    await ctx.send("My safeword is 'Chupacabra'. This is a first playthrough and I don't want any back seating or spoilers. Unless I use my safeword all questions are retorical.")


@bot.command(name='brb')
async def brb(ctx):
    await ctx.send("I have to step away for a moment, but I'll be right back. Would you kindly stick around?")

@bot.command(name='back')
async def back(ctx):
    await ctx.send("I'm back. Stay awhile and listen.")

@bot.command(name='prime')
async def prime(ctx):
    await ctx.send("If you have Amazon Prime, you can link your Amazon account to your Twitch account to get some free stuff: free games, exlcusive in game items, and a free subscription you can give to any streamer. Visit gaming.amazon.com to get started. NOTE: that prime subscriptions do not automatically renew, so you'll have to manually reapply them each month.")


@bot.command(name='podcast')
async def podcast(ctx):
    await ctx.send("@dudeitsmefam hosts a podcast on his twitch channel every week on Wednesday at 6:30 et, 5:30 ct. Guests discuss streamer oriented topics. Please check it out. twitch.tv/dudeitsmefam")

