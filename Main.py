import threading
import time
import spam
import Checker
import keyboard

SPAM_INTERVAL = 11     # ПФ, секунды
SPAM_OFFSET = 0.2      # 200 мс

cycle_running = False
spam.spam_active = False  # False -> чек работает

def run_cycle():
    """Бесконечный цикл АФ/ПФ, запускается после Del"""
    global cycle_running
    print("▶ Цикл АФ/ПФ запущен.")
    while cycle_running:
        # --- стоп чек перед АФ ---
        spam.spam_active = True

        # --- перед АФ ---
        time.sleep(SPAM_OFFSET)

        # --- активная фаза (АФ) ---
        try:
            spam.run_spam_cycle()
        except Exception as e:
            print(f"[Ошибка АФ]: {e}")

        # --- после АФ ---
        spam.spam_active = False
        time.sleep(SPAM_OFFSET)

        # --- пассивная фаза ПФ 11 сек, чек работает ---
        elapsed = 0
        while elapsed < SPAM_INTERVAL and cycle_running:
            time.sleep(1)
            elapsed += 1

    print("⏹ Цикл АФ/ПФ остановлен.")

def start_cycle():
    """Запуск цикла и чекера по Del (только включение)"""
    global cycle_running
    if not cycle_running:
        cycle_running = True
        # Запуск чекера
        threading.Thread(target=Checker.run_detector, args=(lambda: spam.spam_active,), daemon=True).start()
        print("👁 Чек уведомлений запущен")
        # Запуск цикла АФ/ПФ
        threading.Thread(target=run_cycle, daemon=True).start()
    else:
        print("Цикл уже запущен.")

def start_controller():
    """Ожидание Del для запуска всего"""
    print("Ожидаю нажатие Del для запуска цикла АФ/ПФ и чека...")
    keyboard.add_hotkey("del", start_cycle)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹ Завершение работы.")
        cycle_running = False

if __name__ == "__main__":
    start_controller()