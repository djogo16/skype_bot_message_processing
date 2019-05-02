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
                sh 'python -m py_compile /home/hadoop/Documents/skype_bot_message_processing/frank_contributions/3-23.py /home/hadoop/Documents/skype_bot_message_processing/frank_contributions/hivebatch.py /home/hadoop/Documents/skype_bot_message_processing/frank_contributions/hive_job_scheduler.py' 
            }
        }
    }
}
