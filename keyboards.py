from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_admin_main_menu():
    buttons = [
        [KeyboardButton(text="👤 Info User"), KeyboardButton(text="📊 Info Account")],
        [KeyboardButton(text="🔑 Give Key"), KeyboardButton(text="📚 All Accounts")],
        [KeyboardButton(text="👥 All Users"), KeyboardButton(text="📁 APKs")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_user_main_menu():
    buttons = [
        [KeyboardButton(text="📋 Available Accounts")],
        [KeyboardButton(text="📥 Download Client APK"), KeyboardButton(text="📥 Download Admin APK")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_apk_menu():
    buttons = [
        [KeyboardButton(text="📲 Client APK"), KeyboardButton(text="📲 Admin APK")],
        [KeyboardButton(text="⬅️ Back")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_refresh_key_inline(account_number: str):
    button = InlineKeyboardButton(text="🔄 Refresh Key", callback_data=f"refresh_{account_number}")
    return InlineKeyboardMarkup(inline_keyboard=[[button]])

def get_ban_user_inline(user_id):
    buttons = [[InlineKeyboardButton(text="🚫 Ban User", callback_data=f"ban_{user_id}")]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_unban_user_inline(user_id):
    buttons = [[InlineKeyboardButton(text="✅ Unban User", callback_data=f"unban_{user_id}")]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
