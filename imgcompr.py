from PIL import Image, ImageEnhance
import os
import tkinter as tk
from tkinter.simpledialog import askstring

input_directory = r"C:\path_containing_the_images"
output_directory = r"C:\where_images_will_be_saved"
target_size = (1920, 1080)

def apply_enhancements(image):
    contrast_factor = 1.08  
    brightness_factor = 1.08  
    saturation_factor = 1.08 
    
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)
    
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)
    
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(saturation_factor)
    
    return image

root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

output_name = askstring("Nombre", "Ingrese el nombre base para las imágenes de salida:")

if output_name is None:
    exit()

count = 1

for filename in os.listdir(input_directory):
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".png") or filename.lower().endswith(".jpeg"):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, f"{output_name}_{count}.jpg")
        
        image = Image.open(input_path)
        
        image.thumbnail(target_size)
        
        image = apply_enhancements(image)
        
        image.save(output_path, format="JPEG", optimize=True, quality=60)
