""" Importa o pyautogui"""
import pyautogui

def get_mouse_postition():
    x, y = pyautogui.position()

    return x,y