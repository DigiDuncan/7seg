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
        self.ms = False
        self.colons = True
        self.blink = False

        self.sprite_list = None
        self.ms_sprite_list = None
        self.digits = None

        self.now = arrow.now()

        # Init the parent class
        super().__init__(width, height, title, update_rate = 1 / 240)

    def setup(self):
        """ Set up everything with the game """
        self.sprite_list = arcade.SpriteList()
        self.ms_sprite_list = arcade.SpriteList()

        DIGIT_WIDTH = 150
        self.digit_H1 = SevenSeg(DIGIT_WIDTH)
        self.digit_H2 = SevenSeg(DIGIT_WIDTH)
        self.digit_M1 = SevenSeg(DIGIT_WIDTH)
        self.digit_M2 = SevenSeg(DIGIT_WIDTH)
        self.digit_S1 = SevenSeg(DIGIT_WIDTH)
        self.digit_S2 = SevenSeg(DIGIT_WIDTH)
        self.digit_MS1 = SevenSeg(DIGIT_WIDTH // 4)
        self.digit_MS2 = SevenSeg(DIGIT_WIDTH // 4)
        self.digit_MS3 = SevenSeg(DIGIT_WIDTH // 4)
        self.digits = [self.digit_H1, self.digit_H2, self.digit_M1, self.digit_M2, self.digit_S1, self.digit_S2]
        self.ms_digits = [self.digit_MS1, self.digit_MS2, self.digit_MS3]
        for digit in self.digits:
            self.sprite_list.append(digit)
            digit.center_y = self.get_size()[1] // 2
        for digit in self.ms_digits:
            self.ms_sprite_list.append(digit)
            digit.top = self.digit_S2.bottom - 20

        self.digit_M1.right = self.get_size()[0] // 2
        self.digit_M2.left = self.get_size()[0] // 2
        self.digit_H2.right = self.digit_M1.left - (self.digit_M1.width // 4)
        self.digit_H1.right = self.digit_H2.left
        self.digit_S1.left = self.digit_M2.right + (self.digit_M2.width // 4)
        self.digit_S2.left = self.digit_S1.right

        self.digit_MS3.right = self.digit_S2.right
        self.digit_MS2.right = self.digit_MS3.left
        self.digit_MS1.right = self.digit_MS2.left

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        match key:
            case arcade.key.EQUAL:
                self.color_cursor += 1
            case arcade.key.MINUS:
                self.color_cursor -= 1
            case arcade.key.T:
                self.text = not self.text
            case arcade.key.M:
                self.ms = not self.ms
            case arcade.key.C:
                self.colons = not self.colons
            case arcade.key.B:
                self.blink = not self.blink
        self.color_cursor %= len(self.colors)
        for digit in self.digits:
            digit.on_color = self.colors[self.color_cursor]

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.fps = round(1 / delta_time)
        self.now = arrow.now()
        hs = f"{self.now.format('h'):>2}"
        ms = self.now.format('mm')
        ss = self.now.format('ss')
        mss = self.now.format('SSS')
        fulltime = hs + ms + ss
        for n, c in enumerate(fulltime):
            self.digits[n].set_char(c)
        for n, c in enumerate(mss):
            self.ms_digits[n].set_char(c)

        # the worst pm check
        if self.now.format('a')[0] == "p":
            self.digit_H2.dot = True

        if self.ms:
            self.digit_S2.dot = True
            self.ms_sprite_list.update()
        self.sprite_list.update()

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.sprite_list.draw()
        if self.ms:
            self.ms_sprite_list.draw()

        # Colons
        if self.colons:
            circle_size = self.digit_H1.circle_size // 2
            colon_1_x = (self.digit_H2.center_x + self.digit_M1.center_x) // 2 - (self.digit_M1.width // 8)
            colon_2_x = (self.digit_M2.center_x + self.digit_S1.center_x) // 2 - (self.digit_S1.width // 8)
            colon_a_y = self.digit_H1.center_y + (self.digit_H1.height // 5)
            colon_b_y = self.digit_H1.center_y - (self.digit_H1.height // 5)
            circle_color = self.digit_H1.off_color if self.now.second % 2 and self.blink else self.digit_H1.on_color

            arcade.draw_circle_filled(colon_1_x, colon_a_y, circle_size, circle_color)
            arcade.draw_circle_filled(colon_1_x, colon_b_y, circle_size, circle_color)
            arcade.draw_circle_filled(colon_2_x, colon_a_y, circle_size, circle_color)
            arcade.draw_circle_filled(colon_2_x, colon_b_y, circle_size, circle_color)

        # Debug
        if self.text:
            arcade.draw_text(f"{self.now.format('HH:mm:ss')} | Color: {self.colors[self.color_cursor]}", 0, 5)
            arcade.draw_text("+/- to change color | [M] for ms | [C] for colons | [B] for blinking | [T] for debug info", 0, 25)
            arcade.draw_text(f"{self.fps} FPS", 0, 45)


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
