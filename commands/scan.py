import discord
from discord.ext import commands
from utils.infection_manager import check_infection_status

class Scan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="scan", description="Scan a user for infection.")
    async def scan(self, ctx, user: discord.Member):
        status = check_infection_status(user.id)
        if status:
            await ctx.respond(f"🧬 {user.display_name} is infected (Stage {status['stage']}).")
        else:
            await ctx.respond(f"✅ {user.display_name} is clean.")

def setup(bot):
    bot.add_cog(Scan(bot))
