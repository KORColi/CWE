pipeline {
    agent any
    environment {
        SONARQUBE_SCANNER_HOME = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
        SONAR_PROJECT_KEY = 'CWE-79'  // SonarQube에서 확인한 프로젝트 키
        SONAR_PROJECT_NAME = 'CWE-79'  // SonarQube 대시보드에 표시된 프로젝트 이름
        SONARQUBE_HOST_URL = 'http://localhost:9000'
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
                gdown --id 15IFVCP2oMkY5GkCcwf6UJThRjmeSRq1B -O nvdcve-1.1-2021.json.gz
                gdown --id 15IFVCP2oMkY5GkCcwf6UJThRjmeSRq1B -O nvdcve-1.1-2022.json.gz
                gdown --id 102cEdnxztmrx0qdScs82t6AlhPHwQE5d -O nvdcve-1.1-2023.json.gz
                gdown --id 1YK_E3_Fvd-FJelPvCFlVcnt1fNL3i0_R -O nvdcve-1.1-2024.json.gz
                '''
            }
        }
        stage('Static Analysis') {
            steps {
                echo 'Running static analysis with SonarQube...'
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    $SONARQUBE_SCANNER_HOME/bin/sonar-scanner \
                      -Dsonar.projectKey=$SONAR_PROJECT_KEY \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=$SONARQUBE_HOST_URL
                    '''
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: '**/sonarqube-reports/*', allowEmptyArchive: true
                }
            }
        }
        stage('Dynamic Analysis') {
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
        stage('AI Analysis') {
            steps {
                sh '''
                . venv/bin/activate
                python3 ai_analysis.py > ai_analysis_report.txt
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'ai_analysis_report.txt', allowEmptyArchive: true
                }
            }
        }
    }
}
