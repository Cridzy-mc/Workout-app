"""Draw the app icon (a barbell on ember orange) at the sizes iOS and the manifest need."""
from PIL import Image, ImageDraw
import os
os.makedirs("icons", exist_ok=True)
def icon(size):
    s = size / 512
    im = Image.new("RGB", (size, size), "#d9480f")
    d = ImageDraw.Draw(im)
    R = lambda x0, y0, x1, y1, r: d.rounded_rectangle([x0*s, y0*s, x1*s, y1*s], radius=r*s, fill="#ffffff")
    R(96, 244, 416, 268, 8)            # bar
    R(130, 176, 168, 336, 12)          # inner plates
    R(344, 176, 382, 336, 12)
    R(90, 206, 124, 306, 10)           # outer plates
    R(388, 206, 422, 306, 10)
    return im
for n in (180, 192, 512):
    icon(n).save(f"icons/icon-{n}.png")
