pipeline {
    agent any
    environment {
        SONAR_SCANNER_HOME = '/opt/sonar-scanner/latest'  // SonarQube 스캐너 경로
        SONAR_PROJECT_KEY = 'CWE-79'  // SonarQube 프로젝트 키
        SONAR_PROJECT_NAME = 'CWE-79'  // SonarQube 프로젝트 이름
        SONARQUBE_HOST_URL = 'http://localhost:9000'  // SonarQube 서버 URL
        SONARQUBE_TOKEN = 'sqa_32bedcecbd772605f34aba9f20565ae4f9dc762b'  // SonarQube 인증 토큰
        ZAP_DOCKER_IMAGE = 'owasp/zap2docker-stable'  // OWASP ZAP Docker 이미지
        ZAP_TARGET_URL = 'http://your-application-url.com'  // OWASP ZAP으로 테스트할 타겟 URL
        ZAP_REPORT = 'zap_report.html'  // OWASP ZAP 결과 파일
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm  // Git에서 소스 코드 다운로드
            }
        }
        stage('Run SonarQube Analysis') {
            steps {
                echo 'Running static analysis with SonarQube...'
                sh '''
                    chmod +x ${SONAR_SCANNER_HOME}/bin/sonar-scanner
                    ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
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
        stage('Run OWASP ZAP') {
            steps {
                echo 'Running dynamic analysis with OWASP ZAP...'
                sh '''
                docker run -v $(pwd):/zap/wrk/:rw -t ${ZAP_DOCKER_IMAGE} zap-baseline.py \
                -t ${ZAP_TARGET_URL} \
                -r ${ZAP_REPORT}
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
            archiveArtifacts artifacts: '**/sonarqube-reports/*, ${ZAP_REPORT}', allowEmptyArchive: true
        }
    }
}
