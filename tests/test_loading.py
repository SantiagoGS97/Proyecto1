import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from PIL import ImageTk, Image
from funciones import predict,preprocess,read_jpg_file,read_dicom_file
import cv2
import pydicom
import warnings
import pytest

    
class TestCase(unittest.TestCase):
    def test_random(self): 
        a = 1
        self.assertEqual(a, 1)
######################### Prueba 1 ##################################################################
class TestReadJpgFile(unittest.TestCase):
    @patch('cv2.imread')
    def test_read_jpg_file(self, mock_imread):
        mock_img = np.array([[0, 1], [2, 3]], dtype=np.uint8)
        mock_imread.return_value = mock_img
        filepath = 'dummy.jpg'
        img2, img2show = read_jpg_file(filepath)
        self.assertIsInstance(img2, np.ndarray)
        self.assertIsInstance(img2show, Image.Image)
        self.assertEqual(img2.shape, mock_img.shape)

######################### Prueba 2 ##################################################################      
class MyClass:
    def __init__(self, filepath):
        self.filepath = filepath
    def read_dicom_file(self):
        img = pydicom.dcmread(self.filepath)
        img_array = img.pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        return img_RGB, img2show

class TestReadDicomFile(unittest.TestCase):
    @patch('pydicom.dcmread')
    def test_read_dicom_file(self, mock_dcmread):
        mock_dicom = MagicMock()
        mock_dicom.pixel_array = np.random.randint(0, 256, (512, 512), dtype=np.uint8)
        mock_dcmread.return_value = mock_dicom
        obj = MyClass('dummy_path.dcm')
        img_RGB, img2show = obj.read_dicom_file()
        self.assertIsInstance(img_RGB, np.ndarray)
        self.assertIsInstance(img2show, Image.Image)
        self.assertEqual(img_RGB.dtype, np.uint8)
        self.assertEqual(img_RGB.shape[2], 3)


######################### Prueba 3 ##################################################################   