import os
def read_images_add():
    BASE_ADD = "~/donmemedo/1/Vision Codes/1/pics"
    image_files = []
    for root, dirs, files in os.walk(BASE_ADD):
        for file in files:
            (os.path.join(root,file))
            image_files.append(os.path.join(root,file))
    return  image_files,

