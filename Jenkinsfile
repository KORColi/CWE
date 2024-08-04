pipeline {
    agent any
    environment {
        SONARQUBE_SCANNER_HOME = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
        SONAR_PROJECT_KEY = 'CWE-79'  // 여기에 SonarQube에서 확인한 프로젝트 키를 입력
        SONAR_PROJECT_NAME = 'CWE-79'  // 프로젝트 이름
        SONARQUBE_HOST_URL = 'http://localhost:9000'
        SONARQUBE_TOKEN = 'sqp_82a6743c4bfe5853c53e57bf15fb386086cd3eda'
    }
    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install gdown scikit-learn
                '''
            }
        }
        stage('Download NVD Data') {
            steps {
                sh '''
                . venv/bin/activate
                gdown --id 1EIx6HWnFvu1ImymrMDVwums573NHJL9_ -O nvdcve-1.1-2017.json.gz
                gdown --id 1C6GUd7IMrsKfF3Fj4NOkoOJ9Ipclf3L5 -O nvdcve-1.1-2018.json.gz
                gdown --id 1QWDoX4Yup89SthBCRGUEPCBL2G38viVK -O nvdcve-1.1-2019.json.gz
                gdown --id 1bjps8VHKPpxzl72gR2ZqOwDvGlO5id8o -O nvdcve-1.1-2020.json.gz
