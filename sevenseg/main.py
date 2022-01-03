from itertools import cycle

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
        self.cursor = 0
        self.dot = False
        self.digit_0 = SevenSeg(200)
        self.digit_0.center_x = self.get_size()[0] // 2
        self.digit_0.center_y = self.get_size()[1] // 2

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        match key:
            case arcade.key.PERIOD:
                self.dot = not self.dot
            case arcade.key.EQUAL:
                self.cursor += 1
            case arcade.key.MINUS:
                self.cursor -= 1
        self.cursor %= len(self.digits)
        self.digit_0.set_char(self.digits[self.cursor])
        self.digit_0.dot = self.dot

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        pass

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.digit_0.draw()


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
