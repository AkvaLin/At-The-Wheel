from pydispatch import dispatcher
from mainMenu import MainMenu
from game import GameView
from defeatMenu import DefeatMenu

class EventHandler:
    def __init__(self, window):
        self.window = window

        dispatcher.connect(self.set_game, signal='start')
        dispatcher.connect(self.set_defeat, signal='defeat')
        dispatcher.connect(self.set_main, signal='main')

    def set_game(self, event=None):
        game = GameView()
        game.setup()
        self.window.show_view(game)

    def set_main(self, event=None):
        main_menu = MainMenu()
        self.window.show_view(main_menu)

    def set_defeat(self, event=None):
        defeat_menu = DefeatMenu()
        self.window.show_view(defeat_menu)