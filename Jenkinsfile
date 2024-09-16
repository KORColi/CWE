pipeline {
    agent any
    environment {
        SONARQUBE_SCANNER_HOME = '/opt/sonar-scanner/latest'
        SONAR_PROJECT_KEY = 'CWE-79'
        SONAR_PROJECT_NAME = 'CWE-79'
        SONARQUBE_HOST_URL = 'http://localhost:9000'
        SONARQUBE_TOKEN = 'sqa_32bedcecbd772605f34aba9f20565ae4f9dc762b'
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
        // Other stages
    }
}
