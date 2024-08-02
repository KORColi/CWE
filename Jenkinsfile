pipeline {
    agent any
    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install gdown pylint pytest
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
                sh '''
                . venv/bin/activate
                pylint ai_analysis.py > static_analysis_results.txt
                '''
                archiveArtifacts artifacts: 'static_analysis_results.txt'
            }
        }
        stage('Dynamic Analysis') {
            steps {
                sh '''
                . venv/bin/activate
                pytest > dynamic_analysis_results.txt
                '''
                archiveArtifacts artifacts: 'dynamic_analysis_results.txt'
            }
        }
        stage('AI Analysis') {
            steps {
                sh '''
                . venv/bin/activate
                python3 ai_analysis.py > ai_analysis_results.txt
                '''
                archiveArtifacts artifacts: 'ai_analysis_results.txt'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
