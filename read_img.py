import pydicom as dicom
from PIL import ImageTk, Image
import numpy as np
import cv2


class ImageReader:
    def __init__(self,filepath):
        self.filepath = filepath
        
    def read_dicom_file(self):
        img = dicom.read_file(self.filepath)
        img_array = img.pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        return img_RGB, img2show
    
    def read_jpg_file(self):
        img = cv2.imread(self.filepath)
        img_array = np.asarray(img)
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        return img2, img2show

    def process_image(self):
        if self.filepath.lower().endswith('.dcm'):
            return self.read_dicom_file()
        elif self.filepath.lower().endswith(('.jpg', '.jpeg', '.png')):
            return self.read_jpg_file()
        else:
            raise ValueError("Unsupported file format")