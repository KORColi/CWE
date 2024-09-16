pipeline {
    agent any
    environment {
        // SonarQube 관련 환경 변수 설정
        SONARQUBE_SCANNER_HOME = '/opt/sonar-scanner/latest'  // SonarQube 스캐너 설치 위치
        SONAR_PROJECT_KEY = 'CWE-79'  // SonarQube 프로젝트 키 (프로젝트 이름과 동일하게 설정)
        SONAR_PROJECT_NAME = 'CWE-79'  // SonarQube 프로젝트 이름
        SONARQUBE_HOST_URL = 'http://localhost:9000'  // SonarQube 서버 URL
        SONARQUBE_TOKEN = 'sqa_32bedcecbd772605f34aba9f20565ae4f9dc762b'  // SonarQube 인증 토큰

        // OWASP ZAP 관련 환경 변수 설정
        ZAP_DOCKER_IMAGE = 'owasp/zap2docker-stable'  // OWASP ZAP Docker 이미지
        ZAP_TARGET_URL = 'http://your-application-url.com'  // 동적 분석할 웹 애플리케이션 URL
        ZAP_REPORT = 'zap_report.html'  // OWASP ZAP 결과 파일 경로

        // 사용자 정의 XSS 페이로드 경로
        CUSTOM_PAYLOAD_PATH = '/home/compiler/PayloadsAllTheThings/XSS Injection/XSS_Common_WAF_Bypass.txt'  // XSS 페이로드 데이터셋 경로
    }
    stages {
        stage('SCM') {
            steps {
                checkout scm  // 소스 코드 다운로드
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
                sh """
                docker run -v $(pwd):/zap/wrk/:rw -t ${ZAP_DOCKER_IMAGE} zap-baseline.py \
                -t ${ZAP_TARGET_URL} \
                -r ${ZAP_REPORT} \
                -p /zap/wrk/${CUSTOM_PAYLOAD_PATH}
                """
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
