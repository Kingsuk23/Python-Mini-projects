import os
from PIL import Image

def add_watermark(input_image_path,watermark_image_path,output_image_path):
    base_image=Image.open(input_image_path)
    watermark=Image.open(watermark_image_path).convert("RGBA")
    position=base_image.size
    new_size= (int(position[0]*8/100),int(position[0]*8/100))
    watermark=watermark.resize(new_size)

    new_position=position[0]-new_size[0]-20,position[1]-new_size[0]-20
    transparent=Image.new(mode="RGBA",size=position,color=(0,0,0,0))
    transparent.paste(base_image,(0,0))
    transparent.paste(watermark,new_position,watermark)
    image_mode=base_image.mode

    if image_mode=="RGB":
        transparent=transparent.convert(image_mode)
    else:
        transparent=transparent.convert("P")
    transparent.save(output_image_path,optimize=True,quality=100)

folder = input("Enter Folder path: ").strip()
Watermark=input("Enter watermark path: ").strip()
os.chdir(folder)
files=os.listdir(os.getcwd())

output_dir= input_path=os.path.join(folder,"Output")
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

for f in files:
    input_path=os.path.join(folder,f)

    if os.path.isfile(os.path.abspath(f)):
        if os.path.isfile(input_path) or f.lower().endswith(('.jpg', '.png')):
            output_path= os.path.join(output_dir, f)
            try:
                add_watermark(input_path,Watermark,output_path)
            except Exception as e:
                print(f"❌ Failed to process {f}: {e}")