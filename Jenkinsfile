pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile /frank_contributions/3-23.py /frank_contributions/hivebatch.py /frank_contributions/hive_job_scheduler.py' 
            }
        }
    }
}
