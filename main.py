from datetime import datetime
import os
import requests
import json

API_KEY = 'xcbDQ9fSwl2Z9OkMwe44Yx5CUCdBd5qB'
CURRENCY_RATES_FILE = 'currency_rates.json'
# API_KEY = os.getenv('RATE_API_KEY')

def main():
    while True:
        currency = input("Введите название валюты (USD или EUR): ")
        if currency not in ("USD", "EUR"):
            print("Некорректный ввод")
            continue
        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f'Курс {currency} к рублю: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Выберите действие: (1 - продолжить, 2 - выйти) ')
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print('Некорректный ввод')


def get_currency_rate(base: str) -> float:
    """Получает курс от API и возвращает его в виде float"""
    url = "https://api.apilayer.com/exchangerates_data/latest"

    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data: dict) -> None:
    """Сохраняет данные в json файл."""
    with open(CURRENCY_RATES_FILE, 'a') as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATES_FILE) as f:
                data_list = json.load(f)
                data_list.append(data)
            with open(CURRENCY_RATES_FILE, 'w') as f:
                json.dump(data_list, f)


if __name__ == "__main__":
    main()
