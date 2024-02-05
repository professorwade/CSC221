"""
This file is just to illustrate how to do part3b with global variables. This is shown for the
purpose of understanding, not as a recommendation. It is recommended for the vast majority of
cases to not use global variables.
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

snow_person_xpos = 0

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    global snow_person_xpos # this is needed to specify that snow_person_xpos is a global variable
    draw_snow_person(snow_person_xpos, 140)
    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.

    # this line is somewhat modified from what is in the textbook
    snow_person_xpos = (snow_person_xpos + 5) % 800


# Create a value that our on_draw.snow_person1_x will start at.
#on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


# Call the main function to get the program started.
main()