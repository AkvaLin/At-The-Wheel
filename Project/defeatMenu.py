import arcade
import arcade.gui
from pydispatch import dispatcher


class DefeatMenu(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        defeat_lbl = arcade.gui.UILabel(text="Defeat", font_size=48)
        restart_button = arcade.gui.UIFlatButton(text="Restart", width=250)
        exit_button = arcade.gui.UIFlatButton(text="Exit", width=250)

        self.box = arcade.gui.UIBoxLayout(space_between=20)

        self.box.add(defeat_lbl)
        self.box.add(restart_button)
        self.box.add(exit_button)

        @restart_button.event("on_click")
        def on_click_restart_button(event):
            dispatcher.send('start')

        @exit_button.event("on_click")
        def on_click_exit_button(event):
            dispatcher.send('main')

        self.anchor = self.manager.add(arcade.gui.UIAnchorWidget(child=self.box))

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_CANDY_APPLE_RED)

        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()

        self.manager.draw()
