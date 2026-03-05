import os
from aiogram import Router, types, F
from api_client import backend_api
from keyboards import get_user_main_menu, get_apk_menu
from dotenv import load_dotenv


load_dotenv()

router = Router()

@router.message(F.text == "📋 Available Accounts")
async def show_accounts(message: types.Message):
    accounts = await backend_api.get_available_accounts(telegram_id=message.from_user.id)
    if "error" in accounts:
        return
    
    if not accounts:
        await message.answer("📭 Немає доступних акаунтів.")
        return
    
    text = "🔑 Доступні ключі:\n" + "\n".join([f"• <code>{acc.get('key')}</code>" for acc in accounts])
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "📁 APKs")
async def show_apk_menu(message: types.Message):
    await message.answer("Оберіть APK для завантаження:", reply_markup=get_apk_menu())

@router.message(F.text == "❓ Как пользоваться")
async def how_to_use(message: types.Message):
    contacts = os.getenv("CONTACTS", "Контакти не вказані у .env")
    await message.answer(f"ℹ️ **Як користуватися:**\n\n{contacts}", parse_mode="Markdown")

@router.message(F.text == "📲 Client APK")
async def download_client_apk(message: types.Message):
    # Hardcoded forwarding: Client ID 6 from specific channel
    channel_id = os.getenv("CHANNEL_ID")
    try:
        await message.bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=channel_id,
            message_id=os.getenv("CLIENT_APK")
        )
    except Exception as e:
        pass
    else:
        instruction = os.getenv("CLIENT_INSTRUCTION", "Інструкція відсутня.")
        await message.answer(f"📋 **Інструкція (Клієнт):**\n{instruction}", parse_mode="Markdown")

@router.message(F.text == "📲 Admin APK")
async def download_admin_apk(message: types.Message):
    # Hardcoded forwarding: Admin ID 7 from specific channel
    channel_id = os.getenv("CHANNEL_ID")
    try:
        await message.bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=channel_id,
            message_id=os.getenv("ADMIN_APK")
        )
    except Exception as e:
        pass
    else:
        instruction = os.getenv("ADMIN_INSTRUCTION", "Інструкція відсутня.")
        await message.answer(f"📋 **Інструкція (Адмін):**\n{instruction}", parse_mode="Markdown")
