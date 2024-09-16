pipeline {
    agent any
    environment {
        SONARQUBE_SCANNER_HOME = '/opt/sonar-scanner/latest'  // 스캐너 경로 설정
        SONAR_PROJECT_KEY = 'CWE-79'  // 프로젝트 키 설정
        SONAR_PROJECT_NAME = 'CWE-79'  // 프로젝트 이름 설정
        SONARQUBE_HOST_URL = 'http://localhost:9000'  // SonarQube URL
        SONARQUBE_TOKEN = 'sqa_32bedcecbd772605f34aba9f20565ae4f9dc762b'  // SonarQube 토큰
    }
    stages {
        stage('SCM') {
            steps {
                checkout scm
            }
        }
        stage('SonarQube Analysis') {
            steps {
                echo 'Running static analysis with SonarQube...'
                sh """
                ${SONARQUBE_SCANNER_HOME}/bin/sonar-scanner \
                  -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                  -Dsonar.sources=. \
                  -Dsonar.host.url=${SONARQUBE_HOST_URL} \
                  -Dsonar.login=${SONARQUBE_TOKEN}
                """
            }
            post {
                always {
                    archiveArtifacts artifacts: '**/sonarqube-reports/*', allowEmptyArchive: true
                }
            }
        }
        stage('Dynamic Analysis with OWASP ZAP') {
            steps {
                echo 'Running dynamic analysis with OWASP ZAP...'
                sh '''
                docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t http://example.com -r zap_report.html
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'zap_report.html', allowEmptyArchive: true
                }
            }
        }
    }
}
