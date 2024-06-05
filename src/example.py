import pyautogui as ag
import time
from MenuNavigation import MenuNavigator
from TamaSousa import Tamasatchi
from ExampleMenu import MainMenu

# Sets up a 0.55 second pause after each pyautogui call:
ag.PAUSE = 0.55

# A message box shows up:
desc = "Start the game and keep the game focused while staying at the title screen for the next 10 seconds for the automation.\n"
desc += "Visual-locate functions are unavailable and currently under development.\n"
desc += "Press OK to proceed and click the game window to make it stay focused."
button_clicked = ag.confirm(text=desc, title="Demonstration", buttons=["OK", "Cancel"])

# TODO: Add visual_locate functions

if button_clicked == "OK":

    # On title screen:
    time.sleep(10)

    # Enters Main menu:
    ag.press("enter")
    time.sleep(4)

    # Navigate through the Main menu:
    main_menu = MainMenu(isBetweenspaceUnlocked=True, isTamasatchiUnlocked=True)
    main_menu.move_cursor_to("Tamasatchi")

    # Enters Tamasatchi:
    ag.press("enter")
    time.sleep(3)

    # Buys tickets and spends them on Satchapon:
    tama = Tamasatchi(purchase_left=3)
    tama.buy({"Tickets": 3})
    tama.satchapon(2)
