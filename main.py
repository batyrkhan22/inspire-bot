import asyncio
import logging
import aiohttp
import re
import random
from datetime import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
import database

TOKEN = "8749688320:AAF0SWMkLUVnY7xXZyZocXKBgvldnbhuQRc"
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)


class UserStates(StatesGroup):
    waiting_for_time = State()
    waiting_for_feedback = State()
    waiting_for_custom_quote = State()
    waiting_for_font_choice = State()


# --- Әдемі эмоджилер мен шрифт стильдері ---
EMOJIS = {
    "happy": ["✨", "🌟", "💫", "⭐", "🌸", "💖", "😊", "🌈"],
    "motivational": ["💪", "🔥", "🚀", "⭐", "🎯", "💯", "⚡", "🌟"],
    "calm": ["🌊", "🍃", "🌙", "💫", "🕊️", "🌸", "🌿", "✨"],
    "cool": ["🔥", "💎", "👑", "⚡", "🎨", "💫", "🚀", "✨"]
}

FONTS_STYLE = {
    "bold": "**{}**",
    "italic": "_{}_",
    "bold_italic": "***{}***",
    "code": "`{}`",
    "spoiler": "||{}||",
    "underline": "<u>{}</u>"
}


# --- Menu ---
def get_main_menu():
    kb = [
        [KeyboardButton(text="💡 Random Quote"), KeyboardButton(text="✍️ My Own Quote")],
        [KeyboardButton(text="⚙️ Daily Reminder"), KeyboardButton(text="📝 Feedback")],
        [KeyboardButton(text="❓ Help"), KeyboardButton(text="👤 About")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


# --- Get random quote from API ---
async def get_quote():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://zenquotes.io/api/random", timeout=5) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data[0]['q']
                else:
                    return "Believe in yourself! ✨"
    except Exception as e:
        logging.error(f"Quote API error: {e}")
        return "Keep going. Every step counts! 💪"


def beautify_text(text, font_style=None, emoji_style=None):
    """Beautify text with emojis and font styling"""

    # Add emojis
    if emoji_style and emoji_style in EMOJIS:
        emojis = EMOJIS[emoji_style]
        emoji_left = random.choice(emojis)
        emoji_right = random.choice(emojis)
        text = f"{emoji_left} {text} {emoji_right}"
    else:
        # Random emojis
        all_emojis = EMOJIS["happy"] + EMOJIS["motivational"]
        emoji_left = random.choice(all_emojis)
        emoji_right = random.choice(all_emojis)
        text = f"{emoji_left} {text} {emoji_right}"

    # Add font style
    if font_style and font_style in FONTS_STYLE:
        text = FONTS_STYLE[font_style].format(text)

    return text


# --- Dialogues ---
@dp.message(F.text.lower().in_(['hi', 'hello', 'hey', 'salem', 'start']))
async def greet(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "✨ Hello! I'm **InspAIre Bot**!\n\n"
        "Send me any text, and I'll make it beautiful with emojis and fancy fonts! 🎨\n\n"
        "Try **✍️ My Own Quote** to get started!",
        reply_markup=get_main_menu()
    )


@dp.message(F.text.lower().in_(['how are you', 'how r u', 'calyn']))
async def status(message: Message):
    await message.answer("💖 I'm full of inspiration! Ready to beautify your words. And you?")


@dp.message(F.text.lower().in_(['good', 'great', 'awesome', 'amazing', 'jaksy']))
async def good(message: Message):
    await message.answer("🌟 Awesome! Try **✍️ My Own Quote** - write anything, I'll make it look amazing!")


@dp.message(F.text.lower().in_(['thanks', 'thank you', 'rahmet', 'thanks bot']))
async def thanks(message: Message):
    await message.answer("🌸 You're welcome! Come back anytime for beautiful quotes! 💫")


@dp.message(F.text.lower().in_(['love', 'i love you', 'suyemin']))
async def love(message: Message):
    await message.answer("💖 Aww, love you too! Stay inspired, my friend! 🌟")


@dp.message(F.text.lower().in_(['joke', 'funny', 'kale']))
async def tell_joke(message: Message):
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😆",
        "What do you call a fake noodle? An impasta! 🍝",
        "Why don't scientists trust atoms? Because they make up everything! ⚛️"
    ]
    await message.answer(random.choice(jokes))


# --- Start Command ---
@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    database.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
    await message.answer(
        "🌟 Welcome to **InspAIre Bot**!\n\n"
        "I take your words and make them **beautiful** with:\n"
        "✨ Fancy emojis\n"
        "🎨 Cool text styles (bold, italic, etc.)\n\n"
        "👇 Click **✍️ My Own Quote** to try it now!",
        reply_markup=get_main_menu()
    )


# --- Random Quote ---
@dp.message(F.text == "💡 Random Quote")
async def handle_quote(message: Message):
    quote = await get_quote()
    # Beautify the random quote
    beautiful_quote = beautify_text(quote, font_style="bold_italic", emoji_style="motivational")
    await message.answer(f"💡 Your daily spark:\n\n{beautiful_quote}", parse_mode="Markdown")


# --- MY OWN QUOTE (Main feature - text beautification) ---
@dp.message(F.text == "✍️ My Own Quote")
async def custom_quote_start(message: Message, state: FSMContext):
    await message.answer(
        "✏️ **Send me your text/quote:**\n\n"
        "Example: *The best way out is always through*\n\n"
        "I'll make it beautiful with emojis and fancy styles! ✨"
    )
    await state.set_state(UserStates.waiting_for_custom_quote)


@dp.message(UserStates.waiting_for_custom_quote)
async def ask_beautify_style(message: Message, state: FSMContext):
    if len(message.text) > 500:
        await message.answer("⚠️ Too long! Please send shorter text (max 500 chars).")
        return

    await state.update_data(quote=message.text)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎲 Surprise Me! (Random)", callback_data="surprise")],
        [InlineKeyboardButton(text="🎨 Customize Style", callback_data="customize")]
    ])
    await message.answer("🎨 **How would you like to beautify your text?**", reply_markup=kb)


@dp.callback_query(F.data == "surprise")
async def surprise_beautify(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    quote = data.get("quote")

    # Random font style
    font_styles = list(FONTS_STYLE.keys())
    random_font = random.choice(font_styles)

    # Random emoji style
    emoji_styles = list(EMOJIS.keys())
    random_emoji = random.choice(emoji_styles)

    beautiful_text = beautify_text(quote, font_style=random_font, emoji_style=random_emoji)

    await call.message.answer(
        f"✨ **Your beautified text:** ✨\n\n"
        f"{beautiful_text}\n\n"
        f"📝 Style: *{random_font}* | Emojis: *{random_emoji}*",
        parse_mode="Markdown"
    )
    await state.clear()


@dp.callback_query(F.data == "customize")
async def show_font_options(call: CallbackQuery, state: FSMContext):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 Bold", callback_data="font_bold")],
        [InlineKeyboardButton(text="🌸 Italic", callback_data="font_italic")],
        [InlineKeyboardButton(text="⭐ Bold + Italic", callback_data="font_bold_italic")],
        [InlineKeyboardButton(text="💻 Code", callback_data="font_code")],
        [InlineKeyboardButton(text="🎭 Spoiler (hidden)", callback_data="font_spoiler")],
        [InlineKeyboardButton(text="📝 Underline", callback_data="font_underline")]
    ])
    await call.message.edit_text("🎨 **Choose a font style:**", reply_markup=kb)


@dp.callback_query(F.data.startswith("font_"))
async def show_emoji_options(call: CallbackQuery, state: FSMContext):
    font_style = call.data.split("font_")[1]
    await state.update_data(selected_font=font_style)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="😊 Happy Emojis", callback_data="emoji_happy")],
        [InlineKeyboardButton(text="💪 Motivational Emojis", callback_data="emoji_motivational")],
        [InlineKeyboardButton(text="🌊 Calm Emojis", callback_data="emoji_calm")],
        [InlineKeyboardButton(text="🔥 Cool Emojis", callback_data="emoji_cool")],
        [InlineKeyboardButton(text="🎲 Random Emojis", callback_data="emoji_random")]
    ])
    await call.message.edit_text(f"📝 Font: *{font_style}*\n\nNow choose emoji style:", parse_mode="Markdown",
                                 reply_markup=kb)


@dp.callback_query(F.data.startswith("emoji_"))
async def final_beautify(call: CallbackQuery, state: FSMContext):
    emoji_choice = call.data.split("emoji_")[1]
    data = await state.get_data()
    quote = data.get("quote")
    font_style = data.get("selected_font")

    if emoji_choice == "random":
        emoji_style = random.choice(list(EMOJIS.keys()))
    else:
        emoji_style = emoji_choice

    beautiful_text = beautify_text(quote, font_style=font_style, emoji_style=emoji_style)

    await call.message.answer(
        f"✨ **Your beautified text:** ✨\n\n"
        f"{beautiful_text}\n\n"
        f"📝 Font: *{font_style}* | Emojis: *{emoji_style}*",
        parse_mode="Markdown"
    )
    await state.clear()


# --- Daily Reminder ---
@dp.message(F.text == "⚙️ Daily Reminder")
async def cmd_settings(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("⏰ Set daily motivation time (HH:MM format, e.g., 09:00 or 18:30):")
    await state.set_state(UserStates.waiting_for_time)


@dp.message(UserStates.waiting_for_time)
async def process_time(message: Message, state: FSMContext):
    if not re.match(r"^\d{2}:\d{2}$", message.text):
        await message.answer("❌ Invalid! Use HH:MM (e.g., 09:00)")
        return
    database.update_time(message.from_user.id, message.text)
    await message.answer(f"✅ Daily reminder set for **{message.text}**! I'll send you motivation every day.",
                         parse_mode="Markdown")
    await state.clear()


# --- Feedback ---
@dp.message(F.text == "📝 Feedback")
async def cmd_feedback(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("💬 Send me your feedback or suggestions to help me improve:")
    await state.set_state(UserStates.waiting_for_feedback)


@dp.message(UserStates.waiting_for_feedback)
async def process_feedback(message: Message, state: FSMContext):
    database.add_feedback(message.from_user.id, message.text)
    await message.answer("🙏 Thank you so much for your feedback! 💖")
    await state.clear()


# --- About & Help ---
@dp.message(F.text == "👤 About")
async def cmd_about(message: Message):
    await message.answer(
        "🤖 **InspAIre Bot v3.0**\n\n"
        "✨ **What I do:**\n"
        "• Take your text and make it beautiful\n"
        "• Add fancy emojis around your words\n"
        "• Apply cool text styles (bold, italic, etc.)\n"
        "• Send daily motivation quotes\n\n"
        "💡 **Try it:** Click **✍️ My Own Quote**!\n\n"
        "_Made with love_ 💖",
        parse_mode="Markdown"
    )


@dp.message(F.text == "❓ Help")
async def cmd_help(message: Message):
    help_text = """
❓ **Help Guide**

📌 **Main Features:**

1️⃣ **✍️ My Own Quote**
   - Send any text
   - Choose random OR customize font & emojis
   - Get beautifully formatted text back!

2️⃣ **💡 Random Quote**
   - Get daily motivational quote
   - Automatically beautified

3️⃣ **⚙️ Daily Reminder**
   - Set time for daily motivation

4️⃣ **📝 Feedback**
   - Send me your suggestions

💬 **Chat with me naturally!** Try: Hello, How are you, Thanks, Joke

---

✨ **Text Styles:** Bold, Italic, Code, Spoiler, Underline
😊 **Emoji Styles:** Happy, Motivational, Calm, Cool, Random
"""
    await message.answer(help_text)


# --- Beautify any text without command (extra feature) ---
@dp.message(F.text.len() > 5)
async def auto_beautify(message: Message, state: FSMContext):
    # Don't auto-beautify if user is in any state
    current_state = await state.get_state()
    if current_state is not None:
        return

    # Auto beautify long messages
    if len(message.text) < 500 and not message.text.startswith("/"):
        beautiful = beautify_text(message.text, font_style="italic", emoji_style="happy")
        await message.answer(f"✨ Here's your beautified text:\n\n{beautiful}", parse_mode="Markdown")


# --- Unknown commands ---
@dp.message(F.text.in_(['/help', '/about', '/start']))
async def handle_commands(message: Message):
    pass  # Already handled


@dp.message()
async def unknown(message: Message):
    await message.answer("🤔 I don't understand that. Click **❓ Help** to see what I can do!")


# --- Daily scheduler ---
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()


async def send_daily_quotes():
    users = database.get_all_users_with_time()
    now = datetime.now().strftime("%H:%M")
    for user_id, notify_time in users:
        if notify_time == now:
            quote = await get_quote()
            beautiful_quote = beautify_text(quote, font_style="bold_italic", emoji_style="motivational")
            try:
                await bot.send_message(user_id, f"🌅 **Daily Motivation**\n\n{beautiful_quote}", parse_mode="Markdown")
            except Exception as e:
                logging.error(f"Can't send to {user_id}: {e}")


scheduler.add_job(send_daily_quotes, "interval", minutes=1)


async def main():
    database.init_db()
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())