import cv2
from PIL import ImageGrab
import numpy as np

ImageGrab.grab().save("sample.png")

def find_image_in_image(image, template):
    # Load images
    img = cv2.imread(image)
    templ = cv2.imread(template)

    # Find template in image
    res = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    if len(loc[0]) > 0:
        return True
    else:
        return False

template_image = r"C:\Users\Sazid\Desktop\do not delete\image2.png"

x = contains_template = find_image_in_image('sample.png', template_image)

print(x)
