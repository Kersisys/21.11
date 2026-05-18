#Requires AutoHotkey v2.0
#SingleInstance Force
#Warn

; === ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ ===
global g_SequenceRunning := false
global g_StopRequested := false

; === ФУНКЦИИ ДЛЯ ВВОДА ===
MButtonPress() {
    Send "{MButton}"
}

ArrowUpPress() {
    Send "{Up}"
}

BackspacePress() {
    Send "{Backspace}"
}

DotPress() {
    Send "."
}

EnterPress() {
    Send "{Enter}"
}

; === ТЕСТОВЫЕ ГОРЯЧИЕ КЛАВИШИ ===
F1::MButtonPress()
F2::ArrowUpPress()
F3::BackspacePress()
F4::DotPress()
F5::EnterPress()

; === ПОСЛЕДОВАТЕЛЬНОСТЬ ОДИН РАЗ ===
Del:: {

    ; Блок последовательности
    DotPress()
    Sleep 120
    ArrowUpPress()
    Sleep 120
    EnterPress()

}
