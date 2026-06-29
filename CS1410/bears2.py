from PIL import Image

filename = '.\\starr_bears.jpg'
filepath = f"{filename}"

file_out = '.\\bears2.jpg'
file_out_path = f"{file_out}"

orig_image = Image.open(filepath)
new_image = orig_image.convert('L')
new_image.save(file_out_path)

