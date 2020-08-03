import telebot
import requests
from bs4 import BeautifulSoup



bot = telebot.TeleBot('1393329859:AAEUX-OCUMru9H-W1tSelxpfWNRq3kOKmXY')

DOLLAR_RUB_RSK_BANK = 'http://www.rsk.kg/'
DOLLAR_RUB_OPTIMA_BANK = 'https://www.optimabank.kg/'
DOLLAR_RUB_CAPITAL_BANK = 'https://www.capitalbank.kg/'
DOLLAR_RUB_FINCA_BANK = 'https://www.fincabank.kg/'
DOLLAR_RUB_HALYK_BANK = 'http://www.halykbank.kg/ru/'
DOLLAR_RUB_DEMIR_BANK = 'https://www.demirbank.kg/ru-ru'
DOLLAR_RUB_AMAN_BANK = 'http://www.amanbank.kg/'
DOLLAR_RUB_AYIL_BANK = 'https://ab.kg/'
DOLLAR_RUB_BAKAI_BANK = 'https://bakai.kg/ru/'
DOLLAR_RUB_TOLUBAI_BANK = 'https://www.tolubaybank.kg/'
DOLLAR_RUB_AZII_BANK = 'https://www.bankasia.kg/'
DOLLAR_RUB_BAI_TUSHUM_BANK = 'https://www.baitushum.kg/ru/'
DOLLAR_RUB_DOSKREDOBANK_BANK = 'https://www.dcb.kg/ru/'
DOLLAR_RUB_NATCH_BANK_PAKISTANA = 'http://nbp.kg/?lang=ru'
DOLLAR_RUB_CHANGANG_BANK = 'https://changan.kg/'
DOLLAR_RUB_KOMMERCIAL_BANK = 'https://www.cbk.kg/'

DOLLAR_RUB_FINANC_BANK = 'http://www.fkb.kg/'
DOLLAR_RUB_KYRGYZKOMMECH_BANK = 'https://kkb.kg/ru/'
DOLLAR_RUB_KICB_BANK = 'https://kicb.net/welcome/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}





optima = requests.get(DOLLAR_RUB_OPTIMA_BANK, headers=headers)
soup2 = BeautifulSoup(optima.content, 'html.parser')
convert2 = soup2.findAll("span", {"class": "zero"})


rsk = requests.get(DOLLAR_RUB_RSK_BANK, headers=headers)
soup1 = BeautifulSoup(rsk.content, 'html.parser')
convert1 = soup1.findAll("div", {"class": "price"})


capital = requests.get(DOLLAR_RUB_CAPITAL_BANK, headers=headers)
soup3 = BeautifulSoup(capital.content, 'html.parser')
convert3 = soup3.findAll("td")


FINCA = requests.get(DOLLAR_RUB_FINCA_BANK, headers=headers)
soup4 = BeautifulSoup(FINCA.content, 'html.parser')
convert4 = soup4.findAll("td")


HALYK = requests.get(DOLLAR_RUB_HALYK_BANK, headers=headers)
soup5 = BeautifulSoup(HALYK.content, 'html.parser')
convert5 = soup5.findAll("span")


DEMIR = requests.get(DOLLAR_RUB_DEMIR_BANK, headers=headers)
soup6 = BeautifulSoup(DEMIR.content, 'html.parser')
convert6 = soup6.findAll("td")


AMAN = requests.get(DOLLAR_RUB_AMAN_BANK, headers=headers)
soup7 = BeautifulSoup(AMAN.content, 'html.parser')
convert7 = soup7.findAll("strong")





@bot.message_handler(commands=['start'])
def start(message):


    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\n"\
          f"Курс  $ в Кыргызстане\n" \
          f"_______________________________________\n"\
          f"   Банки" + "   Покупка   " + "Продажа\n"\
          +"РСК БАНК    "+convert1[0].text+"   |   "+convert1[1].text+"\n"\
          +"Оптима Банк "+convert2[0].text+" | "+convert2[1].text+"\n"\
          +"Капитал Банк "+convert3[6].text+" "+" | "+convert3[8].text+"\n"\
          +"Финка Банк  "+convert4[2].text+" | "+convert4[3].text+"\n"\
          +"Халык Банк "+convert5[20].text+"    | "+convert5[21].text+"\n"\
          +"Демир Банк "+convert6[5].text+"     | "+convert6[6].text+"\n"\
          +"Аман Банк "+convert7[4].text+" | "+convert7[5].text\

    bot.send_message(message.chat.id, send_mess, parse_mode='html')







bot.polling(none_stop=True)