import telebot
import os
from openai import OpenAI
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("proj_VnLTI1SOTV3skpnk6OWP0Auw")
OPENAI_API_KEY = os.getenv("7622330651:AAH1F9WDw7McTspCyuCHUW2oGOlEXLTdm3U")

# تهيئة البوت
bot = telebot.TeleBot(7622330651:AAH1F9WDw7McTspCyuCHUW2oGOlEXLTdm3U)
openai_client = OpenAI(api_key=proj_VnLTI1SOTV3skpnk6OWP0Auw)

# 🚀 رسالة /start
@bot.message_handler(commands=["start"])
def start_message(message):
    user_name = message.from_user.first_name
    text = f"""مرحبا يا {user_name} 🔥.

تم تطوير هذا البوت من قبل chatgpt:open ai api

يرجى دعم ذكاء بايسني عن طريق استخدامه في عدة قنوات !!

اختار احد الزرين أدناه:
"""
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton("خيار جديد قيد التطوير 🔥", callback_data="dev"),
        telebot.types.InlineKeyboardButton("إضافة البوت إلى قناة ➕", callback_data="add_bot")
    )
    
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

# ✅ زر "خيار جديد قيد التطوير"
@bot.callback_query_handler(func=lambda call: call.data == "dev")
def dev_feature(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "خيار قيد التطوير ⚒️.")

# ✅ زر "إضافة البوت إلى قناة"
@bot.callback_query_handler(func=lambda call: call.data == "add_bot")
def add_bot_to_channel(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "عند إضافة البوت إلى القناة سوف يتعامل معك بذكاء كذكاء GPT-4o 🔥\n\nيجب منحه صلاحيات الإرسال على الأقل.")

# 🚀 معالجة أوامر الذكاء الاصطناعي في القنوات (يعمل عند منحه صلاحية إرسال الرسائل)
@bot.message_handler(commands=["ai"])
def ai_command(message):
    user_input = message.text.replace("/ai", "").strip()
    if not user_input:
        bot.send_message(message.chat.id, "يرجى كتابة السؤال بعد `/ai`")
        return
    
    bot.send_chat_action(message.chat.id, "typing")  # إظهار مؤشر الكتابة
    
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_input}]
        )
        bot.send_message(message.chat.id, response.choices[0].message.content)
    except Exception as e:
        bot.send_message(message.chat.id, "حدث خطأ أثناء محاولة التواصل مع OpenAI.")

# 🚀 تشغيل البوت
print("✅ بوت التليجرام يعمل الآن...")
bot.infinity_polling()
