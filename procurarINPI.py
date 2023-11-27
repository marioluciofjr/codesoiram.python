import pyautogui as py
import pyperclip as clip
from time import *

def procurarINPI():
    marcas = input("Digite os nomes das empresas separados por vírgula: ").split(',')
    for i, marca in enumerate(marcas):
        py.hotkey("ctrl", "t")
        sleep(1.5)
        clip.copy("https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login")
        py.hotkey("ctrl", "v")
        sleep(1.5)
        py.press("enter")
        sleep(1.5)
        py.press("TAB", presses=12)
        py.press("enter")
        sleep(1.5)
        py.press("TAB", presses=13)
        py.press("enter")
        sleep(1.5)
        clip.copy(marca.strip())
        py.hotkey("ctrl", "v")
        sleep(1.5)
        py.press("TAB", presses=3)
        sleep(2)
        py.press('up', presses=4)
        sleep(1.5)
        py.press("TAB", presses=1)
        py.press("enter")
        sleep(2)  
        if i < len(marcas) - 1:  # Se não for a última empresa
            py.hotkey('ctrl', 'pgdn')  # Muda para a próxima guia
    # Volta para a primeira guia
    for _ in range(len(marcas) - 1):
        py.hotkey('ctrl', 'pgup')

procurarINPI()
