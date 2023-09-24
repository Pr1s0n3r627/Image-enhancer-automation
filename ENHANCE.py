# Import necessary libraries
from PIL import Image, ImageEnhance, ImageFilter
import os

# Define input and output directories
input_path = './<your images folder name>'
output_path = './editedImags'

# Iterate through files in the input directory
for filename in os.listdir(input_path):
    # Open the image file
    img = Image.open(os.path.join(input_path, filename))

    # Apply image editing: sharpen and enhance contrast
    edited_img = img.filter(ImageFilter.SHARPEN)
    edited_img = ImageEnhance.Contrast(edited_img).enhance(1.5)

    # Extract the clean file name (remove extension)
    clean_name = os.path.splitext(filename)[0]

    # Save the edited image with a new name in the output directory
    edited_img.save(os.path.join(output_path, f'{clean_name}_edited.jpg'))
