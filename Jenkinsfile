pipeline {
    agent any
    environment {
        SONAR_SCANNER_HOME = '/opt/sonar-scanner/latest'
        SONAR_PROJECT_KEY = 'CWE-79'
        SONAR_PROJECT_NAME = 'CWE-79'
        SONARQUBE_HOST_URL = 'http://localhost:9000'
        SONARQUBE_TOKEN = 'squ_7dbbba69ba6c89fc6e43ee78926153a559d2df3c'
        ZAP_DOCKER_IMAGE = 'owasp/zap2docker-stable'
        ZAP_TARGET_URL = 'http://your-application-url.com'
        ZAP_REPORT = 'zap_report.html'
        CUSTOM_PAYLOAD_PATH = '/home/compiler/PayloadsAllTheThings/XSS/xss_payloads.txt'
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Run SonarQube Analysis') {
            steps {
                echo 'Running static analysis with SonarQube...'
                sh '''
                    chmod +x ${SONAR_SCANNER_HOME}/bin/sonar-scanner
                    ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                    -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                    -Dsonar.sources=${WORKSPACE},${CUSTOM_PAYLOAD_PATH} \
                    -Dsonar.host.url=${SONARQUBE_HOST_URL} \
                    -Dsonar.login=${SONARQUBE_TOKEN}
                '''
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
}
