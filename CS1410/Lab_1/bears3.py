from PIL import Image, ImageFilter

filename = 'starr_bears.jpg'
file_out = 'bears3.jpg'
file_ball = 'redBalloon.jpg'

with Image.open(file_ball) as ball_img, Image.open(filename) as bears_img:
    ball_pixel_map = ball_img.load()
    bears_pixel_map = bears_img.load()

    start_x = 200
    start_y = 100

    for x in range(ball_img.width):
        for y in range(ball_img.height):
            r, g, b = ball_pixel_map[x, y]

            if r > 240 and g > 240 and b > 240:
                continue
            bears_pixel_map[start_x + x, start_y + y] = (r, g, b)

new_image = bears_img
new_image.save(file_out)