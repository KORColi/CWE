import json
import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 예시 데이터: 잠재적인 취약점을 식별하는 기계 학습 모델을 위한 데이터
training_data = [
    "Buffer overflow in function XYZ",
    "SQL injection vulnerability in function ABC",
    "Cross-site scripting in function DEF",
    "Use after free in function GHI",
    "Integer overflow in function JKL"
]
training_labels = [1, 1, 1, 1, 1]  # 1은 취약점 있음, 0은 취약점 없음

# 간단한 벡터화 및 모델 훈련
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_data)
model = MultinomialNB()
model.fit(X_train, training_labels)

def load_nvd_data(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        data = json.load(file)
    return data

def analyze_data(data):
    # 예시 분석: CVE의 총 수 계산
    total_cves = len(data['CVE_Items'])
    detected_vulnerabilities = 0
    
    for item in data['CVE_Items']:
        description = item['cve']['description']['description_data'][0]['value']
        X_test = vectorizer.transform([description])
        prediction = model.predict(X_test)
        if prediction[0] == 1:
            detected_vulnerabilities += 1
    
    return total_cves, detected_vulnerabilities

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
            total_cves, detected_vulnerabilities = analyze_data(nvd_data)
            result_file.write(f"Total CVEs in {file}: {total_cves}\n")
            result_file.write(f"Detected Vulnerabilities in {file}: {detected_vulnerabilities}\n")
            print(f"Finished processing {file}")
