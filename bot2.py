import pandas as pd
import requests
from bs4 import BeautifulSoup

user_id = 12345
film1 = requests.get("https://www.kinoafisha.info/rating/movies/")
soup1 = BeautifulSoup(film1.content, "html.parser")

merger = pd.DataFrame()
#####
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
test_df = pd.DataFrame(columns=["name", "cla", "years", "country"])
films = soup1.find_all('div', class_="movieList_item")
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

# film2 = requests.get("https://www.kinoafisha.info/rating/movies/?page=1")
# soup2 = BeautifulSoup(film2.content, "html.parser")
#
# merger = pd.DataFrame()
# #####
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# test_df = pd.DataFrame(columns=["name", "cla", "years", "country"])
# films = soup2.find_all('div', class_="movieList_item")
# for film in films:
#     title = film.find('a', class_="movieItem_title").text.strip()
#     cla = film.find('span', class_="movieItem_genres").text.strip()
#     year = film.find('span', class_="movieItem_year").text.strip()
#     # years = len(year) // 2
#     x = year.split(",")
#     test_df.loc[counter, "name"] = title
#     test_df.loc[counter, "cla"] = cla
#     test_df.loc[counter, "years"] = x[0]
#     test_df.loc[counter, "country"] = x[1]
#     counter += 1
# #print(test_df)
# #print(test_df.sample())

anime3 = requests.get("https://animestars.org/aniserials/video/")
soup3 = BeautifulSoup(anime3.content, "html.parser")

merger = pd.DataFrame()
#####

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
anime_df = pd.DataFrame(columns=["name", "cla", "years"])
anime = soup3.find_all('a', class_="poster grid-item d-flex fd-column has-overlay")
counter = 0
for film in anime:
        title = film.find('h3', class_="poster__title ws-nowrap").text.strip()
        year = film.find('div', class_="poster__meta flex-grow-1 ws-nowrap").text.strip()
        x = year.split(",", 1)
        anime_df.loc[counter, "name"] = title
        anime_df.loc[counter, "years"] = x[0]
        anime_df.loc[counter, "cla"] = x[1]
        counter += 1


from aiogram import Bot, Dispatcher, executor,types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


TOKEN=''
bot=Bot(token=TOKEN)
dp=Dispatcher(bot)

button_hi = KeyboardButton('привет')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

button_game1=KeyboardButton('мультик')
button_game2=KeyboardButton('сирик')
button_NO=KeyboardButton('анумэ')
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
    if msg.text.lower() == 'мультик':
        await msg.answer('думаю как сделать')
    if msg.text.lower() == 'сирик':
        await msg.answer('думаю как сделать')
    if msg.text.lower() == 'анумэ':
        sam_anime = anime_df.sample()
        sam_anime = '\n'.join(sam_anime.to_string(index=False).split('\n')[1:])
        await msg.answer(f'{sam_anime}')

if __name__ == '__main__':
    executor.start_polling(dp)