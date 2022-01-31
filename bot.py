import time
from aiogram import Bot, Dispatcher, executor, types
from main import text_gen
from data import API_TOKEN



# Configure logging # Включаем логирование
import logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):  # много пользователей могут ему писать обработает все запросы
    user_first_name = message.from_user.first_name
    user_id = message.from_user.id
    logging.info(f'{user_id} {user_first_name} started the MusicBot at {time.asctime()}')
    await message.reply(f"Hi, {user_first_name} !\nI'm TimeByClockBot!\nSend me a picture of the watch")


# @dp.message_handler(content_types=['photo'])
# async def handleR_photo(message):
#     # media_group_id is None means single photo at message
#     if message.media_group_id is None:
#         user_id = message.from_user.id
#         message_id = message.message_id
#         img_path = 'uploaded_images/%s_%s_%s.jpg' % (user_id, 'first_name', message_id)
#         await message.photo[-1].download(img_path)
#         await message.answer_sticker(r'CAACAgIAAxkBAAEDwgdh8W1GvrfQg63xacgdWjJ1vtMdNwACESUAAp7OCwABwHeW06BpLm0jBA')
#         pred = predictor(img_path)
#         if not pred[1]:
#             await message.answer_sticker(r'CAACAgIAAxkBAAEDwglh8W6BMY6iD-fGaUrsg6TbPnmvKgACFSUAAp7OCwAB8UnI6IhTMgABIwQ')
#         await message.reply(pred[0])
#
#     else:
#         await message.reply("Send me just one photo, please")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text_gen(message.text))
    await bot.send_audio(message.from_user.id, open("mixed_sounds.mp3" ,'rb'), performer="Нейроштука", title="Песня")
    # await message.reply("Send me image, please")


if __name__ == '__main__':
    executor.start_polling(dp)