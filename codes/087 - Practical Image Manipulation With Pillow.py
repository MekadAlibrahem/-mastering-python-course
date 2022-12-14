'''
====================================
-- 087 - Practical Image Manipulation With Pillow 
-- link : https://www.youtube.com/watch?v=mwmyhIzfkl4&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -------------------------------------------------
# -- Practical =&gt; Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open("D:\Python\Files\game.jpg")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (300, 300, 800, 800)
myNewImage = myImage.crop(myBox)

# Show The New Image
myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show()