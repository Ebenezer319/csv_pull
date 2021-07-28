import unittest
from csv_pull.utils import transform_data, create_csv
import pandas as pd
import string 

class TestBasic(unittest.TestCase):
    
    def test_input(self):
        lowercase_letters = list(string.ascii_lowercase)
        self.assertEqual(len(lowercase_letters), 26)
        
    def test_create_file(self):
        user = [1,2,3,4,3]
        length = [4, 5, 6, 7, 2]
        path = ['/', '/check', '/','/test', '/test/room']        
        d_frame = pd.DataFrame(data={'user_id': user, 'length':length, 'path': path})
        file_name = 'Test.csv'
        create_csv(d_frame, file_name)
        
        test_file = pd.read_csv('Test.csv')
        self.assertEqual(test_file.shape[0], 5)
        
    def test_transform_data(self):
        user = [1,2,3,4,3]
        length = [4, 5, 6, 7, 2]
        path = ['/', '/check', '/','/test', '/test/room']        
        frame = pd.DataFrame(data={'user_id': user, 'length':length, 'path': path})
        pivot = transform_data(frame)
        
        self.assertEqual(pivot.shape[1], 4)
