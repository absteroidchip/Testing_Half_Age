import arcade

def main():
    arcade.open_window(800, 600, "house window")
    arcade.set_background_color(arcade.color.AERO_BLUE)
    #roof_line = arcade.create_line(0, 300, 300, 300, arcade.color.AMARANTH_PURPLE)
    roof = arcade.create_polygon([(0, 300), (150, 450), (300, 300)], arcade.color.AMARANTH_PURPLE)
    house_outline = arcade.create_polygon([(0, 0), (0, 300), (150, 450), (300, 300), (300, 0)], arcade.color.FAWN)
    window1 = arcade.create_ellipse(75, 200, 50, 50,arcade.color.AFRICAN_VIOLET)
    window2 = arcade.create_ellipse(225, 200, 50, 50, arcade.color.AFRICAN_VIOLET)
    window1_outline = arcade.create_ellipse_outline(225, 200, 50, 50, arcade.color.AMARANTH_PURPLE)
    window2_outline = arcade.create_ellipse_outline(75, 200, 50, 50, arcade.color.AMARANTH_PURPLE)
    door = arcade.create_rectangle(150, 0, 75, 275, arcade.color.AFRICAN_VIOLET)
    door_frame = arcade.create_rectangle_outline(150,0,75,275,arcade.color.AMARANTH_PURPLE)
    chimney = arcade.create_rectangle(40, 350, 50, 100, arcade.color.BROWN_NOSE)
    cloudpart1 = arcade.create_ellipse_filled(400, 400, 100, 75, arcade.color.WHITE)
    cloudpart2 = arcade.create_ellipse_filled(500, 400, 275, 100, arcade.color.WHITE)
    cloudpart3 = arcade.create_ellipse_filled(600, 400, 100, 75, arcade.color.WHITE)
    cloudpart4 = arcade.create_ellipse_filled(500, 425, 150, 125, arcade.color.WHITE)

    arcade.start_render()
    chimney.draw()
    house_outline.draw()
    roof.draw()
    window1.draw()
    window2.draw()
    window1_outline.draw()
    window2_outline.draw()
    door.draw()
    door_frame.draw()
    cloudpart1.draw()
    cloudpart2.draw()
    cloudpart3.draw()
    cloudpart4.draw()
    arcade.finish_render()
    arcade.run()
main()