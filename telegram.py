import requests

# Telegram Bot Token и Chat ID
BOT_TOKEN = "8598564656:AAEIs4Tc8XhdQ8xeGvqqYxPqtn6fM1qZj4g"  # Замените на ваш токен бота
CHAT_ID = "5685466268"      # Замените на ваш chat_id

def send_telegram_message(message):
    """Отправляет сообщение в Telegram чат"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"  # Опционально, для форматирования
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"[✔] Сообщение отправлено в Telegram: {message}")
        else:
            print(f"[Ошибка Telegram]: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[Ошибка Telegram]: {e}")

if __name__ == "__main__":
    print("Тестовая отправка сообщения...")
    send_telegram_message("Тестовое сообщение от бота!")