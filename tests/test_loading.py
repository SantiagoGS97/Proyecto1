import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from PIL import ImageTk, Image
from funciones import predict,preprocess,read_jpg_file
import cv2
import warnings
import pytest

    
class TestCase(unittest.TestCase):
    def test_random(self): 
        a = 1
        self.assertEqual(a, 1)

class TestReadJpgFile(unittest.TestCase):
    @patch('cv2.imread')
    def test_read_jpg_file(self, mock_imread):
        # Crear un array numpy simulado que representa una imagen
        mock_img = np.array([[0, 1], [2, 3]], dtype=np.uint8)
        mock_imread.return_value = mock_img
        filepath = 'dummy.jpg'
        img2, img2show = read_jpg_file(filepath)
        self.assertIsInstance(img2, np.ndarray)
        self.assertIsInstance(img2show, Image.Image)
        self.assertEqual(img2.shape, mock_img.shape)
