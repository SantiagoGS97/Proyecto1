import unittest
import numpy as np
from PIL import Image
from detector_neumonia import ImageReader

def test_random():
    assert True is True
    
class TestCase(unittest.TestCase):
    def test_random(self): 
        a = 1
        self.assertEqual(a, 1)


# class TestImageProcessor(unittest.TestCase):

#     def test_read_dicom_file(self, imagen):
#         processor = ImageReader.process_image(imagen)
#         img_RGB, img2show = processor.read_dicom_file()
        
#         self.assertIsInstance(img_RGB, np.ndarray)
#         self.assertIsInstance(img2show, Image.Image)
#         self.assertEqual(img_RGB.shape, (2, 2, 3))  # Should be RGB image with 3 channels


#     def test_read_jpg_file(self, imagen):
#         # Mock JPG file
#         img2, img2show = ImageReader.process_image(imagen)
#         self.assertEqual(img2, np.ndarray)
#         self.assertEqual(img2show, Image.Image)
#         self.assertEqual(img2.shape, (2, 2))  # Should be a grayscale image