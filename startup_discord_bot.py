import discord
from discord.ext import commands
import os
import aiohttp
import json
from datetime import datetime

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Store your API keys in Replit Secrets
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="startups grow 🚀"
    ))

@bot.command(name='tip')
async def startup_tip(ctx, *, category: str = 'general'):
    """Get startup tips by category: funding, marketing, product, legal, hiring, general"""
    
    tips = {
        'funding': [
            "💰 Bootstrap first - prove your concept before seeking investment",
            "📊 Know your numbers cold - investors will ask about unit economics",
            "🎯 Target investors who understand your industry and stage",
            "📈 Show traction - revenue, users, or meaningful metrics matter most",
            "🤝 Warm introductions work better than cold emails"
        ],
        'marketing': [
            "🎯 Focus on one channel at a time until you master it",
            "👥 Build in public - share your journey on social media",
            "📝 Content marketing: Start a blog addressing customer pain points",
            "🔄 Product-led growth: Make your product easy to try and share",
            "💬 Community building beats paid ads in early stages"
        ],
        'product': [
            "🎨 Start with MVP - ship fast, iterate based on feedback",
            "👂 Talk to users weekly - understanding problems > building features",
            "📱 Mobile-first design is crucial in 2025",
            "⚡ Page load speed impacts conversion - optimize ruthlessly",
            "🔐 Build security and privacy in from day one"
        ],
        'legal': [
            "📄 Incorporate early - LLC or C-Corp depending on goals",
            "🤝 Always use written contracts and agreements",
            "💼 Vesting schedules protect co-founder equity",
            "™️ Trademark your brand name and logo early",
            "📋 Keep clean cap tables from the start"
        ],
        'hiring': [
            "🎯 Hire for culture fit and learning ability over experience",
            "💡 First 10 hires define your company culture",
            "🔍 Use trial projects to assess skills before hiring",
            "📈 Equity can attract talent when cash is limited",
            "🤝 Hire people who've built things, not just worked places"
        ],
        'general': [
            "🚀 Launch before you're ready - feedback beats perfection",
            "💪 Founder mental health is crucial - take breaks",
            "📊 Track metrics that matter: CAC, LTV, churn, MRR",
            "🔄 Pivot quickly when data shows you're wrong",
            "🎓 Learn from failures fast and move on"
        ]
    }
    
    cat = category.lower()
    if cat not in tips:
        await ctx.send(f"Category '{category}' not found. Available: funding, marketing, product, legal, hiring, general")
        return
    
    import random
    tip = random.choice(tips[cat])
    
    embed = discord.Embed(
        title=f"💡 Startup Tip - {cat.title()}",
        description=tip,
        color=discord.Color.blue(),
        timestamp=datetime.utcnow()
    )
    embed.set_footer(text="Use !tip <category> for more tips")
    await ctx.send(embed=embed)

@bot.command(name='resources')
async def startup_resources(ctx):
    """Get helpful startup resources and tools"""
    
    embed = discord.Embed(
        title="🚀 Essential Startup Resources",
        description="Curated tools and platforms to help your startup succeed",
        color=discord.Color.green()
    )
    
    embed.add_field(
        name="📚 Learning",
        value="• Y Combinator Startup School (free)\n• How to Start a Startup (YC course)\n• The Lean Startup by Eric Ries\n• Zero to One by Peter Thiel",
        inline=False
    )
    
    embed.add_field(
        name="💰 Funding",
        value="• YC Combinator\n• TechStars\n• AngelList\n• Crunchbase (research)\n• Product Hunt (launches)",
        inline=False
    )
    
    embed.add_field(
        name="🛠️ Tools",
        value="• Notion (docs)\n• Figma (design)\n• Vercel/Replit (hosting)\n• Stripe (payments)\n• PostHog (analytics)",
        inline=False
    )
    
    embed.add_field(
        name="👥 Community",
        value="• Indie Hackers\n• Reddit r/startups\n• Twitter startup community\n• Local startup meetups\n• Slack communities",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='investors')
async def find_investors(ctx, *, stage: str = 'seed'):
    """Get investor contacts by stage: pre-seed, seed, series-a, series-b"""
    
    investors = {
        'pre-seed': {
            'firms': [
                '🏢 Y Combinator - batch program',
                '🏢 Hustle Fund - $25K-$150K checks',
                '🏢 Boost VC - pre-seed crypto/sci-fi',
                '🏢 Antler - pre-seed global',
                '🏢 On Deck - community + funding'
            ],
            'angels': 'AngelList, Angel Investment Network, Gust'
        },
        'seed': {
            'firms': [
                '🏢 Sequoia Arc - $500K-$1M',
                '🏢 a16z - varies by vertical',
                '🏢 First Round Capital',
                '🏢 Initialized Capital',
                '🏢 Founder Collective'
            ],
            'angels': 'Seek warm intros via LinkedIn'
        },
        'series-a': {
            'firms': [
                '🏢 Sequoia Capital',
                '🏢 Accel Partners',
                '🏢 Benchmark',
                '🏢 Greylock Partners',
                '🏢 Lightspeed Venture'
            ],
            'angels': 'Focus on institutional VCs'
        },
        'series-b': {
            'firms': [
                '🏢 Tiger Global',
                '🏢 Coatue Management',
                '🏢 Insight Partners',
                '🏢 General Catalyst',
                '🏢 Index Ventures'
            ],
            'angels': 'Growth-stage institutional only'
        }
    }
    
    stage = stage.lower()
    if stage not in investors:
        await ctx.send("Stage not found. Use: pre-seed, seed, series-a, series-b")
        return
    
    data = investors[stage]
    
    embed = discord.Embed(
        title=f"💼 {stage.title()} Investors",
        description="Top firms and platforms for your stage",
        color=discord.Color.gold()
    )
    
    embed.add_field(
        name="Top Firms",
        value='\n'.join(data['firms']),
        inline=False
    )
    
    embed.add_field(
        name="Finding Angels",
        value=data['angels'],
        inline=False
    )
    
    embed.add_field(
        name="💡 Pro Tip",
        value="Warm introductions have 10x higher success rate. Use LinkedIn to find connections.",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='ask')
async def ask_ai(ctx, *, question: str):
    """Ask AI for startup advice (powered by Claude)"""
    
    if not ANTHROPIC_API_KEY:
        await ctx.send("⚠️ AI feature not configured. Add ANTHROPIC_API_KEY to Replit Secrets.")
        return
    
    async with ctx.typing():
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "x-api-key": ANTHROPIC_API_KEY,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json"
                }
                
                data = {
                    "model": "claude-sonnet-4-20250514",
                    "max_tokens": 500,
                    "messages": [{
                        "role": "user",
                        "content": f"As a startup advisor, answer this question concisely (max 400 words): {question}"
                    }]
                }
                
                async with session.post(
                    "https://api.anthropic.com/v1/messages",
                    headers=headers,
                    json=data
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        answer = result['content'][0]['text']
                        
                        # Split into chunks if too long for Discord
                        if len(answer) > 1900:
                            chunks = [answer[i:i+1900] for i in range(0, len(answer), 1900)]
                            for chunk in chunks:
                                embed = discord.Embed(
                                    description=chunk,
                                    color=discord.Color.purple()
                                )
                                await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(
                                title="🤖 AI Startup Advisor",
                                description=answer,
                                color=discord.Color.purple()
                            )
                            await ctx.send(embed=embed)
                    else:
                        await ctx.send("❌ AI service temporarily unavailable")
        except Exception as e:
            await ctx.send(f"❌ Error: {str(e)}")

@bot.command(name='pitch')
async def pitch_template(ctx):
    """Get a pitch deck template"""
    
    embed = discord.Embed(
        title="📊 Pitch Deck Template (10-15 slides)",
        description="Essential slides every investor pitch needs",
        color=discord.Color.red()
    )
    
    slides = [
        "1️⃣ **Cover**: Company name, tagline, contact",
        "2️⃣ **Problem**: What pain point are you solving?",
        "3️⃣ **Solution**: Your product/service",
        "4️⃣ **Market Size**: TAM/SAM/SOM breakdown",
        "5️⃣ **Product Demo**: Screenshots or video",
        "6️⃣ **Traction**: Users, revenue, growth metrics",
        "7️⃣ **Business Model**: How you make money",
        "8️⃣ **Competition**: Competitive landscape",
        "9️⃣ **Go-to-Market**: Customer acquisition strategy",
        "🔟 **Team**: Founders and key hires",
        "1️⃣1️⃣ **Financials**: 3-year projections",
        "1️⃣2️⃣ **Ask**: How much, use of funds, timeline"
    ]
    
    embed.add_field(
        name="📝 Slide Structure",
        value='\n'.join(slides),
        inline=False
    )
    
    embed.add_field(
        name="⏱️ Timing",
        value="Aim for 10-15 minutes. Leave 10+ minutes for Q&A.",
        inline=False
    )
    
    embed.add_field(
        name="🎨 Design Tips",
        value="• Use Pitch, Canva, or Google Slides\n• Keep it simple and visual\n• One idea per slide\n• Large fonts (30pt minimum)",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='metrics')
async def key_metrics(ctx):
    """Essential startup metrics to track"""
    
    embed = discord.Embed(
        title="📈 Key Startup Metrics",
        description="Track these to understand your business health",
        color=discord.Color.orange()
    )
    
    embed.add_field(
        name="💰 Financial",
        value="• **MRR/ARR**: Monthly/Annual Recurring Revenue\n• **Burn Rate**: Cash spent per month\n• **Runway**: Months until out of cash\n• **Revenue Growth**: Month-over-month %",
        inline=False
    )
    
    embed.add_field(
        name="👥 Customer",
        value="• **CAC**: Customer Acquisition Cost\n• **LTV**: Lifetime Value\n• **LTV:CAC Ratio**: Should be 3:1 or better\n• **Churn Rate**: % customers lost per month",
        inline=False
    )
    
    embed.add_field(
        name="📊 Product",
        value="• **DAU/MAU**: Daily/Monthly Active Users\n• **Activation Rate**: % completing key action\n• **Retention**: % users returning\n• **NPS**: Net Promoter Score",
        inline=False
    )
    
    embed.add_field(
        name="🎯 Growth",
        value="• **Viral Coefficient**: Users referred per user\n• **Conversion Rate**: % visitors to customers\n• **Payback Period**: Time to recover CAC",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='help')
async def help_command(ctx):
    """Show all available commands"""
    
    embed = discord.Embed(
        title="🚀 Startup Helper Bot - Commands",
        description="Your AI-powered startup assistant",
        color=discord.Color.blue()
    )
    
    commands_list = [
        "**!tip [category]** - Get startup tips (funding, marketing, product, legal, hiring, general)",
        "**!resources** - Essential tools and platforms",
        "**!investors [stage]** - Find investors by stage (pre-seed, seed, series-a, series-b)",
        "**!ask [question]** - Ask AI for startup advice",
        "**!pitch** - Get pitch deck template",
        "**!metrics** - Key metrics to track",
        "**!help** - Show this message"
    ]
    
    embed.add_field(
        name="📋 Available Commands",
        value='\n'.join(commands_list),
        inline=False
    )
    
    embed.add_field(
        name="💡 Examples",
        value="`!tip funding` - Get funding tips\n`!investors seed` - Find seed investors\n`!ask How do I validate my idea?` - AI advice",
        inline=False
    )
    
    embed.set_footer(text="Built for startups by startups 🚀")
    
    await ctx.send(embed=embed)

# Run the bot
if __name__ == "__main__":
    if not DISCORD_TOKEN:
        print("❌ Error: DISCORD_TOKEN not found in environment variables")
        print("Add your Discord bot token to Replit Secrets as 'DISCORD_TOKEN'")
    else:
        bot.run(DISCORD_TOKEN)