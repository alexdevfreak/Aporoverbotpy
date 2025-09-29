from pyrogram import Client
from pyrogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton

# ==========================
#  BOT CONFIG
# ==========================
API_ID = 123456          # your API ID (from my.telegram.org)
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client(
    "approve-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ==========================
#  CUSTOM WELCOME MESSAGE
# ==========================
WELCOME_TEXT = """<a href='https://share.google/images/Lvy1Y3SfHHif5nVwA'></a>

⬡ <b>MEGA Indian Pack 2</b>
<blockquote>#MostDemanded #HandPicked</blockquote>
━━━━━━━━━━━━━━━━━━━━━━
‣ <i>Media :</i> 50,00,000+
‣ <i>Length :</i> 1000hrs+
‣ <i>Genres :</i> Etc,Etc,Etc
━━━━━━━━━━━━━━━━━━━━━━

<b>ONLY ON :</b> ₹499 ₹99
<b>ONLY ON :</b> <s>₹499</s> <b>₹99</b>

<blockquote><i>Note: It Contains Personally Watched And Paid Contents</i></blockquote>

Hello {mention}!
Welcome to {title}!
"""

# ==========================
#  BUTTON
# ==========================
BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton(
            "💳 Pᴀʏ Nᴏᴡ",
            url="http://t.me/alex_clb?&text=Rᴇǫᴜᴇsᴛɪɴɢ%20Pʀᴇᴍɪᴜᴍ%20Pᴀᴄᴋ%20%E2%82%B999%20Vɪᴘ2"
        )
    ]]
)

# ==========================
#  HANDLER FOR JOIN REQUESTS
# ==========================
@app.on_chat_join_request()
async def handle_join_request(client, request: ChatJoinRequest):
    try:
        # Approve the user's join request
        await client.approve_chat_join_request(request.chat.id, request.from_user.id)

        # Send the welcome message to the user privately
        await client.send_message(
            request.from_user.id,
            WELCOME_TEXT.format(
                mention=request.from_user.mention,
                title=request.chat.title
            ),
            parse_mode="html",
            reply_markup=BUTTONS
        )

    except Exception as e:
        print("Error:", e)


# ==========================
#  START BOT
# ==========================
print("🚀 Request Approve Bot is running...")
app.run()
