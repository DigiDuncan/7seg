import arcade

from sevenseg.sevensegment import SevenSeg

SCREEN_TITLE = "7Seg"

# Size of screen to show, in pixels
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """

        # Init the parent class
        super().__init__(width, height, title)

    def setup(self):
        """ Set up everything with the game """
        self.digits = "0123456789abcdef "
        self.colors = [arcade.color.RED, arcade.color.GREEN, arcade.color.BLUE,
                       arcade.color.CYAN, arcade.color.MAGENTA, arcade.color.YELLOW,
                       arcade.color.WHITE]
        self.cursor = 0
        self.color_cursor = 0
        self.dot = False
        self.text = False
        self.digit_0 = SevenSeg(300, thinness=6.5, on_color=arcade.color.BLUE)
        self.digit_0.center_x = self.get_size()[0] // 2
        self.digit_0.center_y = self.get_size()[1] // 2

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        match key:
            case arcade.key.PERIOD:
                self.dot = not self.dot
            case arcade.key.EQUAL:
                if modifiers & arcade.key.MOD_SHIFT:
                    self.color_cursor += 1
                else:
                    self.cursor += 1
            case arcade.key.MINUS:
                if modifiers & arcade.key.MOD_SHIFT:
                    self.color_cursor -= 1
                else:
                    self.cursor -= 1
            case arcade.key.T:
                self.text = not self.text
        self.cursor %= len(self.digits)
        self.color_cursor %= len(self.colors)
        self.digit_0.set_char(self.digits[self.cursor])
        self.digit_0.dot = self.dot
        self.digit_0.on_color = self.colors[self.color_cursor]

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.fps = round(1 / delta_time)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.digit_0.draw()
        if self.text:
            arcade.draw_text(f"Char: {self.digits[self.cursor]} | Color: {self.colors[self.color_cursor]}", 0, 5)
            arcade.draw_text("+/- to inc/dec, SHIFT +/- to change color", 0, 25)
            arcade.draw_text(f"{self.fps} FPS", 0, 45)


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
