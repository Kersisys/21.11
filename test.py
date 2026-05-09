import pyautogui
import cv2
import numpy as np
import time
import os

# Координаты области (x1, y1, x2, y2)
REGION = (20, 425, 440, 206)  # x, y, width, height

# Папка для скриншотов
SAVE_DIR = r"C:\Users\_-Keri-_\Desktop\auto_spam\screenshots"
os.makedirs(SAVE_DIR, exist_ok=True)

# Интервал между скриншотами (секунды)
INTERVAL = 5

def capture_region(region):
    """Делает скриншот области и возвращает изображение в BGR"""
    x, y, w, h = region
    img = pyautogui.screenshot(region=(x, y, w, h))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

if __name__ == "__main__":
    print(f"▶ Скриншоты будут сохраняться каждые {INTERVAL} секунд. Ctrl+C для остановки.")

    try:
        while True:
            img = capture_region(REGION)
            timestamp = time.strftime("%Y-%m-%d_%H%M%S")
            filepath = os.path.join(SAVE_DIR, f"screenshot_{timestamp}.png")
            cv2.imwrite(filepath, img)
            print(f"💾 Сохранён скриншот: {filepath}")
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\n⏹ Скрипт остановлен пользователем.")
