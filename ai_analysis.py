import json
import gzip

def load_nvd_data(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        data = json.load(file)
    return data

def analyze_data(data):
    # 예시 분석: CVE의 총 수 계산
    total_cves = len(data['CVE_Items'])
    return total_cves

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
    
    with open('ai_analysis_results.txt', 'w') as result_file:
        for file in nvd_files:
            print(f"Processing {file}")
            nvd_data = load_nvd_data(file)
            total_cves = analyze_data(nvd_data)
            result_file.write(f"Total CVEs in {file}: {total_cves}\n")
            print(f"Finished processing {file}")
