''' Edit all images in a directory with choosen Pillow functions.
    Put all the images you want to edit in the imgs folder and run.
    All edited images will be in the edited_imgs folder.  '''
from PIL import Image, ImageEnhance, ImageFilter
import os

#.venv is giving wrong path when in directories below
# if using as a separate module use
# path_in = './imgs'
# path_out = './edited_imgs'

path_in = './python_automation/imgs'
path_out = './python_automation/edited_imgs'

print(os.getcwd())

for filename in os.listdir(path_in):
    img = Image.open(f"{path_in}/{filename}")
    # make your image edits.
    # Pillow handbook here: https://pillow.readthedocs.io/en/stable/handbook/index.html
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    # resize the image keeping aspect ratio
    edit.thumbnail((400, 400))
    # Split the pathname path into a pair (root, ext)
    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{path_out}/{clean_name}_edited.jpg")
