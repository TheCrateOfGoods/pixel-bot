#User commands v1.0.1
from discord.ext import commands

from bot_globals import version, bot_masters, server_list
from checks import *

class User():
    def __init__(self, bot):
        self.bot = bot
    
    ## Apparently ping commands are hip
    @commands.command()
    @allowed(0, '|')
    async def ping(self):
        """Pong."""
        await self.bot.say("Pong.")
    
    ## Version information
    @commands.command()
    @allowed(0, '|')
    async def info(self):
        """Display information about this bot."""
        await self.bot.say("Ispyra {0} by Ispira (https://github.com/Ispira/Ispyra)"
        .format(version))
    
    ## Bot status
    @commands.command()
    @allowed(0, '|')
    async def status(self):
        """Display number of botmasters, and connected servers."""
        await self.bot.say("Servers: {0} | Botmasters: {1}"
        .format(len(server_list), len(bot_masters)))
    
    ## List names of currently connected servers
    @commands.command()
    @allowed(0, '|')
    async def servers(self):
        """List the names of all currently connected servers."""
        server_names = []
        for serv in server_list:
            server_names.append(serv.name)
        await self.bot.say(" | ".join(server_names))

def setup(bot):
    bot.add_cog(User(bot))
