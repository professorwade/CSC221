"""
Now we can't very well write games without animation. Computers animate in much the same way
that the old cartoonist drew cartoons. Each sheet would be slightly different from the
previous one such that rapidly progressing through the sheets would give the appearance of
animation. See: https://youtu.be/mbpLpxi9rJY?t=128

To employ a similar technique with Python and the arcade library, we first need to set up
a way for a function to be called repeatedly. To do this we use the builtin arcade.schedule
function. Here we pass in as an argument the function we want to call and the period between
calls. Below we have arcade.schedule(on_draw, 1/60) which will call a function named on_draw
every 60th of a second or 60 times per second.

Since we're not changing anything, this code won't look any different than before but we
are set up to animate. Next, we'll move our snow persons.
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


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
    draw_snow_person(150, 140)
    draw_snow_person(450, 180)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()