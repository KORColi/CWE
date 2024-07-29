import json

def load_nvd_data(file_path):
    """Load NVD data from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def analyze_data(data):
    """Analyze NVD data."""
    for item in data.get('CVE_Items', []):
        cve_id = item.get('cve', {}).get('CVE_data_meta', {}).get('ID')
        description = item.get('cve', {}).get('description', {}).get('description_data', [])[0].get('value')
        impact = item.get('impact', {}).get('baseMetricV2', {}).get('severity', 'UNKNOWN')
        
        print(f"Analyzing {cve_id} - Severity: {impact}, Description: {description}")

if __name__ == "__main__":
    nvd_data = load_nvd_data('nvd_data.json')
    analyze_data(nvd_data)
