import requests

# URL для API НБУ
url = "https://bank.gov.ua/NBU_Exchange/exchange_site"

# Параметри запиту
params = {
    'start': '20251031',
    'end': '20251031',
    'valcode': 'usd',
    'sort': 'exchangedate',
    'order': 'desc',
    'json': ''
}

# Виконуємо GET запит
response = requests.get(url, params=params)

# Отримуємо дані у форматі JSON
data = response.json()

# Виводимо заголовок результату
print("=" * 60)
print("КУРС ДОЛАРА США НА 31.10.2025")
print("=" * 60)
print()

# Виводимо дані першого елемента
if len(data) > 0:
    currency = data[0]
    print(f"Дата:         {currency['exchangedate']}")
    print(f"Назва валюти: {currency['txt']}")
    print(f"Код валюти:   {currency['cc']}")
    print(f"Курс:         {currency['rate']:.4f} грн")

print()
print("=" * 60)
