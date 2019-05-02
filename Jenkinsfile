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
                sh 'python3 /home/hadoop/Documents/skype_bot_message_processing/frank_contributions/3-23.py ' 
            }
        }
    }
}
