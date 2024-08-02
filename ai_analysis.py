import json
import gzip

def load_nvd_data(file_path):
    with gzip.open(file_path, 'rt') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    nvd_files = [
        'nvdcve-1.1-2017.json.gz',
        'nvdcve-1.1-2018.json.gz',
        'nvdcve-1.1-2019.json.gz',
        'nvdcve-1.1-2020.json.gz',
        'nvdcve-1.1-2021.json.gz',
        'nvdcve-1.1-2022.json.gz',
        'nvdcve-1.1-2023.json.gz',
        'nvdcve-1.1-2024.json.gz'
    ]
    
    for file in nvd_files:
        print(f"Processing {file}")
        nvd_data = load_nvd_data(file)
        # Add your analysis code here
        print(f"Finished processing {file}")
