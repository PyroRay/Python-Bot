#Discord bot token: Njk4NjAzMTQ3MzQxNTk0NjM0.XpIPMw.tdEboO2luWEdHnlMAzFtvRCTL9U

import discord

client = discord.Client()
prefix = '!!'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello!')
    elif message.content == (prefix + 'terminate'):
        import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        await client.close()
    # elif message.content == (prefix + 'changeprefix'):
    #     await message.channel.send('What prefix would you like to use?')

client.run('Njk4NjAzMTQ3MzQxNTk0NjM0.XpIPMw.tdEboO2luWEdHnlMAzFtvRCTL9U')
