pipeline {
    agent any
    environment {
        SONARQUBE_SCANNER_HOME = '/opt/sonar-scanner/latest'  // SonarScanner 설치 경로
        SONAR_PROJECT_KEY = 'CWE-79-XSS-Detection'  // SonarQube 프로젝트 키
        SONARQUBE_HOST_URL = 'http://localhost:9000'  // SonarQube 서버 URL
        SONARQUBE_TOKEN = 'your_sonar_token'  // SonarQube에서 생성된 토큰
        ZAP_DOCKER_IMAGE = 'owasp/zap2docker-stable'  // ZAP Docker 이미지
        ZAP_TARGET_URL = 'http://your-application-url.com'  // 동적 분석할 웹 애플리케이션 URL
        ZAP_REPORT = 'zap_report.html'  // OWASP ZAP 결과 파일
        CUSTOM_PAYLOAD_PATH = '/path/to/your/xss_payloads.txt'  // 사용자 정의 페이로드 파일 경로
    }
    stages {
        stage('SCM') {
            steps {
                checkout scm  // 소스 코드 다운로드
            }
        }
        
        stage('SonarQube Static Analysis') {
            steps {
                echo 'Running static analysis with SonarQube...'
                sh '''
                ${SONARQUBE_SCANNER_HOME}/bin/sonar-scanner \
                  -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                  -Dsonar.sources=. \
                  -Dsonar.host.url=${SONARQUBE_HOST_URL} \
                  -Dsonar.login=${SONARQUBE_TOKEN}
                '''
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
                // OWASP ZAP을 사용한 동적 분석. 사용자 정의 페이로드 연동
                sh '''
                docker run -v $(pwd):/zap/wrk/:rw -t ${ZAP_DOCKER_IMAGE} zap-baseline.py \
                -t ${ZAP_TARGET_URL} \
                -r ${ZAP_REPORT} \
                -p /zap/wrk/xss_payloads.txt
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: "${ZAP_REPORT}", allowEmptyArchive: true
                }
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: '**/zap_report.html', allowEmptyArchive: true
        }
    }
}
