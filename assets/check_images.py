import os
from PIL import Image

assets_dir = 'assets'
banners = [
    'project_seva.png',
    'project_bachpanshala_juice.png',
    'project_jeev.png',
    'project_udaan.png',
    'project_prakriti.png',
    'project_vikas.png'
]

for banner in banners:
    path = os.path.join(assets_dir, banner)
    if os.path.exists(path):
        with Image.open(path) as img:
            w, h = img.size
            ratio = w / h
            print(f"{banner}: {w}x{h} (Aspect Ratio: {ratio:.2f}:1)")
    else:
        print(f"ERROR: {banner} does not exist at {path}")
