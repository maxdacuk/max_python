import requests
import time

# Функція для отримання курсу валюти з exchangeratesapi.io
def get_rates_from_exchangeratesapi() -> dict:
    url = "https://api.exchangeratesapi.io/v1/latest"
    params = {
        "access_key": "f59e04f1ff90e13b149883737a4dfd25",
        "symbols": "USD,GBP,CAD"  # Лише потрібні курси
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Перевірка на статус код
        data = response.json()
        if 'rates' in data and 'USD' in data['rates']:
            rates = data['rates']
            usd_to_gbp = rates['GBP'] / rates['USD']
            usd_to_cad = rates['CAD'] / rates['USD']
            usd_to_eur = 1 / rates['USD']
            return {
                "EUR": usd_to_eur,
                "GBP": usd_to_gbp,
                "CAD": usd_to_cad
            }
        else:
            print("Курси відсутні у відповіді exchangeratesapi.io")
            return None
    except requests.RequestException as e:
        print("Помилка при отриманні даних з exchangeratesapi.io:", e)
        return None

# Функція для отримання курсу валюти з anyapi.io
def get_rates_from_anyapi() -> dict:
    url = "https://anyapi.io/api/v1/exchange/convert"
    base_currency = "USD"
    target_currencies = ["EUR", "GBP", "CAD"]
    api_key = "474ftmck808ugai0fjd3b8v5m70mb3h388kcmh460fjg02u6iucibso"
    
    rates = {}
    
    for currency in target_currencies:
        params = {
            "base": base_currency,
            "to": currency,
            "amount": 1,
            "apiKey": api_key
        }
        try:
            response = requests.get(url, params=params, timeout=5)
            
            # Перевіряємо статус код
            response.raise_for_status()
            
            # Парсимо JSON відповідь
            data = response.json()
            
            # Перевіряємо, чи є 'rate' у відповіді
            if 'rate' in data:
                rates[currency] = data['rate']
        
        except requests.HTTPError:
            print(f"Помилка при отриманні курсу для {currency}. Можливо, перевищено ліміт запитів або неправильний запит.")
        except requests.RequestException:
            print(f"Інша помилка при отриманні курсу для {currency}.")
        
        # Додаємо затримку перед наступним запитом, щоб уникнути помилки 429
        time.sleep(2)
    
    return rates

# Функція для порівняння курсів з двох сервісів
def compare_rates():
    rates_exchangeratesapi = get_rates_from_exchangeratesapi()
    rates_anyapi = get_rates_from_anyapi()
    
    if not rates_exchangeratesapi:
        print("\nДані не надійшли з exchangeratesapi.io")
    if not rates_anyapi:
        print("\nДані не надійшли з anyapi.io")
    
    if rates_exchangeratesapi and rates_anyapi:
        print("\nПорівняння курсів валют (USD):")
        
        # Порівнюємо курси
        for currency in ["EUR", "GBP", "CAD"]:
            rate_ex = rates_exchangeratesapi.get(currency)
            rate_any = rates_anyapi.get(currency)
            print(f"{currency}: exchangeratesapi.io = {rate_ex}, anyapi.io = {rate_any}")
            
            if rate_ex is not None and rate_any is not None:
                diff = abs(rate_ex - rate_any)
                print(f"Різниця для {currency}: {diff:.4f}")
            else:
                print(f"Неможливо отримати курс для {currency}")
    else:
        print("\nПомилка при отриманні даних із одного або обох сервісів.")

# Виклик функції порівняння
compare_rates()