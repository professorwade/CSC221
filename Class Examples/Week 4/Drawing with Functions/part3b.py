"""
With functions, each time you call them, any variables defined therein are initialized again
 just as the previous call. Consequently, it is difficult to establish a function with a
 memory. If this happened automatically, we could just tell the draw_snow_person code to
 move over a pixel with each successive call and the snow_person would draw, erase, re-draw and
 give use the animation we want.

 That said, there are simple ways to accomplish this that we'll use here. Later you'll learn
 better ways to accomplish more elaborate animations. For now, we need to create a variable
 associated with the on_draw function. (Actually what we are doing is dynamically adding an
 attribute to the on_draw object, but we'll learn more about that later) For now, we just need
 a persistant variable that we can change with each call and create our movement. (Note: the
 modification line is a little different from the text as I changed it such that the snow_person
 moves a little faster and resets to 0 when it goes off the screen. I do this with the remainder
 operator.

 Note that you can also do this with global variables though they should be avoided in general
 as they can complicate code re-use. I'll show how to do this in part3c.py.
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
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.

    # this line is somewhat modified from what is in the textbook
    on_draw.snow_person1_x = (on_draw.snow_person1_x + 5) % 800


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()