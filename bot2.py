import pandas as pd
import requests
from bs4 import BeautifulSoup

user_id = 12345
response = requests.get("https://www.kinoafisha.info/rating/movies/")
soup = BeautifulSoup(response.content, "html.parser")

merger = pd.DataFrame()
#####
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
test_df = pd.DataFrame(columns=["name", "cla", "years", "country"])
films = soup.find_all('div', class_="movieList_item")
counter = 0
for film in films:
    title = film.find('a', class_="movieItem_title").text.strip()
    cla = film.find('span', class_="movieItem_genres").text.strip()
    year = film.find('span', class_="movieItem_year").text.strip()
    # years = len(year) // 2
    x = year.split(",")
    test_df.loc[counter, "name"] = title
    test_df.loc[counter, "cla"] = cla
    test_df.loc[counter, "years"] = x[0]
    test_df.loc[counter, "country"] = x[1]
    counter += 1

user_id = 12345
response = requests.get("https://www.kinoafisha.info/rating/movies/?page=1")
soup = BeautifulSoup(response.content, "html.parser")

merger = pd.DataFrame()
#####
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
test_df = pd.DataFrame(columns=["name", "cla", "years", "country"])
films = soup.find_all('div', class_="movieList_item")
for film in films:
    title = film.find('a', class_="movieItem_title").text.strip()
    cla = film.find('span', class_="movieItem_genres").text.strip()
    year = film.find('span', class_="movieItem_year").text.strip()
    # years = len(year) // 2
    x = year.split(",")
    test_df.loc[counter, "name"] = title
    test_df.loc[counter, "cla"] = cla
    test_df.loc[counter, "years"] = x[0]
    test_df.loc[counter, "country"] = x[1]
    counter += 1
#print(test_df)
#print(test_df.sample())

from aiogram import Bot, Dispatcher, executor,types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


TOKEN=''
bot=Bot(token=TOKEN)
dp=Dispatcher(bot)

button_hi = KeyboardButton('привет')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

button_game1=KeyboardButton('давай в камень, ножницы тупо зарубим')
button_game2=KeyboardButton('не, ну можно и в угадай число')
button_NO=KeyboardButton('да чет влом сорри')
button_film=KeyboardButton('давай фильм')
greet3=ReplyKeyboardMarkup().add(button_game1).add(button_game2).add(button_film).add(button_NO)


@dp.message_handler(commands=['start','help'])
async def send_welcome(msg: types.Message):
    await msg.reply('Хай чунга чанга я Butuz!\nКамень, ножницы, бумага?\nИли может угадай число?\nА может фильмец посоветовать?', reply_markup=greet3)

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'давай фильм':
        sam_film = test_df.sample()
        sam_film = '\n'.join(sam_film.to_string(index=False).split('\n')[1:])
        await msg.answer(f'{sam_film}')
    if msg.text.lower() == 'не, ну можно и в угадай число':
        import random
        RandomnoeChislo = random.randint(1, 100)
        NasheChislo = -1
        while NasheChislo != RandomnoeChislo:
            @dp.message_handler()
            async def echo_message(msg: types.Message):
                NasheChislo = msg.text
                NasheChislo = bot.send_message(message.chat.id, 'Угадайте число от 1 до 100')
                if NasheChislo > RandomnoeChislo:
                    await NasheChislo.text("Число должно быть меньше вонючка")
                elif NasheChislo < RandomnoeChislo:
                    await NasheChislo.text(("Число должно быть больше козел"))
                else:
                    await NasheChislo.text("Ооооооо яяяяяя дастишь фантастишь")
    if msg.text.lower() == 'давай в камень, ножницы тупо зарубим':
        await msg.answer('думаю как сделать')
    if msg.text.lower() == 'да чет влом сорри':
        await msg.answer('пока')

if __name__ == '__main__':
    executor.start_polling(dp)
