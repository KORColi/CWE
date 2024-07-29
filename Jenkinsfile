pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/KORColi/CWE.git'
            }
        }
        stage('Static Analysis') {
            steps {
                // Checkmarx 스캔 명령어 또는 대체 명령어를 추가합니다.
            }
        }
        stage('Dynamic Analysis') {
            steps {
                // OWASP ZAP 명령어를 추가합니다.
                zapStart target: 'http://your-app-url'
                zapSpider()
                zapScan()
                zapReport()
            }
        }
        stage('AI Analysis') {
            steps {
                sh 'python3 ai_analysis.py'
            }
        }
    }
}
