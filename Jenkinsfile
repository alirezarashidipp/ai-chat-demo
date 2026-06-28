pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ai-chat-demo .'
            }
        }

        stage('Run Tests In Docker') {
            steps {
                sh 'docker run --rm ai-chat-demo pytest tests/'
            }
        }
    }
}