from config import bot

@bot.command(name='source')
async def source(ctx):
    await ctx.send('I am a bot created by Dredgen_Teaja. You can see the code that makes me work at https://github.com/thomas-j-sell')

@bot.command(name='blurg')
async def blurg(ctx):
    await ctx.send('blurg')

