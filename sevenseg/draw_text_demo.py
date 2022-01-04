import random
import string

import arcade

SCREEN_TITLE = "draw_text() demo"

# Size of screen to show, in pixels
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def make_random_string(length = 50):
    s = ""
    for i in range(length):
        s += random.choice(string.printable)
    return s


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        """ Set up everything with the game """
        self.text_amount = 0
        self.strings = [make_random_string() for i in range(50)]

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        match key:
            case arcade.key.PERIOD:
                self.dot = not self.dot
            case arcade.key.EQUAL:
                self.text_amount += 1
            case arcade.key.MINUS:
                self.text_amount -= 1
            case arcade.key.T:
                self.text = not self.text
        self.text_amount = min(self.text_amount, 35)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.fps = round(1 / delta_time)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        arcade.draw_text(f"{self.fps} FPS | {self.text_amount + 1} draw_text() calls", 5, self.get_size()[1] - 20)
        for i in range(self.text_amount):
            arcade.draw_text(self.strings[i], 5, self.get_size()[1] - (40 + (20 * i)))


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
