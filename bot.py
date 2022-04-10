import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready():
    print(" ")
    print("봇 작동중")
    print(" ")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("공지사항")) # 상태메세지

#========================================================================================================================================================================================================================================================================================================================================================================

@client.event
async def on_message(message):
    if message.content == "테스트메세지테스트": # 명령어설정
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

    if message.content == "!출근": # 명령어설정
        ch = client.get_channel(950932986608615485)
        await message.delete()
        await ch.send ("{}님이 **`출근`** 하였습니다.\n**```fix\n- 모든 문의 및 활동이 가능합니다.\n```**```- 출근한 시간 : {}시 {}분```".format(message.author.mention, datetime.datetime.now().hour, datetime.datetime.now().minute))
        await message.channel.send ("{}님이 `{}`시 `{}`분에 **`출근`** 하였습니다.".format(message.author.mention, datetime.datetime.now().hour, datetime.datetime.now().minute))

    if message.content == "!퇴근": # 명령어설정
        ch = client.get_channel(950932986608615485)
        await message.delete()
        await ch.send ("{}님이 **`퇴근`** 하였습니다.\n**```diff\n- 모든 문의 및 활동이 불가능 합니다.\n```**```- 퇴근한 시간 : {}시 {}분```".format(message.author.mention, datetime.datetime.now().hour, datetime.datetime.now().minute))
        await message.channel.send ("{}님이 `{}`시 `{}`분에 **`퇴근`** 하였습니다.\n".format(message.author.mention, datetime.datetime.now().hour, datetime.datetime.now().minute))

    if message.content == "!휴식": # 명령어설정
        ch = client.get_channel(950932986608615485)
        await message.delete()
        await ch.send ("{}님이 **`휴식 상태`**로 전환 하였습니다.\n**```diff\n- 잠시 동안 모든 문의 및 활동이 불가능 합니다.\n```**```- 휴식 시작 시간 : {}시 {}분```".format(message.author.mention, datetime.datetime.now().hour, datetime.datetime.now().minute))
        await message.channel.send ("{}님이 `{}`시 `{}`분에 **`휴식`**을 시작 하였습니다.".format(message.author.mention, datetime.datetime.now().hour, datetime.datetime.now().minute))    

#========================================================================================================================================================================================================================================================================================================================================================================

    if message.content == "!상품": # 명령어설정
        await message.delete()
        embed = discord.Embed(title="[서버] 노드vpn랜계", description="```\n· 누구나 아는\n· vpn랜계```\n**```diff\n- 바로 구매하새요.\n```**\n**```· 판매 가격 : 1원```**", color=0x00ff00)
        embed.set_thumbnail(url="사진링크")
        await message.channel.send (embed=embed)      

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('토큰')