from PIL import Image
import pathlib
import os
import shutil
# I used a bunch of libraries, to not re-invent the wheel

# ONLY CHANGE THESE TWO LINES
path_for_original_photos = "./Photos"
path_for_new_photos = "./NewPhotos"

# Don't Change Anything Below Here.
for file in os.listdir(path_for_original_photos):
    src = f"{path_for_original_photos}/{file}"
    ext = pathlib.Path(src).suffix
    img = Image.open(src)
    img_exif = img.getexif()
    for key, value in img_exif.items():
        if key == 306:
            shutil.copyfile(
                src=src,
                dst=f'{path_for_new_photos}/{value}{ext}'
            )
            break
