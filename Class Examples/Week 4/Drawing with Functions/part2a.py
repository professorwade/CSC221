"""
The process of refining your code is called re-factoring. Essentially it is a process of
improving the structure or implementation to gain maintainability, efficiency, error
tolerance, etc., I.e. making it better. This is an important lifecycle step in sofware
development and a good practice for professionals.

First we will "pull out" the code for drawing grass and put it in its own function. Once
done, we will call that function in the main function where the code came from. By naming
our functions clear, descriptive names, we improve the readability of our code and make
it easier to maintain by separating large tasks into smaller ones. This also allows for other
code to "import" these functions and use them.
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()

    # Draw a snow person

    # Snow
    arcade.draw_circle_filled(300, 200, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 280, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 340, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285, 350, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315, 350, 5, arcade.color.BLACK)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()