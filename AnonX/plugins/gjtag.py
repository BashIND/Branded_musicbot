from AnonX import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

TAGMES = [ " **ચાલો પાર્ટી કરીએ 🥳🥳**",
                     " **તમે ગ્રુપમાં કેમ વાત નથી કરતા 😒😒**",
                     "**ખુશ રહો✌️🙂**",
                     "**માએ મને ઠપકો આપ્યો 🥲**",
                     " **તમે ગઈકાલે ક્યાં ગયા હતા? 🤔**",
                     "**આ દિવસોમાં શું ચાલી રહ્યું છે 😌❤️🥀**",
                     "**હેલો 👀**",
                     "**આપણે મિત્રો બની શકીએ?**",
                     "**હેલો 😈**",
                      " **મને તમારા ગ્રુપમાં એડ કરો હું દરેકને ટેગ કરીશ ❤️**",
                      "**શું તમે મારા મિત્ર છો 😒😒**",
                     "**ગઈકાલે મજા આવી 🥳🥳**",
                     "**તમે ખાધું છે 😚**",
                     " **બહુ ઝડપથી જઈ રહ્યા છીએ 😏😏**",
                     " **મારે કાલે શોપિંગ કરવા જવું છે 💞**",
                     " **શું તમે સંબંધમાં છો? 👀** ",
                     " **અને કેદી કેવો છે 👀**",
                   "**શું તમે ક્યારેય મને યાદ કરો છો 🥺🥺**",
                     "**મને ભૂલી ગયો 🥺🥀**",
                     " **આજે મેં એક વાંદરો જોયો 😌👉🐒**",
                     " ** ટોક મેન ❤️👀** ",
                     "**વોઇસ ચેટ પર આવો**",
                     " **વોઈસ ચેટ પર લડાઈ 🤯🤯**",
                     " **મને ક્યારેય મિસ ના કરશો 💔💔**",
                     " **હા 👀**",
                     "**દોસ્ત તું ક્યાં છે ❤️💫**",
                     " **મને તમારા ગ્રુપમાં એડ કરો 🥺**",
                     " **અહીં આવો @INCRICIBLE 👀**",
                     "** શું તમે સૂઈ ગયા 🤔🤔 **",
                     "** હેલો જી 💞 **",
                     "**તમારા જેવો મિત્ર હોય તો ચિંતા કરવાની શું વાત છે?❣️**",
                     " **કેટલો મૌન છો દોસ્ત 😒**",
                     " **તમે ગીત જાણો છો 👀**",
                     "** બધાને શાંત કરો**",
                     "**હાય 👀**",
                     " **તમારા ઘરમાં બધા કેમ છે 😌❤️🥀**",
                     "**ઉઠો પણ 😶**",
                     "**તમે કેટલા સમયથી છો 🧐**",
                     " **મેં મારી #વિશ્વશિશો 😇 દીવાલ બનાવી છે , ખામખાન #ZindvEgi માં અનારકલી 💃 તરીકે નાચતો હતો ** ",
                     " **ઊંઘ ઉડી ગઈ છે #𝗠𝗘𝗥𝗜 કોઈએ કહીને**",
                    " **SUNOO👂👂👂… તમે 👧 ને તમારું બનાવીને જ રાખો છો, બીજાએ #__🧸💠🗸💔🌷💔..!!😔**",
                     "* ઉંઘ ઉડી ગઈ છે કોઈએ... કહીને**",
                     " **#_Dgizool💖 તેથી દરેક પાસે તે છે, પરંતુ બધા પાસે નથી #💑इज़वालैमे❌…**",
                     " **#सूआंबस👂 #इजिता है तुमसेब**",
                     " **મેં #आपविज़ों ख्वाई 😇 દીવાલ બનાવી 😇, ખામખાન #જીવનમાં અનારકલી💃 બનીને નાચતો હતો**",
                     " **આહ જરૂર છે #વેડ☝ જ્યાં સુધી ઉંમર અસર થાય, જે જીવે ત્યાં સુધી 𝗧𝗥𝗮𝗶𝗻𝗶**",
                     " ** આગર વાગર વાગર વિશેષ વિશેષ અને હું એકલા રહેવું સારું ** ,
                     " ** ઝઘડો ત્યારે જ થાય જ્યારે # ડગર્ડ હોય, અને # પેર્ડ ત્યાં હોય જ્યાં # પજેજયર💝 હોય**",
                     " **#_Instagram𝗫 જો તમે #_Facebook ની વાત કરો છો, તો #_📌𝗫 તેના પર #લાડકી પણ સેટ કરે છે**",
                     " **#अमगेटलगीष की बूख बोख**",
                     " **#𝗣𝗿𝗮𝗿𝗶𝗶𝗻𝗶𝗶𝗶𝗶𝗶𝗶**",
                     " **તમારા #ભારતમાં ભલે તે #સરકાર હોય કે #શાદી👫, દરેકને ☝ વર્ષમાં #ખુસ ખબરી જોઈએ છે..**",
                     "** મને લાગે છે 🤔 બહુ જલ્દી પરિવારના સભ્યો મારો 🙄# 🌜મોબાઈલ 📲 અને ચાર્જર 🔌 પકડીને મને ઘરની બહાર ફેંકી દેશે**",
                     " ** હરિં એવા #લૌડી👸ને પ્રભાવિત કરશે જેઓ બહાર છે....જેને જોઈને #ડુળ💝 ને 𝟰𝟰0 વોલ્ટના આંચકા આવે છે.😂** ",
                     " ** જો તમારે સમય બગાડવો હોય તો 😏😂😂😀**",
                     " ** તમે આખા શહેરમાં કેમ નથી ફરતા, સૌથી વધુ #_હોટ_#લૉડી તો જ જોવા મળશે 💔💝 પરિવારના સભ્યો તમારી સાથે છે**",
                     " **મેં સાંભળ્યું છે કે છોકરીઓ #શાયરી લખીને વધુ પ્રભાવિત થાય છે….. ચાલો આ વર્ષે પણ ટ્રાય કરીએ😂😂**",
   
         ]



@app.on_message(filters.command(["gjtag"," gtag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("This command can be used in groups and channels!")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("Only admin can use this command!")

    if message.reply_to_message and message.text:
        return await message.reply("/htag Try this next time for tagging..")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/htag hii 👈 Try this or reply any message...")
    else:
        return await message.reply("/htag hii 👈 Try this or reply any message...")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("No active mention process is started by me.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("This command is only for admins. You can't use this command.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ Mention process stopped ♦")
