import requests
import matplotlib.pyplot as plt

# URL для API НБУ
url = "https://bank.gov.ua/NBU_Exchange/exchange_site"

# Параметри запиту для отримання даних за тиждень
params = {
    'start': '20251027',
    'end': '20251102',
    'valcode': 'usd',
    'sort': 'exchangedate',
    'order': 'asc',
    'json': ''
}

# Виконуємо запит до API
print("Завантаження даних...")
response = requests.get(url, params=params)

# Отримуємо дані у форматі JSON
data = response.json()

# Створюємо списки для дат та курсів
dates = []
rates = []

# Заповнюємо списки даними
for item in data:
    dates.append(item['exchangedate'])
    rates.append(item['rate'])

# Виводимо статистику
print(f"Завантажено {len(dates)} записів")
print("Побудова графіка...")

# Створюємо фігуру графіка
plt.figure(figsize=(12, 6))

# Будуємо лінійний графік
plt.plot(dates, rates, linewidth=2, color='blue')

# Налаштовуємо заголовок та підписи
plt.title('Курс Долар США', fontsize=14)
plt.xlabel('Дата', fontsize=11)
plt.ylabel('Курс (грн)', fontsize=11)

# Додаємо сітку
plt.grid(True, alpha=0.5)

# Обертаємо підписи дат
plt.xticks(rotation=45)

# Автоматичне вирівнювання
plt.tight_layout()

# Зберігаємо графік у файл
plt.savefig('currency_rates.png', dpi=300, bbox_inches='tight')
print("✓ Графік збережено у файл 'currency_rates.png'")

# Показуємо графік
plt.show()
