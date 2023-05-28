from mainMenu import MainMenu
import arcade

SCREEN_TITLE = 'At The Wheel'

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    menu = MainMenu()
    window.show_view(menu)
    arcade.run()

if __name__ == '__main__':
    main()
