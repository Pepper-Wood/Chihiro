import discord

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        # Discord channel IDs
        chs = {
            '#art-feed': 734943046474530856
        }

        # Iterate through recent messages in channel
        async for message in self.get_channel(chs['#art-feed']).history(limit=200):
            # 
            print(message.author)
            for attach in message.attachments:
                print(attach.url)
            for react in message.reactions:
                print(react.emoji)
            await message.add_reaction("🎉")

discord_client = DiscordClient()
discord_client.run(DISCORD_TOKEN)
