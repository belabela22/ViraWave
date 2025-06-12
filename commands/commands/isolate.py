import discord
from discord.ext import commands
from utils.infection_manager import check_infection_status, mark_isolated

class Isolate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="isolate", description="Isolate an infected user.")
    async def isolate(self, ctx, user: discord.Member):
        status = check_infection_status(user.id)
        if status:
            mark_isolated(user.id)
            await ctx.respond(f"🚨 {user.display_name} has been isolated!")
        else:
            await ctx.respond(f"⚠️ {user.display_name} is not infected.")

def setup(bot):
    bot.add_cog(Isolate(bot))
