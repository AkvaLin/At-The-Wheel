import arcade
import arcade.gui
from pydispatch import dispatcher


class MainMenu(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        label = arcade.gui.UILabel(text="At The Wheel", font_size=52, bold=True)
        start_button = arcade.gui.UIFlatButton(text="Start", width=250)
        exit_button = arcade.gui.UIFlatButton(text="Exit", width=250)

        self.box = arcade.gui.UIBoxLayout(space_between=20)

        self.box.add(label)
        self.box.add(start_button)
        self.box.add(exit_button)

        @start_button.event("on_click")
        def on_click_start_button(event):
            dispatcher.send('start')

        @exit_button.event("on_click")
        def on_click_exit_button(event):
            arcade.close_window()

        self.anchor = self.manager.add(arcade.gui.UIAnchorWidget(child=self.box))

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()

        self.manager.draw()
