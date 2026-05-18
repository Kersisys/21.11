import subprocess
import os

# Путь к AutoHotkey.exe
ahk_exe = r"C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe"
# Путь к AHK скрипту
ahk_script = r"C:\Users\_-Keri-_\Desktop\auto_spam\new.ahk"

# Проверка файлов
if not os.path.exists(ahk_exe):
    raise FileNotFoundError(f"AutoHotkey.exe не найден: {ahk_exe}")
if not os.path.exists(ahk_script):
    raise FileNotFoundError(f"AHK скрипт не найден: {ahk_script}")

# Глобальный флаг
spam_active = False

def run_spam_cycle():
    """Запуск AHK-скрипта один раз"""
    print("▶ Запуск AHK-скрипта")
    process = subprocess.Popen([ahk_exe, ahk_script])
    process.wait()  # Ждём завершения AHK-скрипта
    print("✅ AHK-скрипт завершён")