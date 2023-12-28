import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram import F
from aiogram import html
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.formatting import Text, Bold
from datetime import datetime
from aiogram.types import FSInputFile, BufferedInputFile,InputFile
from aiogram.filters import Command
from aiogram.types import URLInputFile
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.formatting import(
    Bold, as_list, as_marked_section, as_key_value, HashTag
)
 

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6801749680:AAEJpOXUz_b5evaxxE_mdyuUwSZpMEUT19w")
# Диспетчер
dp = Dispatcher()

# (
#     Bold, as_list, as_marked_section, as_key_value, HashTag
# )

# @dp.message(Command("advanced_example"))
# async def cmd_advanced_example(message: Message):
#     content = as_list(
#         as_marked_section(
#             Bold("Success:"),
#             "Test 1",
#             "Test 3",
#             "Test 4",
#             marker="✅ ",
#         ),
#         as_marked_section(
#             Bold("Failed:"),
#             "Test 2",
#             marker="❌ ",
#         ),
#         as_marked_section(
#             Bold("Summary:"),
#             as_key_value("Total", 4),
#             as_key_value("Success", 3),
#             as_key_value("Failed", 1),
#             marker="  ",
#         ),
#         HashTag("#test"),
#         sep="\n\n",
#     )
#     await message.answer(**content.as_kwargs())
# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token="6801749680:AAEJpOXUz_b5evaxxE_mdyuUwSZpMEUT19w")
# # Диспетчер


dp = Dispatcher()
@dp.message(Command("images"))
async def cmd_images(message: types.Message):
    file_ids =[]
    with open("cat.jpg", "rb") as file:

        result = await message.answer_photo(
            BufferedInputFile(
                file.read(),
                filename="image from buffer.jpg"
            ),
            caption="Изображение из буфера")
        file_ids.append(result.photo[-1].file_id)
    image_from_pc = FSInputFile("Sunset.jpg")
    result = await message.answer_photo(
        image_from_pc,
         caption="Изображение из файла на компютер")
    file_ids.append(result.photo[-1].file_id)   


# image_from_url = URLInputFile("https://www.python.org/static/community_logos/python-powered-h-140x182.png")
# result = await message.answer_photo(
#     image_from_url,
#     caption="Изображение по ссылке"
# )
# file_ids.append(result.photo[-1].file_id)  
# await message.answer("Отправка фото :\n"+"\n".join(file_idc))
    


@dp.message(F.photo )
async def download_photo(message: Message, bot:Bot):
    await bot.download(
        message.photo[-1],
        destination=f"C:\\Users\\HP9\\Desktop\\{message.photo[-1].file_id}.jpg"
    )
    await message.answer(f"Фото сохранено в /tmp")
    




# # Хэндлер на команду /start
# @dp.message(F.text == 'Hello')
# async def echo_with_time(message: Message):
#     time_now = datetime.now().strftime('%H:%M')
#     added_text = html.underline(f"Создано в {time_now}")
#     await message.answer(f"{message.html_text}\n\n{added_text}", parse_mode="HTML")
# @dp.message(F.text == 'Hello')
# async def name(message:Message):
#     await message.answer(message.from_user.username)

# @dp.message(F.text)
# async def echo_with_time(message: Message):
#     time_now = datetime.now().strftime('%H:%M')
# added_text = html.underline(f"Создано в {time_now}")
# await message.answer(f"{message.text}\n\n{added_text}", parse_mode="HTML")
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")
# @dp.message(Command("hello"))
# async def cmd_hello(message: Message):
#     content = Text(
#         "Hello, ",
#         Bold(message.from_user.full_name)
#     )
#     await message.answer(
#         **content.as_kwargs()
#     )
# @dp.message(F.text == 'Hello')
# async def echo (message:Message):
#     await message.answer(message.text)    

# # @dp.message(Command("11"))
# # async def cmd_11(message: types.Message):
# #     await message.answer(emoji="😍")

# @dp.message(Command("Homework"))
# async def cmd_start(message: types.Message):
#     await message.answer("Select item!")    
    
# @dp.message(Command("help"))
# async def cmd_start(message: types.Message):
#     await message.reply("How can I help!")

# @dp.message(Command("Mathematics"))
# async def cmd_start(message: types.Message):
#     await message.answer("what class are you in?")


# # Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
