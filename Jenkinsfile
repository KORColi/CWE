pipeline {
    agent any

    stages {
        stage('Static Analysis') {
            steps {
                // Static analysis 도구 실행 명령 추가
                echo 'Running static analysis...'
            }
        }
        stage('Dynamic Analysis') {
            steps {
                // Dynamic analysis 도구 실행 명령 추가
                echo 'Running dynamic analysis...'
            }
        }
        stage('AI Analysis') {
            steps {
                // AI 분석 스크립트 실행 명령 추가
                echo 'Running AI analysis...'
                sh 'python3 ai_analysis.py'
            }
        }
    }
}

