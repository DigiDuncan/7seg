import arcade
import arrow

from sevenseg.sevensegment import SevenSeg

SCREEN_TITLE = "7Seg"

# Size of screen to show, in pixels
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """
        self.colors = [arcade.color.RED, arcade.color.GREEN, arcade.color.BLUE,
                       arcade.color.CYAN, arcade.color.MAGENTA, arcade.color.YELLOW,
                       arcade.color.WHITE]
        self.color_cursor = 0
        self.text = False

        self.sprite_list = None
        self.digits = None
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Init the parent class
        super().__init__(width, height, title)

    def setup(self):
        """ Set up everything with the game """
        self.sprite_list = arcade.SpriteList()
        self.digit_H1 = SevenSeg(150)
        self.digit_H2 = SevenSeg(150)
        self.digit_M1 = SevenSeg(150)
        self.digit_M2 = SevenSeg(150)
        self.digit_S1 = SevenSeg(150)
        self.digit_S2 = SevenSeg(150)
        self.digits = [self.digit_H1, self.digit_H2, self.digit_M1, self.digit_M2, self.digit_S1, self.digit_S2]
        for digit in self.digits:
            self.sprite_list.append(digit)
            digit.center_y = self.get_size()[1] // 2

        self.digit_M1.right = self.get_size()[0] // 2
        self.digit_M2.left = self.get_size()[0] // 2
        self.digit_H2.right = self.digit_M1.left - (self.digit_M1.width // 4)
        self.digit_H1.right = self.digit_H2.left
        self.digit_S1.left = self.digit_M2.right + (self.digit_M2.width // 4)
        self.digit_S2.left = self.digit_S1.right

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        match key:
            case arcade.key.EQUAL:
                self.color_cursor += 1
            case arcade.key.MINUS:
                self.color_cursor -= 1
            case arcade.key.T:
                self.text = not self.text
        self.color_cursor %= len(self.colors)
        for digit in self.digits:
            digit.on_color = self.colors[self.color_cursor]

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.fps = round(1 / delta_time)
        now = arrow.now()
        self.hours, self.minutes, self.seconds = now.hour, now.minute, now.second
        hs = f"{self.hours:02}"
        ms = f"{self.minutes:02}"
        ss = f"{self.seconds:02}"
        fulltime = hs + ms + ss
        for n, c in enumerate(fulltime):
            self.digits[n].set_char(c)

        self.sprite_list.update()

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.sprite_list.draw()
        if self.text:
            hs = f"{self.hours:02}"
            ms = f"{self.minutes:02}"
            ss = f"{self.seconds:02}"
            arcade.draw_text(f"Time: {hs}:{ms}:{ss} | Color: {self.colors[self.color_cursor]}", 0, 5)
            arcade.draw_text("SHIFT +/- to change color", 0, 25)
            arcade.draw_text(f"{self.fps} FPS", 0, 45)


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
