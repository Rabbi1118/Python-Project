from PIL import Image,ImageEnhance,ImageFilter
import os

path = f"Input_location_path (Create a folder --> Image)"
path_out = f"Output_location_path (Create a folder --> Edited_Image)"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{path_out}/{clean_name}_edited.png")




