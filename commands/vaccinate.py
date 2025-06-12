import discord
from discord.ext import commands
from utils.infection_manager import check_infection_status, cure_user

class Vaccinate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="vaccinate", description="Vaccinate a user.")
    async def vaccinate(self, ctx, user: discord.Member):
        if check_infection_status(user.id):
            cure_user(user.id)
            await ctx.respond(f"💉 {user.display_name} has been vaccinated and cured.")
        else:
            await ctx.respond(f"✅ {user.display_name} is not infected.")

def setup(bot):
    bot.add_cog(Vaccinate(bot))
