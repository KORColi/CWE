pipeline {
    agent any
    environment {
        CHECKMARX_SERVER = 'https://your-checkmarx-server-url.com'  // Checkmarx 서버 URL
        CHECKMARX_PROJECT = 'CWE-79-XSS-Detection'  // Checkmarx 프로젝트 이름
        CHECKMARX_CREDENTIALS = 'checkmarx_credentials'  // Jenkins에 저장된 Checkmarx 인증 정보 ID
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
        
        stage('Checkmarx Static Analysis') {
            steps {
                echo 'Running static analysis with Checkmarx...'
                checkmarxScan credentialsId: "${CHECKMARX_CREDENTIALS}", 
                               projectName: "${CHECKMARX_PROJECT}", 
                               serverUrl: "${CHECKMARX_SERVER}"
            }
            post {
                always {
                    archiveArtifacts artifacts: '**/checkmarx-reports/*', allowEmptyArchive: true
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
        
        stage('AI Analysis') {
            steps {
                // AI 분석 코드 (선택 사항, 여기에 AI 분석 작업을 추가)
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
    
    post {
        always {
            archiveArtifacts artifacts: '**/ai_analysis_report.txt', allowEmptyArchive: true
        }
    }
}
