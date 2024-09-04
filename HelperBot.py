import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='.', intents=intents)

# Example product
@bot.command()
async def bsprotector(ctx):
    embed = discord.Embed(
        title="ByteS Privacy Protector",
        description="[Website](https://bytestore.sellburst.io/) \n[Ticket](https://discord.com/channels/1275136064863993948/1275147630447427686)",  
        color=discord.Color.from_rgb(0, 255, 255) 
    )

    embed.add_field(name="__Cleaner__", value="\u200b\n<:emoji:1280824723478937683> **[BROWSE]** \n↪︎ Chrome \n↪︎ Mozilla \n↪︎ Brave \n↪︎ Opera GX \n\n<:emoji:1280824723478937683> **[WINDOWS]** \n↪︎ Temp \n↪︎ Logs \n↪︎ Crash dumps \n↪︎ Prefetch \n↪︎ Events \n↪︎ History \n↪︎ Registy \n↪︎ Last Activity \n↪︎ Regseeker \n↪︎ Recent \n↪︎ Memory \n↪︎ Search History \n↪︎ Update \n↪︎ Download File \n\n<:emoji:1280824723478937683> **[AC TRACES]** \n↪︎ Fivem \n↪︎ Fortnite \n↪︎ Valorant \n↪︎ AC \n\n<:emoji:1280824723478937683> **[OTHER]** \n↪︎ Steam Account \n↪︎ Drive Optimizer \n↪︎ Adobe Temp File \n↪︎ Steam Cache \n↪︎ System restore point \n↪︎ Cliboard History \n↪︎ DNS Cache \n↪︎ Windows Store Cache \n↪︎ String", inline=False)
    embed.add_field(name="__Spoofer__", value="\u200b\n<:emoji:1280824723478937683> **[TEMP SPOOF]** \n↪︎ MAC \n↪︎ Bios \n↪︎ Uefi \n↪︎ Disk \n↪︎ Product ID \n↪︎ Machine ID \n↪︎ Display ID \n↪︎ Volume ID \n↪︎ GUID \n↪︎ HWID \n↪︎ PC Name \n↪︎ Bios Date \n\n<:emoji:1280824723478937683> **[ADDONS]** \n↪︎ Fivem Hijacking \n↪︎ Fivem cleaner \n↪︎ Unlink Discord \n↪︎ Unlink Xbox \n\n<:emoji:1280824723478937683> **[OTHER]** \n↪︎ Perm Spoof \n↪︎ Driver Spoof", inline=False)
    embed.add_field(name="__Winodws Control__", value="\u200b\n<:emoji:1280824723478937683> **[NETWORK]** \n↪︎ NIC \n↪︎ Adapter \n↪︎ UserAgent \n↪︎ Host Name \n\n<:emoji:1280824723478937683> **[SYSTEM]** \n↪︎ GPU \n↪︎ CPU \n↪︎ RAM \n↪︎ OS Version \n↪︎ Environment \n↪︎ Windows key \n↪︎ Local \n↪︎ Battery \n↪︎ Configuration \n↪︎ Optical drivres \n↪︎ Bios Information", inline=False)
    embed.add_field(name="__Price__", value="\u200b\n<:emoji:1280824723478937683> **Week: **10€ \n<:emoji:1280824723478937683> **Month: **20€  \n<:emoji:1280824723478937683> **LifeTime: **40€", inline=False)

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1270751192074682418/1280858194968580208/ByteStore_Logo_modern_and_not_white_just_in_blackred_mode.png?ex=66d99ba6&is=66d84a26&hm=7587a8b37efe77d8727ba665221e04cf157a556e3076458255596ff9ce33e624&")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1280810844472737852/1280859840629178368/image.png?ex=66d99d2f&is=66d84baf&hm=db850bf6669a714b57224a719a49cd3c6b6d0f1d5f9d8fb9c70aeef43ba64c13&")

    embed.set_footer(
    icon_url="https://cdn.discordapp.com/attachments/1280810844472737852/1280867592017547365/ByteStore_Logo_modern_and_not_white_just_in_blackred_mode.png?ex=66d9a467&is=66d852e7&hm=f38b2ea8f318374ac9bbec2265a83ac15f0140cf056efefb1c92952472d416f3&",
    text="ByteS developers team"
)
    await ctx.send(embed=embed)

# Example payment
@bot.command()
async def payment(ctx):
    embed = discord.Embed(
        title="ByteS Payment Method",
        description="",  
        color=discord.Color.from_rgb(0, 255, 255) 
    )

    embed.add_field(name="__Method__", value="\u200b\n<:emoji:1280824723478937683> **[PAYPAL]** \n↪︎[enter your email] \n↪︎Friends and Family, Note: This person is my friend and i know him. \n\n<:emoji:1280824723478937683> **[GIFT CARD]** \n↪︎Binance, Steam [enter your country] \n\n<:emoji:1280824723478937683> **[CRYPTO]** \n↪︎LTC, BTC, USDC", inline=False)

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1270751192074682418/1280858194968580208/ByteStore_Logo_modern_and_not_white_just_in_blackred_mode.png?ex=66d99ba6&is=66d84a26&hm=7587a8b37efe77d8727ba665221e04cf157a556e3076458255596ff9ce33e624&")
    embed.set_image(url="")

    embed.set_footer(
    icon_url="https://cdn.discordapp.com/attachments/1280810844472737852/1280867592017547365/ByteStore_Logo_modern_and_not_white_just_in_blackred_mode.png?ex=66d9a467&is=66d852e7&hm=f38b2ea8f318374ac9bbec2265a83ac15f0140cf056efefb1c92952472d416f3&",
    text="ByteS developers team"
)
    await ctx.send(embed=embed)

# Product
@bot.command()
async def product1(ctx):
    embed = discord.Embed(
        title="Product Name",
        description="Product Description",  
        color=discord.Color.from_rgb(0, 255, 255) 
    )

    embed.add_field(name="__Category1__", value="", inline=False)
    embed.add_field(name="__Category2__", value="", inline=False)
    embed.add_field(name="__Category3__", value="", inline=False)
    embed.add_field(name="__Category4__", value="", inline=False)

    # embed.set_thumbnail(url="PRODUCT_ LOGO")
    # embed.set_image(url="PRODUCT_IMAGE")

    # embed.set_footer(
    # icon_url="ICON",
    # text="TEXT"
# )
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'The bot is ready: {bot.user.name} (ID: {bot.user.id})')

bot.run("your_bot_token")
