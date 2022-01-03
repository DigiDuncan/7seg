import arcade

from sevenseg.sevensegment import get_segment_point_list

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
        pass

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        pass

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        pass

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        points = get_segment_point_list(True, 400, 90, 100, 100)
        arcade.draw_points(points, arcade.color.RED, 5)
        arcade.draw_polygon_filled(points, arcade.color.RED)
        for i, point in enumerate(points):
            arcade.draw_text(str(i), point[0], point[1], arcade.color.WHITE)


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
