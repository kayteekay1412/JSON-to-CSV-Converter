# -*- coding: utf-8 -*-
"""
@author: ktk
"""

import json
import sys

def json_to_csv(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())

        if not data:
            raise ValueError("JSON data is empty.")

        headers = list(data[0].keys())
        output = ','.join(headers)
        
        for obj in data:
            row = ','.join(str(obj[key]) for key in headers)
            output += f'\n{row}'

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
        
        print(f'Successfully converted {input_path} to {output_path}')
        
    except FileNotFoundError:
        print(f'Error: The file {input_path} does not exist.')
    except json.JSONDecodeError:
        print('Error: Failed to decode JSON.')
    except Exception as ex:
        print(f'An unexpected error occurred: {str(ex)}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python script.py <input_json_path> <output_csv_path>')
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        json_to_csv(input_path, output_path)
