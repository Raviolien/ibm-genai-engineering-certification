import requests
import glob
import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Specify the directory where your images are
image_dir = "../pictures"
image_exts = ["jpg", "jpeg", "png"]  # specify the image file extensions to search for

# Open a file to write the captions
with open("captions_local_drive.txt", "w") as caption_file:
    # Iterate over each img element
    for image_ext in image_exts:
        for img_path in glob.glob(os.path.join(image_dir, f"*.{image_ext}")):
            
            # Load your image from the local drive
            raw_image = Image.open(img_path).convert('RGB')

            # You do not need a question for image captioning
            inputs = processor(raw_image, return_tensors="pt")
            
            # Generate a caption for the image
            out = model.generate(**inputs, max_new_tokens=50)
            
            # Decode the generated tokens to text
            caption = processor.decode(out[0], skip_special_tokens=True)

            # Write the caption to the file, prepended by the image file name
            caption_file.write(f"{os.path.basename(img_path)}: {caption}\n")