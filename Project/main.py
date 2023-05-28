import arcade
from eventHandler import EventHandler

SCREEN_TITLE = 'At The Wheel'

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

handler = None

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    handler = EventHandler(window)
    handler.set_main()
    arcade.run()

if __name__ == '__main__':
    main()
