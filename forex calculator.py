from selenium import webdriver
from selenium.webdriver.common.by import By


PATH = "C:\Program Files (x86)\chromedriver.exe"
forex = webdriver.Chrome(PATH)
forex.get("https://www.investing.com/currencies/streaming-forex-rates-majors")
EUR_USD_bid = float(forex.find_element(By.CLASS_NAME, "pid-1-bid").text)
EUR_USD_ask = float(forex.find_element(By.CLASS_NAME, "pid-1-ask").text)
USD_JPY_bid = float(forex.find_element(By.CLASS_NAME, "pid-3-bid").text)
USD_JPY_ask = float(forex.find_element(By.CLASS_NAME, "pid-3-ask").text)
GBP_USD_bid = float(forex.find_element(By.CLASS_NAME, "pid-2-bid").text)
GBP_USD_ask = float(forex.find_element(By.CLASS_NAME, "pid-2-ask").text)
USD_CHF_bid = float(forex.find_element(By.CLASS_NAME, "pid-4-bid").text)
USD_CHF_ask = float(forex.find_element(By.CLASS_NAME, "pid-4-ask").text)
USD_CAD_bid = float(forex.find_element(By.CLASS_NAME, "pid-7-bid").text)
USD_CAD_ask = float(forex.find_element(By.CLASS_NAME, "pid-7-ask").text)
AUD_USD_bid = float(forex.find_element(By.CLASS_NAME, "pid-5-bid").text)
AUD_USD_ask = float(forex.find_element(By.CLASS_NAME, "pid-5-ask").text)
NZD_USD_bid = float(forex.find_element(By.CLASS_NAME, "pid-8-bid").text)
NZD_USD_ask = float(forex.find_element(By.CLASS_NAME, "pid-8-ask").text)
forex.quit()


def print_rates():
    print(f"pair buy sell")
    print(f"EUR/USD {EUR_USD_bid} {EUR_USD_ask}")
    print(f"USD/JPY {USD_JPY_bid} {USD_JPY_ask}")
    print(f"GBP/USD {GBP_USD_bid} {GBP_USD_ask}")
    print(f"USD/CHF {USD_CHF_bid} {USD_CHF_ask}")
    print(f"USD/CAD {USD_CAD_bid} {USD_CAD_ask}")
    print(f"AUD/USD {AUD_USD_bid} {AUD_USD_ask}")
    print(f"NZD/USD {NZD_USD_bid} {NZD_USD_ask}")


def count_bid():
    pairs = ["EUR/USD", "USD/JPY", "GBP/USD", "USD/CHF", "USD/CAD", "AUD/USD", "NZD/USD"]
    print(pairs)
    pair = input("On which pair would you like to bet")
    pair = pair.upper()
    if pair not in pairs:
        print("provide one of six currency pair")
        count_bid()
    bets = ["B", "S"]
    typ_of_bet = input("Write 'b' if you want to buy, 's' if you want to sell ")
    typ_of_bet = typ_of_bet.upper()
    if typ_of_bet not in bets:
        print("provide valid transaction option")
        count_bid()
    value = float(input("Amount of money you want to bet in lots (1 lot = 100 000 units of base currency), grater then 0"))
    if value < 0:
        print("please give value greater then 0")
        count_bid()
    stop_loss = float(input("How many points from starting price would you like to set your stop lose, grater then 0"))
    if stop_loss < 0:
        print("please give value greater then 0")
        count_bid()
    take_profit = float(input("How many points from starting price would you like to set your take profit, grater then 0"))
    if take_profit < 0:
        print("please give value greater then 0")
        count_bid()
    value = value * 100000
    match pair:
        case "EUR/USD":
            match typ_of_bet:
                case "B":
                    stop_loss_value = round(EUR_USD_bid - (stop_loss / 10000), 4)
                    take_profit_value = round(EUR_USD_ask + (take_profit / 10000), 4)
                    expected_win = round(take_profit_value * value - value * EUR_USD_bid, 2)
                    expected_loss = round(stop_loss_value * value - EUR_USD_ask * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
                case "S":
                    stop_loss_value = round(EUR_USD_ask + (stop_loss / 10000), 4)
                    take_profit_value = round(EUR_USD_bid - (take_profit / 10000), 4)
                    expected_win = round(EUR_USD_bid * value - take_profit_value * value, 2)
                    expected_loss = round(EUR_USD_ask * value - stop_loss_value * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
        case "USD/JPY":
            match typ_of_bet:
                case "B":
                    stop_loss_value = round(USD_JPY_bid - (stop_loss / 100), 2)
                    take_profit_value = round(USD_JPY_ask + (take_profit / 100), 2)
                    expected_win = round((take_profit_value * value - value * USD_JPY_bid) / 100, 2)
                    expected_loss = round((stop_loss_value * value - USD_JPY_ask * value) / 100, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
                case "S":
                    stop_loss_value = round(EUR_USD_ask + (stop_loss / 100), 2)
                    take_profit_value = round(EUR_USD_bid - (take_profit / 100), 2)
                    expected_win = round((EUR_USD_bid * value - take_profit_value * value) / 100, 2)
                    expected_loss = round((EUR_USD_ask * value - stop_loss_value * value) / 100, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
        case "GBP/USD":
            match typ_of_bet:
                case "B":
                    stop_loss_value = round(GBP_USD_bid - (stop_loss / 10000), 4)
                    take_profit_value = round(GBP_USD_ask + (take_profit / 10000), 4)
                    expected_win = round(take_profit_value * value - value * GBP_USD_bid, 2)
                    expected_loss = round(stop_loss_value * value - GBP_USD_ask * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
                case "S":
                    stop_loss_value = round(GBP_USD_ask + (stop_loss / 10000), 4)
                    take_profit_value = round(GBP_USD_bid - (take_profit / 10000), 4)
                    expected_win = round(GBP_USD_bid * value - take_profit_value * value, 2)
                    expected_loss = round(GBP_USD_ask * value - stop_loss_value * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
        case "USD/CHF":
            match typ_of_bet:
                case "B":
                    stop_loss_value = round(USD_CHF_bid - (stop_loss / 10000), 4)
                    take_profit_value = round(USD_CHF_ask + (take_profit / 10000), 4)
                    expected_win = round(take_profit_value * value - value * USD_CHF_bid, 2)
                    expected_loss = round(stop_loss_value * value - USD_CHF_ask * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
                case "S":
                    stop_loss_value = round(USD_CHF_ask + (stop_loss / 10000), 4)
                    take_profit_value = round(USD_CHF_bid - (take_profit / 10000), 4)
                    expected_win = round(USD_CHF_bid * value - take_profit_value * value, 2)
                    expected_loss = round(USD_CHF_ask * value - stop_loss_value * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
        case "AUD/USD":
            match typ_of_bet:
                case "B":
                    stop_loss_value = round(AUD_USD_bid - (stop_loss / 10000), 4)
                    take_profit_value = round(AUD_USD_ask + (take_profit / 10000), 4)
                    expected_win = round(take_profit_value * value - value * AUD_USD_bid, 2)
                    expected_loss = round(stop_loss_value * value - AUD_USD_ask * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
                case "S":
                    stop_loss_value = round(AUD_USD_ask + (stop_loss / 10000), 4)
                    take_profit_value = round(AUD_USD_bid - (take_profit / 10000), 4)
                    expected_win = round(AUD_USD_bid * value - take_profit_value * value, 2)
                    expected_loss = round(AUD_USD_ask * value - stop_loss_value * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
        case "NZD/USD":
            match typ_of_bet:
                case "B":
                    stop_loss_value = round(NZD_USD_bid - (stop_loss / 10000), 4)
                    take_profit_value = round(NZD_USD_ask + (take_profit / 10000), 4)
                    expected_win = round(take_profit_value * value - value * NZD_USD_bid, 2)
                    expected_loss = round(stop_loss_value * value - NZD_USD_ask * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
                case "S":
                    stop_loss_value = round(NZD_USD_ask + (stop_loss / 10000), 4)
                    take_profit_value = round(NZD_USD_bid - (take_profit / 10000), 4)
                    expected_win = round(NZD_USD_bid * value - take_profit_value * value, 2)
                    expected_loss = round(NZD_USD_ask * value - stop_loss_value * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
        case "USD/CAD":
            match typ_of_bet:
                case "B":
                    stop_loss_value = round(USD_CAD_bid - (stop_loss / 10000), 4)
                    take_profit_value = round(USD_CAD_ask + (take_profit / 10000), 4)
                    expected_win = round(take_profit_value * value - value * USD_CAD_bid, 2)
                    expected_loss = round(stop_loss_value * value - USD_CAD_ask * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)
                case "S":
                    stop_loss_value = round(USD_CAD_ask + (stop_loss / 10000), 4)
                    take_profit_value = round(USD_CAD_bid - (take_profit / 10000), 4)
                    expected_win = round(USD_CAD_bid * value - take_profit_value * value, 2)
                    expected_loss = round(USD_CAD_ask * value - stop_loss_value * value, 2)
                    print(stop_loss_value, take_profit_value, expected_win, expected_loss)


while True:
    print("possible options: print rate, count bid, quit")
    decision = input("What operation would you like to perform")
    match decision:
        case "print rate":
            print_rates()
        case "count bid":
            count_bid()
        case "quit":
            quit()