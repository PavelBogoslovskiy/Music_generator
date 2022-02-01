import time
from aiogram import Bot, Dispatcher, executor, types
from main import text_gen
from data import API_TOKEN
import logging

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
CONTENT_TYPES = ["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]


@dp.message_handler(commands=['start'])
async def start(message: types.Message):  # много пользователей могут ему писать обработает все запросы
    user_first_name = message.from_user.first_name
    user_id = message.from_user.id
    logging.info(f'{user_id} {user_first_name} started the MusicBot at {time.asctime()}')
    await message.reply(f"Привет, {user_first_name} !\nЯ MusicBot!\nПришли мне начало песни, а я ее продолжу..")
    await message.answer_sticker(r'CAACAgIAAxkBAAEDyDxh-P_ur__U8dK0EHllcRoa0NDZAQAC6CQAAp7OCwABx40TskPHi3MjBA')


@dp.message_handler(content_types=["text"])
async def musgen(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEDyDhh-P62yzJW7H1CKGiU7e8CDFCYlQACBCUAAp7OCwABE30V36lyBr8jBA')
    text_gen(message.text)
    await message.answer(text_gen(message.text))
    await bot.send_audio(message.from_user.id, open("mixed_sounds.mp3", 'rb'), performer="Нейроштука", title="Песня")


@dp.message_handler(content_types=CONTENT_TYPES)
async def nottext(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEDyDph-P8ovipaq8MUXzlClT-zsoG_zwACCyUAAp7OCwABrghZgrziDy4jBA')
    await message.answer('Пришли мне текст, пожалуйста!')


if __name__ == '__main__':
    executor.start_polling(dp)
