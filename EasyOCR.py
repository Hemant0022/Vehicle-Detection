import easyocr
from IPython.display import Image
Image("plates\Plate_img0.jpg")

reader = easyocr.Reader(['en'])

output = reader.readtext("plates\Plate_img0.jpg")

print(output)


# import pickle
# print("runn")