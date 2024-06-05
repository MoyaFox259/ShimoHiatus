from MenuNavigation import MenuNavigator

class MainMenu(MenuNavigator):
    def __init__(self, isBetweenspaceUnlocked:bool=False, isTamasatchiUnlocked:bool=False):
        items_unlocked = ["Rhythm Play",
                          "Course Mode",
                          "Song Shop",
                          "Node Flowchart",
                          "Profile",
                          "Rating List",
                          "User Manual",
                          "System Options"]
        if isBetweenspaceUnlocked:
            items_unlocked.insert(4, "Betweenspace")
            if isTamasatchiUnlocked:
                items_unlocked.insert(5, "Tamasatchi")
        super().__init__(items_unlocked, 1, len(items_unlocked), 1)
