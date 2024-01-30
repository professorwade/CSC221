import arcade
STAR_SCALE = 1

star_texture = arcade.load_texture("small_star.png")
arcade.open_window(600, 600, "Seeing Stars")
arcade.set_background_color(arcade.color.BLACK)
x_points = []
y_points = []
flag = True
while flag:
    x = int(input("Enter a x coordinate: (0-599)"))
    y = int(input("Enter a y coordinate (0-599)"))
    if x == -1 or y == -1:
        break
    x_points.append(x)
    y_points.append(y)

arcade.start_render()

for i in range(len(x_points)):
    arcade.draw_scaled_texture_rectangle(x_points[i],y_points[i],star_texture, STAR_SCALE, 0)

arcade.finish_render()
arcade.run()
