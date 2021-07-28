# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:18:32 2021

@author: ebenezer.an
"""

from csv_pull.utils import pull_files, transform_data, create_csv
import sys

def main():
    try:
        path = sys.argv[1]
        user_data = pull_files(path)
        user_pivot = transform_data(user_data)
        create_csv(user_pivot, 'User Journey.csv')
        print("Program Successfully Finished!")
        
    except TypeError:
        exc_type, exc_val, exc_tb = sys.exc_info()
        print(f"An exception occurred - {exc_val} line {exc_tb.tb_lineno}")
        print('You have entered a value that is not a string. Please use public root URL like "https://public.wiwdata.com/"')    
                
    except FileNotFoundError: 
        exc_type, exc_val, exc_tb = sys.exc_info()
        print(f"An exception occurred - {exc_val} line {exc_tb.tb_lineno}")
        print('Non existent public root URL provided. Please provide an accurate directory"')        
        
    except IndexError:  
        exc_type, exc_val, exc_tb = sys.exc_info()
        print(f"An exception occurred {exc_val} line {exc_tb.tb_lineno}")
        print('Please provide a public root URL like "https://public.wiwdata.com/"')
        
    except:
        exc_type, exc_val, exc_tb = sys.exc_info()
        print(f"An exception occurred - {exc_type}")
        print(f"{exc_val} at line {exc_tb.tb_lineno}")
            


main()
