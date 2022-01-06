import random
import string
import arcade

SCREEN_TITLE = "draw_text() demo"
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
        self.text = [arcade.Text(make_random_string(), start_x=5, start_y=self.height - (40 + (20 * i))) for i in range(50)]

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.W:
            self.text_amount += 1
        elif key == arcade.key.Q:
            self.text_amount -= 1
        self.text_amount = max(min(self.text_amount, 35), 0)

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

        for text in self.text[0:self.text_amount]:
            text.draw()


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
