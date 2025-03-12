import discord
from discord.ext import commands
from random import random
import loadJson

from getEventData import getEventData
from generateRandomName import generateRandomName


bot = commands.Bot(
    command_prefix="!",
    intents= discord.Intents.all(),
    sync_command=True)


# 봇 초기화 후 호출
@bot.event
async def on_ready():
    print("CLBot 기동 시작...")
    activity = discord.Game("삐삐쀼쀼")
    await bot.change_presence(status=discord.Status.online, activity=activity)


# 봇 커맨드 ----------

# @bot.command(name="깡통", description="깡통은 깡통입니다")
# async def aris(ctx):
#     if int(random() + 0.3) == 1:
#         await ctx.channel.send("삐삐쀼쀼")
#     else:
#         await ctx.send("끄아앙")
#     return

@bot.command(name="랜덤닉", description="3~10글자의 랜덤한 문자열을 생성합니다")
async def randomNickname(ctx):
    await ctx.channel.send(generateRandomName())
    return

@bot.command(name="썬데이", description="썬데이 메이플 정보가 있으면 사진을 불러옵니다")
async def getSunday(ctx):
    await ctx.channel.send(getEventData("썬데이"))

@bot.command(name="공지", description="공지 정보를 받아옵니다")
async def getNotice(ctx, eventName):
    await ctx.channel.send(getEventData(eventName))

@bot.command(name="백준", description="백준 문제 링크를 올려줍니다")
async def getBOJLink(ctx, BOJNumber):
    await ctx.channel.send("백준 {}번 문제 : https://www.acmicpc.net/problem/{}".format(BOJNumber, BOJNumber))

@bot.command(name="디맥", description="디맥 서열표")
async def getDJMAX(ctx, number=None):
    if number == None:
        number = '4'
    else:
        number = str(number)
    if number in ['4', '5', '6', '8']:
        await ctx.channel.send("https://v-archive.net/grade/{}/ALL".format(number))
    else:
        await ctx.channel.send("올바르지 않은 키입니다.")

bot.run(loadJson.getBotToken())
