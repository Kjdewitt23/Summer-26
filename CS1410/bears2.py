from PIL import Image

filename = 'starr_bears.jpg'
filepath = f"{filename}"

file_out = 'bears2.jpg'
file_out_path = f"{file_out}"

orig_image = Image.open(filepath)

width, height = orig_image.size

pixel_map = orig_image.load()

for x in range(width):
    for y in range(height):
        pixel_data = pixel_map[x, y]
        r, g, b = pixel_data[0], pixel_data[1], pixel_data[2]

        grayScale = int(0.299 * r + 0.587 * g + 0.114 * b)
        pixel_map[x, y] = (grayScale, grayScale, grayScale)

orig_image.save(file_out_path)

