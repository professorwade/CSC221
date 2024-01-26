import arcade
import math

# Creates a drawing window
arcade.open_window(600, 600, "Drawing Example")

# Sets the screen color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Put this at the beginning of the drawing commands
arcade.start_render()

# Suppose you wanted to draw the sun and include sunbeams shining out frome it
# Drawing the sun is pretty easy (try a sunset shade)
arcade.draw_circle_filled(300, 300, 50, arcade.color.YELLOW_ORANGE)

# Lets try for a beach sunset scene, second the water
# Note, the reason we do this second is that everything drawn in arcade gets drawn over top
# of what was before. I want the sun to "set" over the water, so I draw the water second to
# cover half the sun.
arcade.draw_rectangle_filled(300, 150, 600, 300, arcade.csscolor.DARK_BLUE)

# Now we want to draw sunbeams coming out of the sun around the sun and extending off the screen
# How? We use trigonometry function sin and cosine and we are going to construct rectangles (beams)
# that extend around the perimeter of the sun off the screen. Each rectangle will have a rotation
# that matches the location on the suns perimeter.

# since we are only doing this on the top half of the sun, our degrees will go from 0 to 180 or
# 0 to pi in radians
# 30 degrees
width = 10
degrees = 30

# I like to work in degrees but the Python standard math library works in radians. Therefore
# we need to convert the degrees we assigned to the variable "degrees" to radians. We can
# do this by calling another function math.radians.
x_start = 300 + math.cos(math.radians(degrees)) * 55


y_start = 300 + math.sin(math.radians(degrees)) * 55
x_end = 300 + math.cos(math.radians(degrees)) * 400
y_end = 300 + math.sin(math.radians(degrees)) * 400
arcade.draw_line(x_start, y_start, x_end, y_end, arcade.color.YELLOW_ORANGE, width)

# 60 degrees
degrees = 60
x_start = 300 + math.cos(math.radians(degrees)) * 55
y_start = 300 + math.sin(math.radians(degrees)) * 55
x_end = 300 + math.cos(math.radians(degrees)) * 400
y_end = 300 + math.sin(math.radians(degrees)) * 400
arcade.draw_line(x_start, y_start, x_end, y_end, arcade.color.YELLOW_ORANGE, width)

# 90 degrees
degrees = 90
x_start = 300 + math.cos(math.radians(degrees)) * 55
y_start = 300 + math.sin(math.radians(degrees)) * 55
x_end = 300 + math.cos(math.radians(degrees)) * 400
y_end = 300 + math.sin(math.radians(degrees)) * 400
arcade.draw_line(x_start, y_start, x_end, y_end, arcade.color.YELLOW_ORANGE, width)

# 120 degrees
degrees = 120
x_start = 300 + math.cos(math.radians(degrees)) * 55
y_start = 300 + math.sin(math.radians(degrees)) * 55
x_end = 300 + math.cos(math.radians(degrees)) * 400
y_end = 300 + math.sin(math.radians(degrees)) * 400
arcade.draw_line(x_start, y_start, x_end, y_end, arcade.color.YELLOW_ORANGE, width)

# 150 degrees
degrees = 150
x_start = 300 + math.cos(math.radians(degrees)) * 55
y_start = 300 + math.sin(math.radians(degrees)) * 55
x_end = 300 + math.cos(math.radians(degrees)) * 400
y_end = 300 + math.sin(math.radians(degrees)) * 400
arcade.draw_line(x_start, y_start, x_end, y_end, arcade.color.YELLOW_ORANGE, width)

# Well, this is good but seems like a lot of typing. Agree? And yes there is a much easier way to
#do the same thing and more. Stay tuned!

# Put this at the end of the drawing commands
arcade.finish_render()

# Important! This keeps the window up until someone closes it.
arcade.run()