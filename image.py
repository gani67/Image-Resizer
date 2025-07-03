import os
from PIL import Image

input_folder = 'input_images'
output_folder = 'resized_images'
new_size = (800, 800)

# Check if input folder exists
if not os.path.exists(input_folder):
    print(f"Input folder '{input_folder}' not found. Please create it and add images.")
    exit()

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(new_size)
        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)
        print(f"Resized and saved: {filename}")

print("Batch image resize complete.")

