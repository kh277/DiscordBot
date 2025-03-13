import discord
from discord.ext import commands
from random import random
import asyncio

import loadJson
from getEventData import getEventData
from generateRandomName import generateRandomString
from getCharactorData import getCharacterExp


RED = 0xFF0000
BLUE = 0x00FFFF
LIME = 0x00FF00
YELLOW = 0xFFFF00
DARK_ORANGE = 0xFF8C00
CRIMSON = 0xDC143C
CHARTREUSE = 0x7FFF00

bot = commands.Bot(
    command_prefix="/",
    intents=discord.Intents.all(),
    sync_command=True)


@bot.event
async def on_ready():
    print("CLBot 기동 시작...")
    activity = discord.Game("삐삐쀼쀼")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await bot.tree.sync()


# ----------------- 슬래시 명령어 -----------------

@bot.tree.command(name="청소", description="지정한 개수(1~20)의 메시지를 삭제합니다")
async def 청소(interaction: discord.Interaction, number: int):
    await interaction.response.defer(ephemeral=True)
    
    if 0 < number <= 20:
        deleted = await interaction.channel.purge(limit=number+1)
        msg = await interaction.followup.send(
            f"{len(deleted)-1}개의 메시지를 삭제했습니다. (이 메시지는 3초 후 사라집니다.)", 
            ephemeral=True
        )
        await asyncio.sleep(3)
        await msg.delete()
    else:
        embed = discord.Embed(description="올바르지 않은 숫자입니다.", color=RED)
        await interaction.followup.send(embed=embed, ephemeral=True)


@bot.tree.command(name="랜덤닉", description="3~10글자의 랜덤한 문자열을 생성합니다")
async def 랜덤닉(interaction: discord.Interaction):
    embed = discord.Embed(title=generateRandomString(), color=CRIMSON)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="썬데이", description="썬데이 메이플 정보가 있으면 사진을 불러옵니다")
async def 썬데이(interaction: discord.Interaction):
    embed = discord.Embed(description=getEventData("썬데이"), color=DARK_ORANGE)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="공지", description="공지 정보를 받아옵니다")
async def 공지(interaction: discord.Interaction, event_name: str):
    embed = discord.Embed(description=getEventData(event_name), color=DARK_ORANGE)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="경험치", description="메이플 캐릭터의 경험치를 알려줍니다")
async def 경험치(interaction: discord.Interaction, character_name: str):
    exp = getCharacterExp(character_name)
    if exp is None:
        embed = discord.Embed(description="캐릭터를 찾을 수 없습니다", color=RED)
    else:
        embed = discord.Embed(title=character_name, description="{}  {}%".format(*exp), color=LIME)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="깡통", description="깡통은 깡통입니다")
async def 깡통(interaction: discord.Interaction):
    if int(random() + 0.3) == 1:
        embed = discord.Embed(title="삐삐쀼쀼", color=CHARTREUSE)
    else:
        embed = discord.Embed(title="끄아앙", color=RED)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="백준", description="백준 문제 링크를 올려줍니다")
async def 백준(interaction: discord.Interaction, boj_number: int):
    if boj_number < 1000:
        embed = discord.Embed(description="올바르지 않은 문제 번호입니다.", color=RED)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f"백준 {boj_number}번 문제 : https://www.acmicpc.net/problem/{boj_number}")


@bot.tree.command(name="디맥", description="디맥 서열표")
async def 디맥(interaction: discord.Interaction, number: str = "4"):
    if number in ['4', '5', '6', '8']:
        await interaction.response.send_message(f"https://v-archive.net/grade/{number}/ALL")
    else:
        embed = discord.Embed(description="올바르지 않은 키입니다.", color=RED)
        await interaction.response.send_message(embed=embed)


bot.run(loadJson.getBotToken())
