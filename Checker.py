import pyautogui
import numpy as np
import time
from telegram import send_telegram_message  # Импорт функции

# Область скриншота (x, y, width, height)
REGION = (20, 425, 475, 225)

# Координаты точек внутри этой области
PIXELS = [
    (15, 27),
    (15, 92),
    (15, 157),
    (15, 58),
    (15, 123),
    (15, 91),
    (15, 23),
    (15, 84),
    (15, 145),
    (15, 55),
    (15, 115),
]

# Целевой цвет (в формате RGB)
TARGET_COLOR = (222, 222, 222)  # #dedede

# Погрешность при сравнении цвета
COLOR_TOLERANCE = 10

# Интервал проверки (секунды)
INTERVAL = 0.3

# Глобальный флаг остановки
stop_detector = False

# Переменные для предотвращения спама в Telegram
last_notification_time = 0
NOTIFICATION_COOLDOWN = 20  # Ограничение: 1 сообщение в 60 секунд

def color_match(c1, c2, tol=COLOR_TOLERANCE):
    """Проверка, что два цвета примерно равны"""
    return all(abs(int(a) - int(b)) <= tol for a, b in zip(c1, c2))

def capture_region(region):
    """Делает скриншот указанной области"""
    x, y, w, h = region
    img = pyautogui.screenshot(region=(x, y, w, h))
    return np.array(img)

def check_pixels(img):
    """Проверяет, есть ли среди указанных пикселей нужный цвет"""
    for (px, py) in PIXELS:
        if py >= img.shape[0] or px >= img.shape[1]:
            continue
        color = tuple(img[py, px][:3])
        if color_match(color, TARGET_COLOR):
            return True, color
    return False, None

def run_detector(get_spam_active):
    """Основной цикл детектора, работает в отдельном потоке"""
    global stop_detector, last_notification_time
    print("👁 Детектор уведомлений запущен")

    while not stop_detector:
        try:
            # Если сейчас идёт спам — пропускаем проверку
            if get_spam_active():
                time.sleep(INTERVAL)
                continue

            img = capture_region(REGION)
            found, color = check_pixels(img)

            if found:
                print(f"[✔] Найден пиксель #dedede — уведомление! Цвет: {color}")
                # Проверяем, прошло ли достаточно времени с последнего уведомления
                current_time = time.time()
                if current_time - last_notification_time >= NOTIFICATION_COOLDOWN:
                    # Формируем сообщение с временной меткой
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    message = f"🚨 Обнаружен отряд!| Время: {timestamp}"
                    send_telegram_message(message)
                    last_notification_time = current_time
                else:
                    print(f"[Telegram] Пропуск отправки: на кулдауне (осталось {NOTIFICATION_COOLDOWN - (current_time - last_notification_time):.1f} сек)")
            else:
                print("[ ] Нет уведомлений.")

            time.sleep(INTERVAL)

        except Exception as e:
            print(f"[Ошибка детектора]: {e}")
            time.sleep(1)

    print("👁 Детектор остановлен.")

if __name__ == "__main__":
    print("▶ Тестовый запуск детектора...")
    run_detector(lambda: False)