def hex_color_to_tuple(color):
    red = int(color[1:3], 16)
    green = int(color[3:5], 16)
    blue = int(color[5:7], 16)
    return red, green, blue

color = hex_color_to_tuple("#ff0011")
print(color)