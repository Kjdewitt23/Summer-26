from PIL import Image, ImageFilter

filename = 'starr_bears.jpg'
filepath = f"{filename}"

file_out = 'bears3.jpg'
file_out_path = f"{file_out}"

file_ball = 'redBalloon.jpg'
file_ball_path = f"{file_ball}"

def erode(cycles, image):
    for x in range(cycles):
        image = image.filter(ImageFilter.MinFilter(3))
    return image

def dilate(cycles, image):
    for x in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(3))
    return image

with Image.open(file_ball_path) as ball_img:
    ball_img = ball_img.crop((70, 0, 280, 230))
    #ball_img.show()
    red, green, blue = ball_img.split()
    #red.show()
    #green.show()
    #blue.show()

    threshold = 57
    ball_img_threshold = green.point(lambda x: 0 if x > threshold else 255)
    ball_img_threshold = ball_img_threshold.convert("1")
    # ball_img_threshold.show()

    step_1 = dilate(16, ball_img_threshold)
    ball_mask = erode(16, step_1)
    
    # step_1.show()
    # ball_mask.show()

    ball_mask = ball_mask.convert("L")
    ball_mask = ball_mask.filter(ImageFilter.BoxBlur(4))
    # ball_mask.show()

    blank = ball_img.point(lambda _: 0)
    ball_segmented = Image.composite(ball_img, blank, ball_mask)
    # ball_segmented.show()

with Image.open(filepath) as bears_img:
    bears_img.paste(
        ball_img.resize((ball_img.width // 3, ball_img.height //3)),
        (260, 120),
        ball_mask.resize((ball_mask.width // 3, ball_mask.height //3))
    )
    # bears_img.show()

new_image = bears_img
new_image.save(file_out_path)