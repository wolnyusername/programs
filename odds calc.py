from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


def get_fortuna():
    forbiden_text_names = ["-", "TVP 1", "Rozszerzona", "oferta", "LIVE", "BetBuilder", "Zagraj", "HIT", "DNIA", "TVP 2"
        , "Sport/", "/", "ZAGRAJ", "TVP", "1", "Sport", "wyższy", "kurs", "2", "Mecz", "Płd.", "S.", "finału", "1/8"
        , "1/4", "CF"]
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    fortuna = webdriver.Chrome(PATH)
    fortuna.get("https://www.efortuna.pl/zaklady-bukmacherskie/pilka-nozna-ms-2022/spotkania")
    downloaded_content = fortuna.find_elements(By.CSS_SELECTOR, 'tr.tablesorter-hasChildRow')
    data_to_clear = []
    for i in downloaded_content:
        for j in i.text.split():
            if j not in forbiden_text_names:
                data_to_clear.append(j)
    host = data_to_clear[:len(data_to_clear) - 10:11]
    guest = data_to_clear[1:len(data_to_clear) - 9:11]
    host_win_odds = data_to_clear[2:len(data_to_clear) - 8:11]
    draw = data_to_clear[3:len(data_to_clear) - 7:11]
    guest_win_odds = data_to_clear[4:len(data_to_clear) - 6:11]
    match_names = []
    for i in range(len(host)):
        mecz = f"{host[i]} vs {guest[i]}"
        match_names.append(mecz)
    match_names_series = pd.Series(match_names, name="match name")
    host_win_odds_series = pd.Series(host_win_odds, name="host odds", dtype=float)
    draw_series = pd.Series(draw, name="draw odds", dtype=float)
    guest_win_odds_series = pd.Series(guest_win_odds, name="guest odds", dtype=float)
    fortuna_odds = pd.DataFrame(data=match_names_series)
    fortuna_odds.insert(1, "host win odds", host_win_odds_series)
    fortuna_odds.insert(2, "draw odds", draw_series)
    fortuna_odds.insert(3, "guest win odds", guest_win_odds_series)
    fortuna_odds.insert(4, "bookmaker", "fortuna")
    return fortuna_odds


def get_super_bet():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    super_bet = webdriver.Chrome(PATH)
    super_bet.get("https://superbet.pl/zaklady-bukmacherskie/pilka-nozna/miedzynarodowe/mistrzostwa-swiata")
    downloaded_content = super_bet.find_elements(By.CLASS_NAME, "event-row-container")
    forbiden_words = ["w", "WT.", "ŚR.", "CZW.", "PT.", "1", "X", "2", "Płd.", "S.", "SOB.", "NIEDZ.", "Oferta",
                      "specjalna", "dla", "nowych", "graczy", "online!", "Bonus", "za", "program", "typ", "na", "gola",
                      "Polski", "meczu", "300", "PLN", "poprawny", "z", "Francją.", "Szczegóły", "i", "wygraną",
                      "otrzymasz", "-", "Postaw", "zakład", "oferty", "przedmeczowej,", "a", "jeśli", "trafisz",
                      "otrzymasz", "bonus.", "sekcji", "„Promocje”", "PON.", "1/8", "finału."]
    data_to_clear = []
    for i in downloaded_content:
        for j in i.text.split():
            if j not in forbiden_words:
                data_to_clear.append(j)
    host_name = []
    for i in range(1, len(data_to_clear), 11):
        host_name.append(data_to_clear[i])

    guest_name = []
    for i in range(2, len(data_to_clear), 11):
        guest_name.append(data_to_clear[i])

    host_win_odds = []
    for i in range(4, len(data_to_clear), 11):
        host_win_odds.append(data_to_clear[i])

    draw_odds = []
    for i in range(6, len(data_to_clear), 11):
        draw_odds.append(data_to_clear[i])

    guest_win_odds = []
    for i in range(8, len(data_to_clear), 11):
        guest_win_odds.append(data_to_clear[i])

    event = []
    for i in range(len(host_name)):
        event.append(f"{host_name[i]} vs {guest_name[i]}")

    event_series = pd.Series(data=event, name="match name")
    host_win_odds_series = pd.Series(data=host_win_odds, name="host odds", dtype=float)
    draw_odds_series = pd.Series(data=draw_odds, name="draw odds", dtype=float)
    guest_win_odds_series = pd.Series(data=guest_win_odds, name="guest odds", dtype=float)
    super_bets_odds = pd.DataFrame(data=event_series)
    super_bets_odds.insert(1, "host win odds", host_win_odds_series)
    super_bets_odds.insert(2, "draw odds", draw_odds_series)
    super_bets_odds.insert(3, "guest win odds", guest_win_odds_series)
    super_bets_odds.insert(4, "bookmaker", "super bet")
    return super_bets_odds


def get_fuksiarz():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    fuksiarz = webdriver.Chrome(PATH)
    fuksiarz.get("https://fuksiarz.pl/zaklady-bukmacherskie/pilka-nozna/miedzynarodowe/mistrzostwa-swiata/174616/1")
    downloaded_teams_names = fuksiarz.find_elements(By.CLASS_NAME, "event")
    odds_downloaded = fuksiarz.find_elements(By.CLASS_NAME, "game")
    forbiden_words = ["Saudyjska", "Płd.", "-"]
    names_to_clean = []
    for i in downloaded_teams_names:
        for j in i.text.split():
            if j not in forbiden_words:
                names_to_clean.append(j)

    host_names = []
    for i in range(2, len(names_to_clean), 4):
        host_names.append(names_to_clean[i])

    guest_names = []
    for i in range(3, len(names_to_clean), 4):
        guest_names.append(names_to_clean[i])

    event = []
    for i in range(len(host_names)):
        event.append(f"{host_names[i]} vs {guest_names[i]}")

    odds = []
    for i in odds_downloaded:
        if i.text.split():
            odds.append(i.text.split())

    host_win_odds = []
    draw_odds = []
    guest_win_odds = []
    for i in odds:
        for j in range(3):
            if j == 0:
                host_win_odds.append(i[j])
            elif j == 1:
                draw_odds.append(i[j])
            elif j == 2:
                guest_win_odds.append((i[j]))

    event_series = pd.Series(data=event, name="match name")
    host_win_odds_series = pd.Series(data=host_win_odds, name="host win odds", dtype=float)
    draw_odds_series = pd.Series(data=draw_odds, name="draw odds", dtype=float)
    guest_win_odds_series = pd.Series(data=guest_win_odds, name="guest win odds", dtype=float)
    fuksiarz_odds = pd.DataFrame(data=event_series)
    fuksiarz_odds.insert(1, "host win odds", host_win_odds_series)
    fuksiarz_odds.insert(2, "draw odds", draw_odds_series)
    fuksiarz_odds.insert(3, "guest win odds", guest_win_odds_series)
    fuksiarz_odds.insert(4, "bookmaker", "fuksiarz")
    return fuksiarz_odds


def save_odds():
    combine = pd.concat([get_super_bet(), get_fuksiarz(), get_fortuna()])
    combine.to_excel('test.xlsx')
    return combine


def load_odds():
    combine = pd.read_excel('test.xlsx')
    return combine


def arb_odds():
    df = pd.concat([get_super_bet(), get_fuksiarz(), get_fortuna()])
    df = df.groupby(['match name'])
    arb_value = []
    arbit_odd = []
    for i, j in df:
        for win_odd in j['host win odds']:
            for draw_odd in j['draw odds']:
                for guest_odd in j['guest win odds']:
                    wynik = round((1/win_odd)+(1/draw_odd)+(1/guest_odd), 2)
                    arbit_odd.append((win_odd, draw_odd, guest_odd))
                    arb_value.append(wynik)
    arbit_name = []
    for i, j in df:
        for win_buk in j['bookmaker']:
            for draw_buk in j['bookmaker']:
                for guest_buk in j['bookmaker']:
                    buk_comb = [win_buk, draw_buk, guest_buk, i]
                    arbit_name.append(buk_comb)
    events = []
    if len(arb_value) == len(arbit_odd) == len(arbit_name):
        for i in range(len(arb_value)):
            events.append([arb_value[i], arbit_odd[i], arbit_name[i]])
    else:
        print("cos poszlo nie tak z obrobka danych")
    for i in events:
        #if i[0] < 0.85:
            print(i)
            print(f"host bet {round(((100 / i[1][0]) / i[0]), 2)}")
            print(f"draw bet {round(((100 / i[1][1]) / i[0]), 2)}")
            print(f"guest bet {round(((100 / i[1][2]) / i[0]), 2)}")


arb_odds()
