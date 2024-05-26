import PIL.Image as Image
import numpy as np

file_location = r"C:\Users\Sazid\Desktop\final_csv_result\test1.png"
path_to_save = r"C:\Users\Sazid\Desktop\final_csv_result\out_test1.png"

img = Image.open(file_location)
rgb_data = np.array(img)


rgb_data = Image.fromarray(rgb_data)
rgb_data.save(path_to_save, format="PNG")
