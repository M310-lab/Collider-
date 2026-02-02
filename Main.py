# VB Local Growth Telegram Bot
# Mobile-ready deployment
# Python 3.10+

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

from flask import Flask
from threading import Thread

# ---------------- CONFIG ----------------
BOT_TOKEN = 8404994831:AAEZtdfA5B-i08oZ3YWp1pP1cHeIf2iqpo8
PORT = 8080

# ---------------- FLASK KEEPALIVE ----------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running."

def run_flask():
    app.run(host="0.0.0.0", port=PORT)

Thread(target=run_flask).start()

# ---------------- BOT COMMANDS ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1️⃣ Build Offer", callback_data="offer")],
        [InlineKeyboardButton("2️⃣ Generate Outreach", callback_data="outreach")],
        [InlineKeyboardButton("3️⃣ Lead Audit Script", callback_data="audit")],
        [InlineKeyboardButton("4️⃣ Automation Setup", callback_data="automation")],
        [InlineKeyboardButton("5️⃣ Daily Prospecting Plan", callback_data="prospecting")]
    ]

    await update.message.reply_text(
        "🚀 *VB Local Growth – Mobile Lead-Gen Command Center*\n\n"
        "Tap a button to get instant scripts & workflows:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# ---------------- BUTTON HANDLER ----------------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        "offer": (
            "🎯 *BUILD OFFER*\n\n"
            "*One-Line Pitch:*\n"
            "We help Virginia Beach businesses get more calls, bookings, and reviews using automated local marketing.\n\n"
            "*Pricing:*\n"
            "• $750 / month – Starter\n"
            "• $1,250 / month – Growth\n\n"
            "*Best Targets:*\n"
            "• Restaurants\n"
            "• Pressure washing\n"
            "• Cleaning, landscaping, HVAC\n"
            "• Weak online presence"
        ),

        "outreach": (
            "📧 *OUTREACH SCRIPT*\n\n"
            "Hi — I’m local to Virginia Beach and help small businesses get more calls and bookings using simple automation.\n\n"
            "I noticed a few quick wins on Google that may be costing you customers.\n"
            "I recorded a short 2-minute video showing exactly what I mean.\n\n"
            "Want me to send it over?"
        ),

        "audit": (
            "🎥 *2-MINUTE LOOM AUDIT*\n\n"
            "Show ONLY problems:\n"
            "1. Google listing quality\n"
            "2. Review gap vs competitors\n"
            "3. Missed call risk\n"
            "4. No follow-up automation\n\n"
            "⚠️ Don’t explain fixes."
        ),

        "automation": (
            "⚙️ *AUTOMATION SETUP*\n\n"
            "*Missed Call SMS:*\n"
            "\"Sorry we missed your call — how can we help?\"\n\n"
            "*Lead Follow-Up:*\n"
            "SMS instantly → Email after 5 min → Reminder next day\n\n"
            "*Review Request SMS:*\n"
            "\"Thanks for choosing us! Would you mind leaving a quick review?\""
        ),

        "prospecting": (
            "📍 *DAILY PROSPECTING PLAN*\n\n"
            "*Search:*\n"
            "• restaurant Virginia Beach\n"
            "• pressure washing Virginia Beach\n"
            "• cleaning service Virginia Beach\n\n"
            "*Target:*\n"
            "• <100 reviews\n"
            "• Bad website\n"
            "• No automation\n\n"
            "*Daily Goal:* 10 prospects"
        )
    }

    await query.edit_message_text(
        responses.get(query.data, "Unknown option."),
        parse_mode="Markdown"
    )

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app_bot = ApplicationBuilder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CallbackQueryHandler(button_handler))
    python-telegram-bot==20.7
flask
