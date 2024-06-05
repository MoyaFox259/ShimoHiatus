import pyautogui as ag
import time
from MenuNavigation import MenuNavigator

class Tamasatchi(MenuNavigator):
    def __init__(self, purchase_left:int=3):
        super().__init__(["Rename", "Reclass", "Shop",
                       "Give Item", "Satchapon", "Trial"],3,2,1)

        self.syn = {"Apathy Pill": ["Max LIFE", "LIFE", "HP"],
                    "Antipathy Pill": ["ATTACK", "ATK"],
                    "Empathy Pill": ["DEFENSE", "DEF"],
                    "Sympathy Pill": ["SUPPORT", "SPT", "SP", "HEALING", "HEAL"],
                    "Powersaves": ["Level", "LV"],
                    "Tickets for Two": ["Tickets", "Ticket"]}

        self.shop = Shop()
        self.purchase_left = purchase_left
        self.shopping_list = []

    def buy(self, items:iter):
        if isinstance(items, str):
            self.add_to_shopping_list(items)
        elif isinstance(items, dict):
            for k,v in items.items():
                for _ in range(v):
                    self.add_to_shopping_list(k)
        else:
            for i in items:
                self.add_to_shopping_list(i)

        self.move_cursor_to("Shop")

        #TODO:check shop cooldown or purchases left

        ag.press("enter")
        for i in range(min(len(self.shopping_list), self.purchase_left)):
            self.shop.move_cursor_to(self.shopping_list[0])
            ag.press("enter")
            self.shopping_list.pop(0)

    def add_to_shopping_list(self, item:str):
        if item not in self.shop.items:
            item = self.match_syn(item)
        if item:
            self.shopping_list.append(item)

    def match_syn(self, string:str):
        for k,v in self.syn.items():
            for s in v:
                if string.lower() == s.lower():
                    return k
        else:
            return

    def satchapon(self, count:int):
        self.move_cursor_to("Satchapon")
        ag.press("enter")
        time.sleep(0.5)
        for _ in range(abs(count)):
            ag.keyDown("enter")
            time.sleep(2)
            ag.keyUp("enter")
            time.sleep(2)
        ag.press("esc")

class Shop(MenuNavigator):
    def __init__(self):
        super().__init__(["Tickets for Two", "Apathy Pill",
                        "Antipathy Pill", "Empathy Pill",
                        "Sympathy Pill", "Powersaves"],2,3,1)
