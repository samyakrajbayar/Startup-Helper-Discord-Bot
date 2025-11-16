# 🚀 Startup Helper Discord Bot

A comprehensive Discord bot designed to help startups succeed by providing expert tips, investor contacts, essential resources, and AI-powered advice. Perfect for founders, startup teams, and entrepreneurship communities.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Discord.py](https://img.shields.io/badge/discord.py-2.0+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

### 💡 Curated Startup Tips
Get expert advice across multiple categories:
- **Funding** - Investment strategies, pitch advice, investor relations
- **Marketing** - Growth hacking, content marketing, user acquisition
- **Product** - MVP development, product-market fit, iteration
- **Legal** - Incorporation, contracts, IP protection
- **Hiring** - Team building, equity, culture
- **General** - Mental health, metrics, pivoting

### 💼 Investor Database
Find the right investors for your stage:
- Pre-seed investors and accelerators
- Seed-stage VCs and angel networks
- Series A and B institutional investors
- Warm introduction strategies

### 🛠️ Essential Resources
Curated list of:
- Learning platforms and courses
- Funding platforms and accelerators
- Development and design tools
- Analytics and business tools
- Startup communities

### 🤖 AI-Powered Advice
Powered by Claude (Anthropic), get personalized answers to your specific startup questions in real-time.

### 📊 Business Templates
- Complete pitch deck structure (10-15 slides)
- Key metrics dashboard (MRR, CAC, LTV, churn, etc.)
- Financial and growth KPIs

## 🎯 Commands

| Command | Description | Example |
|---------|-------------|---------|
| `!tip [category]` | Get startup tips by category | `!tip funding` |
| `!resources` | View essential startup resources | `!resources` |
| `!investors [stage]` | Find investors by funding stage | `!investors seed` |
| `!ask [question]` | Ask AI for personalized advice | `!ask How do I validate my idea?` |
| `!pitch` | Get pitch deck template | `!pitch` |
| `!metrics` | View key startup metrics to track | `!metrics` |
| `!help` | Show all available commands | `!help` |

## 🚀 Quick Start on Replit

### 1. Create New Repl
- Go to [Replit](https://replit.com)
- Create a new Python Repl
- Copy the bot code into `main.py`

### 2. Install Dependencies
Create a `requirements.txt` file with:
```txt
discord.py>=2.0.0
aiohttp
```

Replit will automatically install these when you run the project.

### 3. Get Your Discord Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" tab and click "Add Bot"
4. **Important:** Enable "Message Content Intent" under Privileged Gateway Intents
5. Click "Reset Token" and copy your bot token (keep this secret!)

### 4. Configure Replit Secrets

1. In your Repl, click the "Secrets" tab (🔒 lock icon) in the left sidebar
2. Add the following secrets:

| Key | Value | Required |
|-----|-------|----------|
| `DISCORD_TOKEN` | Your Discord bot token | ✅ Yes |
| `ANTHROPIC_API_KEY` | Your Claude API key (optional) | ❌ No |

**Note:** The bot works without `ANTHROPIC_API_KEY`, but the `!ask` command will be disabled.

### 5. Invite Bot to Your Server

1. In Discord Developer Portal, go to "OAuth2" → "URL Generator"
2. Select scopes:
   - ✅ `bot`
   - ✅ `applications.commands` (optional, for future slash commands)
3. Select bot permissions:
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Read Messages/View Channels
   - ✅ Read Message History
4. Copy the generated URL and open it in your browser
5. Select your server and authorize the bot

### 6. Run the Bot

Click the "Run" button in Replit. You should see:
```
[Bot Username] has connected to Discord!
```

🎉 Your bot is now live! Try `!help` in your Discord server.

## 🔧 Configuration

### Environment Variables

The bot uses Replit Secrets for configuration:

```python
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')  # Required
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')  # Optional
```

### Getting Claude API Key (Optional)

For AI-powered `!ask` command:

1. Sign up at [Anthropic Console](https://console.anthropic.com/)
2. Go to API Keys section
3. Create a new API key
4. Add it to Replit Secrets as `ANTHROPIC_API_KEY`

**Cost:** Claude API charges per token. The bot is configured to use minimal tokens (~$0.01-0.05 per query).

## 📖 Usage Examples

### Get Funding Tips
```
!tip funding
```
Returns: Random tip about fundraising, investor relations, or pitch strategy

### Find Seed Investors
```
!investors seed
```
Returns: List of top seed-stage VCs and angel networks

### Ask AI for Advice
```
!ask How do I find product-market fit for a B2B SaaS?
```
Returns: Personalized AI-generated advice from Claude

### View All Resources
```
!resources
```
Returns: Curated list of tools, platforms, and learning resources

## 🎨 Customization

### Adding New Tips

Edit the `tips` dictionary in the `startup_tip` command:

```python
tips = {
    'your_category': [
        "💡 Your tip here",
        "🚀 Another tip",
        # Add more tips
    ]
}
```

### Adding Investors

Edit the `investors` dictionary in the `find_investors` command:

```python
investors = {
    'your-stage': {
        'firms': [
            '🏢 Firm Name - details',
        ],
        'angels': 'Finding strategy'
    }
}
```

### Changing Bot Prefix

Modify the command prefix from `!` to anything else:

```python
bot = commands.Bot(command_prefix='$', intents=intents)  # Use $ instead of !
```

## 🔒 Security Best Practices

- ✅ **Never commit tokens** to version control
- ✅ **Use Replit Secrets** for all sensitive data
- ✅ **Regenerate tokens** if accidentally exposed
- ✅ **Limit bot permissions** to only what's needed
- ✅ **Monitor API usage** to avoid unexpected charges

## 🐛 Troubleshooting

### Bot doesn't respond to commands

**Check:**
1. "Message Content Intent" is enabled in Discord Developer Portal
2. Bot has permission to read messages in the channel
3. You're using the correct prefix (`!` by default)
4. Bot is online (green status in Discord)

### "DISCORD_TOKEN not found" error

**Solution:**
1. Verify token is added to Replit Secrets (not environment variables in code)
2. Key name is exactly `DISCORD_TOKEN` (case-sensitive)
3. Restart the Repl after adding secrets

### AI command not working

**Check:**
1. `ANTHROPIC_API_KEY` is added to Replit Secrets
2. API key is valid and has credits
3. Check Anthropic Console for API usage/errors

### Bot goes offline when closing Replit

**Solution:**
Replit free tier stops your Repl when inactive. Options:
1. Upgrade to Replit's Always On feature
2. Use a keep-alive service like UptimeRobot
3. Host on a VPS or cloud platform

## 📊 Analytics & Monitoring

Track bot usage by adding logging:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

@bot.event
async def on_command(ctx):
    logger.info(f'{ctx.author} used {ctx.command} in {ctx.guild}')
```

## 🚦 Rate Limits

- **Discord API:** 50 requests per second per bot
- **Claude API:** Varies by plan (typically 50-100 requests/min)
- Bot includes automatic rate limit handling

## 🤝 Contributing

Contributions are welcome! To add features:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Test thoroughly
5. Submit a pull request

**Ideas for contributions:**
- Slash commands implementation
- Database for user preferences
- More investor categories
- Industry-specific tips
- Startup events calendar

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## 🙏 Acknowledgments

- **Discord.py** - Amazing Discord API wrapper
- **Anthropic Claude** - AI-powered advice
- **Replit** - Easy deployment platform
- **Startup Community** - For inspiring this project

## 📧 Support

- **Issues:** Open a GitHub issue
- **Questions:** Use the Discussions tab
- **Security:** Report vulnerabilities privately

## 🔗 Useful Links

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [Replit Documentation](https://docs.replit.com/)

---

**Built with ❤️ for the startup community**

*Last updated: November 2025*
