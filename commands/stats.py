import discord
from discord.ext import commands
from utils.infection_manager import get_stats

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="outbreak_stats", description="Show live outbreak statistics.")
    async def stats(self, ctx):
        stats = get_stats()
        await ctx.respond(f"📊 **Outbreak Stats**\n😷 Infected: {stats['infected']}\n💉 Vaccinated: {stats['vaccinated']}\n🏥 Isolated: {stats['isolated']}\n🧪 Mutation Level: {stats['mutation_level']}")

def setup(bot):
    bot.add_cog(Stats(bot))
