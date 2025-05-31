import telebot
from telebot import types
import os
import random
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('7730117183:AAGJsFIUjsgDeY_U2H29Htw1xeniLa3Ya5k')

@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, "Приветсвуйю, исследователь! Этот бот поможет узнать тебе о глобальном потеплении. Причины , последствия и бла-бла-бла... Напиши /help", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """ Список команд:
/reasons
/consequences
/methods_of_struggle
/opinion_of_scientists
/What_can_you_do
/FSA
/Facts
/Begining
/Reasons_to_watch_Oshi_no_KO
/photos
/news""", reply_markup=markup)

@bot.message_handler(commands=['consequences'])
def consequences(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Список последствий:
/first
/second
/third
/fourth
/fifth
/sixth""", reply_markup=markup)

@bot.message_handler(commands=['first'])
def first_c(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Повышение температуры 
🌡 Рост средних температур – Земля уже нагрелась на ~1,2°C с доиндустриального уровня. Без действий к 2100 году потепление может достичь 2–4°C или больше.
🔥 Аномальная жара – участились волны тепла (например, в Европе, Северной Америке, Азии), что приводит к смертям, пожарам и нагрузке на энергосистемы.""", reply_markup=markup)

@bot.message_handler(commands=['second'])
def second_c(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Таяние льдов и повышение уровня моря
🧊 Исчезновение ледников – Гренландия и Антарктида теряют лёд, что ускоряет рост уровня океана.
🌊 Подтопление территорий – к 2100 году уровень моря может подняться на 0,5–2 м, угрожая прибрежным городам (Майами, Шанхай, Венеция, Бангладеш).
❄ Деградация вечной мерзлоты – высвобождает метан (сильный парниковый газ) и разрушает инфраструктуру в Сибири и Канаде.""", reply_markup=markup)

@bot.message_handler(commands=['third'])
def third_c(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Экстремальные погодные явления
🌀 Усиление ураганов и штормов – тёплые океаны дают больше энергии тропическим циклонам (как ураган 'Катрина' или 'Ирма').
🌪 Засухи и наводнения – одни регионы страдают от нехватки воды (Африка, Калифорния), другие – от катастрофических ливней (Европа, Южная Азия).""", reply_markup=markup)

@bot.message_handler(commands=['fourth'])
def fourth_c(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Угроза биоразнообразию
🐻 Вымирание видов – многие животные (белые медведи, кораллы) не успевают адаптироваться.
🌳 Гибель экосистем – обесцвечивание кораллов, гибель лесов из-за засух и вредителей.""", reply_markup=markup)

@bot.message_handler(commands=['fifth'])
def fifth_c(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Экономические и социальные последствия
💸 Ущерб экономике – расходы на борьбу с пожарами, наводнениями, переселение людей.
🌾 Снижение урожаев – в тропиках урожайность падает, растёт угроза голода.
 🏚 Климатические мигранты – к 2050 году до 200 млн человек могут стать беженцами из-за изменений климата.""", reply_markup=markup)

@bot.message_handler(commands=['sixth'])
def sixth_c(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Здоровье людей
🦠 Распространение болезней – комары-переносчики малярии и лихорадки денге расширяют ареал.
😷 Ухудшение качества воздуха – рост аллергий, астмы из-за жары и смога.""", reply_markup=markup)

@bot.message_handler(commands=['reasons'])
def reasons(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Глобальное потепление вызвано усилением парникового эффекта из-за роста концентрации парниковых газов в атмосфере.
Основные причины делятся на естественные и антропогенные (связанные с деятельностью человека):
/natural
/antropogenic""", reply_markup=markup)

@bot.message_handler(commands=['natural'])
def natural(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """🌍 Естественные причины.
☀️ Солнечная активность – небольшие колебания энергии Солнца.
🌋 Вулканическая деятельность – выбросы CO₂ и аэрозолей (но вулканы охлаждают планету из-за пепла в атмосфере).
🌀 Океанские течения – влияют на распределение тепла.
🌌Природные циклы (Миланковича) – изменения орбиты Земли (но действуют за десятки тысяч лет).
🌫️ Природные парниковые газы – Вулканы и болота выделяют CO₂ и метан, но в малых количествах.""", reply_markup=markup)

@bot.message_handler(commands=['antropogenic'])
def reasons(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """👨‍🦰Антропогенные причины (основной вклад в потепление)
1. Сжигание ископаемого топлива (главная причина)
⚡ Электростанции (уголь, нефть, газ) – дают ~60% выбросов CO₂.
🚗 Транспорт – автомобили, самолёты, суда (сжигание бензина и дизеля).
🏭 Промышленность – производство цемента, металлов, химических продуктов.
2. Вырубка лесов (дефорестация)
🌳 Леса поглощают CO₂, но их массовая вырубка (Амазония, Сибирь, Индонезия) снижает способность планеты очищать воздух.
3. Сельское хозяйство
🐄 Животноводство – коровы выделяют метан (CH₄), который в 25 раз сильнее CO₂.
🌾 Рисовые поля – выделяют метан при заболачивании.
💨 Удобрения – производят закись азота (N₂O), мощный парниковый газ.
4. Промышленные выбросы
🏭 Фреоны и хладагенты (используются в холодильниках и кондиционерах) разрушают озоновый слой и усиливают парниковый эффект.
5. Урбанизация и загрязнение
🏙 Города – создают 'острова тепла', усиливая локальное потепление.
🗑 Свалки – разлагающийся мусор выделяет метан.""", reply_markup=markup)

@bot.message_handler(commands=['methods_of_struggle'])
def methods(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Сократить выбросы 🏭→🌱
Улавливание и хранение углерода 🕸️
Геоинженерия (спорно! ⚠️)
Адаптация 🛡️
Международные соглашения и политика 📜🤝
Изменение потребительского поведения ♻️""", reply_markup=markup)

@bot.message_handler(commands=['opinion_of_scientists'])
def opinion(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Подавляющее большинство климатологов (свыше 97%) единодушно признают: глобальное потепление - реальный и стремительно развивающийся процесс, вызванный преимущественно деятельностью человека. Температура Земли уже повысилась на 1.1°C по сравнению с доиндустриальным уровнем, причём последние десятилетия неизменно бьют температурные рекорды. Основная причина - колоссальные выбросы углекислого газа от сжигания ископаемого топлива, что подтверждается многочисленными исследованиями ледниковых кернов, спутниковыми данными и климатическими моделями.
Учёные предупреждают о катастрофических последствиях: таяние ледников и вечной мерзлоты, повышение уровня моря, учащение экстремальных погодных явлений - от разрушительных ураганов до продолжительных засух. Особую тревогу вызывает возможность достижения 'переломных моментов' - необратимых изменений климатической системы, таких как гибель амазонских лесов или остановка Гольфстрима.
Среди научного сообщества ведутся дискуссии о сроках наступления критических изменений и оптимальных путях решения проблемы. Консервативная часть учёных настаивает на радикальном сокращении выбросов через переход на возобновляемую энергетику, повышение энергоэффективности и защиту экосистем. Более радикально настроенные исследователи предлагают рассмотреть методы геоинженерии как 'план Б', хотя и признают их потенциальные риски.
Межправительственная группа экспертов по изменению климата (IPCC) в своём последнем отчёте обозначила чёткие цели: сокращение выбросов на 45% к 2030 году и достижение углеродной нейтральности к 2050 году. Это требует немедленных и скоординированных действий всех стран. Учёные подчёркивают: хотя ситуация серьёзна, у человечества ещё есть шанс избежать наихудших сценариев, но для этого необходимы беспрецедентные политические решения и изменение потребительских моделей поведения в глобальном масштабе.""", reply_markup=markup)

@bot.message_handler(commands=['What_can_you_do'])
def WCYD(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Что ты можешь сделать, чтобы замедлить глобальное потеплениеБ если ты обычный школьник/студент/гражданин:
/SCW1
/SCW2
/SCW3
/SCW4
/SCW5
/SCW6""", reply_markup=markup) 

@bot.message_handler(commands=['SCW1'])
def SCW1(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Даже если ты школьник, студент или обычный работяга — твои действия реально влияют на экологию. Вот конкретные шаги, которые помогут снизить углеродный след и внести вклад в борьбу с климатическим кризисом:
  экономи ресурсы (это бесплатно!)
🔹 Электричество → выключай свет, зарядки из розетки, используй LED-лампы.
🔹 Вода → короче душ, закрывай кран при чистке зубов.
🔹 Отопление → утепляй окна, не открывай балкон 'проветрить' зимой.""", reply_markup=markup)

@bot.message_handler(commands=['SCW2'])
def SCW2(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Меньше мусора = меньше выбросов
🔸 Откажись от одноразового пластика (бутылки, пакеты, стаканчики)
🔸 Сортируй мусор (хотя бы бумагу/пластик/батарейки).
🔸 Покупай разумно → не бери лишнего, используй вещи дольше.""", reply_markup=markup)

@bot.message_handler(commands=['SCW3'])
def SCW3(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Транспорт: двигайся 'зелёно'
🚶 Пешком/на велике → для здоровья + 0 выбросов.
🚌 Общественный транспорт → лучше, чем такси/личная машина.
🚗 Если авто неизбежно → карпулинг (подвози друзей).""", reply_markup=markup)

@bot.message_handler(commands=['SCW4'])
def SCW4(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Еда: как выбор еды влияет на климат?
🍔 Реже мясо (особенно говядину) → животноводство = 15% всех выбросов.
🍎 Локальные продукты → яблоки из сада рядом > авокадо из Мексики.
🗑 Не выбрасывай еду → гниение на свалке = метан (сильный парниковый газ).""", reply_markup=markup)

@bot.message_handler(commands=['SCW5'])
def SCW5(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Распространяй знания и влияй на других
📢 Говори о проблеме → в соцсетях, среди друзей, семьи.
📝 Подпиши петиции → за 'зелёные' законы в своём городе/стране.
👥 Вступай в эко-движения → даже маленькие акции (уборки, посадки деревьев) имеют значение.""", reply_markup=markup)

@bot.message_handler(commands=['SCW6'])
def SCW6(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Давление на бизнес и власти
💼 Выбирай 'зелёные' компании → поддерживай тех, кто снижает выбросы.
🗳 Голосуй за политиков с климатической программой.
📢 Требуй изменений → например, углеродной нейтральности в своём вузе/офисе.""", reply_markup=markup)

@bot.message_handler(commands=['FSA'])
def FSA(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Фильмы, сериалы и аниме связанные с глобальным потеплением:
/Movies
/Series
/Animes""", reply_markup=markup)

@bot.message_handler(commands=['Movies'])
def FSA(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """«Послезвтра»
«Геошторм»
«Сквозь снег»""", reply_markup=markup)

@bot.message_handler(commands=['Series'])
def Ser(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """«Годы и годы»
«100»
«Сквозь снег»""", reply_markup=markup)

@bot.message_handler(commands=['Animes'])
def Ani(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """«Tengoku Daimakyou»
  «Mushishi»
  «Somali and the Forest Spirit»""", reply_markup=markup)

@bot.message_handler(commands=['Facts'])
def facts(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Интересные факты про глобальное потепление
/F1
/F2
/F3
/F4
/F5
/F6""", reply_markup=markup) 

@bot.message_handler(commands=['F1'])
def F1(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Океан стал кислым 🍋
Из-за поглощения CO₂ кислотность океана выросла на 30% с XIX века. Это убивает кораллы и планктон — основу морской пищевой цепочки.""", reply_markup=markup) 

@bot.message_handler(commands=['F2'])
def F2(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Вечная мерзлота — бомба замедленного действия 💣
В сибирской и канадской мерзлоте заперты 1,5 триллиона тонн метана (в 25 раз мощнее CO₂). Если растает — катастрофа ускорится.""", reply_markup=markup) 

@bot.message_handler(commands=['F3'])
def F3(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Ледники тают быстрее, чем думали ❄️
Гренландия теряет 260 млрд тонн льда в год (это как 104 млн олимпийских бассейнов!).""", reply_markup=markup) 

@bot.message_handler(commands=['F4'])
def F4(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Жара делает нас глупее 🧠
При +26°C когнитивные способности падают на 10%, а при +32°C — на 30%.""", reply_markup=markup) 

@bot.message_handler(commands=['F5'])
def F5(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Вино и кофе под угрозой 🍷☕
К 2050 году из-за жары и засух:
Площади для кофе сократятся на 50%.
Виноградники исчезнут в Италии, Испании и Франции.""", reply_markup=markup) 

@bot.message_handler(commands=['F6'])
def F6(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """В Арктике идёт «кровавый дождь» 🩸
Ледники иногда становятся красными из-за водорослей Chlamydomonas nivalis — они ускоряют таяние.""", reply_markup=markup) 

@bot.message_handler(commands=['Begining'])
def begining(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """Глобальное потепление — это долгий процесс, который ускорился из-за деятельности человека за последние 150 лет.""", reply_markup=markup) 

@bot.message_handler(commands=['Reasons_to_watch_Oshi_no_KO'])
def Oshi_no_KO(message):
  markup = types.ReplyKeyboardMarkup()
  bot.send_message(message.chat.id, """1) Это лучшее аниме 2022 года
2) Там есть Кана 
3) Да 
4) Смотри пункт №3""", reply_markup=markup) 

@bot.message_handler(commands=['photos'])
def send_photo(message):
    images = os.listdir('images')
    if images:
        image = random.choice(images)
        with open(f'images/{image}', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    else:
        bot.reply_to(message, "В папке нет фотографий!")

@bot.message_handler(commands=['news'])
def send_news(message):
    try:
        html = requests.get('https://iz.ru/tag/globalnoe-poteplenie').text
        soup = BeautifulSoup(html, 'html.parser')
        
        news = []
        for item in soup.find_all('h3', class_='gs-c-promo-heading__title')[:5]:
            title = item.text.strip()
            link = item.find_parent('a')['href']
            if not link.startswith('http'):
                link = 'https://iz.ru' + link
            news.append(f"• <a href='{link}'>{title}</a>")
        
        bot.send_message(message.chat.id, "\n\n".join(news), parse_mode='HTML')
    
    except:
        bot.send_message(message.chat.id, "Не получилось загрузить новости")

bot.infinity_polling()
