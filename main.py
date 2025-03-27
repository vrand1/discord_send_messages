import sys
import time
import requests
import datetime
def convert_seconds(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')

def find_latest_entry(data, name):
    latest_key = None
    latest_date = None

    for key in data:
        date, entry_name = key
        if entry_name == name:
            if latest_date is None or date > latest_date:
                latest_date = date
                latest_key = key

    if latest_key:
        return latest_key[0]
    else:
        return None

def CheckTime(servername):
    with open("logs\logs.txt", "r") as file:
        lines = file.readlines()
    with open("logs\Servers_TimerCooldown.txt", "r") as file:
        lines_servers = file.readlines()
    date_dict = {}
    servers_TCD = {}

    for line in lines:

        parts = line.strip().split('&&&')

        if len(parts) == 3:
            date, name, value = parts
            date = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
            key = (date, name)
            date_dict[key] = value
    for line in lines_servers:
        parts = line.strip().split('-')
        if len(parts) == 2:
            name, value = parts
            value = int(value)
            value = datetime.timedelta(seconds=value)
            key = name
            servers_TCD[key] = value
    DateNow = datetime.datetime.now()
    try:
        DateTCD = DateNow - find_latest_entry(date_dict, servername)

        DateTCD = servers_TCD[servername] - DateTCD
    except:
        return "[Недостаточно данных, нужно одно успешное срабатывание скрипта]"
    return (str(DateTCD)[0:7])


def Info(date, servername):
    with open("logs\logs.txt", "a") as file:
        file.write(f"{date}&&&{servername}&&&Успех\n")

def SendMessage(url, key, servername):
    payload = {
       "content": "# :frog:  Мы - компания **T E A P A R T Y** ждем именно тебя!  :frog:\n***Мы в поисках игроков желающих лутать PvP контент в формате СС (до 20и ppl)!***\n***Приходи сам и зови друзей, пришло время самим создавать историю Альбиона!***\n\n      **:cactus:  У нас в Гильдии тебя ждёт: :cactus: **\n\n> *:green_book: Онлайн 14-20 UTC;*\n> *:green_book: Ежедневный контент (Статики, Авалоны, Small-Scale и многое другое);*\n> *:green_book: Быстрая прокачка;*\n> *:green_book: Сильный состав;*\n> *:green_book: Разбор игровых моментов (Поможем правильно прожимать кнопки, расскажем о позициях и не дадим тебе умереть во время файта).*\n\n       **:crossed_swords:  От тебя требуется: :crossed_swords: **\n\n> *:tea: Дискорд для коммуникации, а так же дружелюбное отношение;*\n> *:tea: Актив и желание развиваться в PvP направлении;*\n> *:tea: По возможности записывать видео (Не обязательно);*\n> *:tea: 5КК PvP фейма на европе или 10КК на других серверах (возможны исключения).*\n\n**Играем от города Fort Sterling :four_leaf_clover:  **\nhttps://discord.gg/6YpwvtjbTa\n**Так же мы: https://www.youtube.com/watch?v=U87Qs548kRY**\n"
    }
    headers = {
        "Authorization": key
    }
    date = datetime.datetime.now()
    date =str(date.strftime('%Y-%m-%d %H:%M:%S'))
    r = requests.post("https://discord.com/api/v9/channels/"+str(url)+"/messages", payload, headers=headers)
    if (r.status_code == 200):
        print(date + " — Операция на сервере " + servername + " проведена успешно")
        Info(date, servername)
    elif (r.status_code == 401):
        print(date + " — Неверный токен, перепроверьте его правильность ещё раз.")
    elif (r.status_code == 429):
        try:
            time = CheckTime(servername)
        except:
            time = "[Недостаточно данных, нужно одно успешное срабатывание скрипта]"

        print(date+ " — Вы уже отправляли сообщение в канал " +servername +", подождите ещё "+time)





Key = sys.argv[1]

# Пример использования, ID канала, и как будет называться сервер)
SendMessage(838102290593349654, Key, "Crafting Tavern")
SendMessage(1234603706490556548, Key, "The Crossroad")
SendMessage(704733930103767090, Key, "Arreat Regaro")
SendMessage(1026898164831232090, Key, "tv.atrophos")
SendMessage(982002649312403556, Key, "KDA")
SendMessage(1245274698833596416, Key, "RuTT")
SendMessage(1091295250624041112, Key, "Albion Trade Hall")
SendMessage(894848414121086997, Key, "The Dno")
SendMessage(1242490337763524630, Key, "Albion Market")


