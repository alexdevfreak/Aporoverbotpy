from pyrogram import Client
from pyrogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
import config

# ==========================
#  CREATE BOT
# ==========================
app = Client(
    "approve-bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# ==========================
#  BUTTON INLINE KEYBOARD
# ==========================
BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton(
            config.BUTTON_TEXT,
            url=config.BUTTON_URL
        )
    ]]
)

# ==========================
#  HANDLE CHANNEL JOIN REQUESTS
# ==========================
@app.on_chat_join_request()
async def handle_join_request(client, request: ChatJoinRequest):
    try:
        # Approve the join request automatically
        await client.approve_chat_join_request(request.chat.id, request.from_user.id)

        # Send the welcome message privately to the user
        await client.send_message(
            request.from_user.id,
            config.WELCOME_TEXT.format(
                mention=request.from_user.mention,
                title=request.chat.title
            ),
            parse_mode="html",
            reply_markup=BUTTONS
        )

    except Exception as e:
        print(f"Error handling join request for {request.from_user.id}: {e}")

# ==========================
#  START BOT
# ==========================
print("🚀 Request Approve Bot is running...")
app.run()
