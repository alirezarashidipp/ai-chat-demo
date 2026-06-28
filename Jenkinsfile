pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Show Environment') {
            steps {
                sh 'uname -a'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ai-chat-demo .'
            }
        }

        stage('Run Tests In Docker') {
            steps {
                sh 'docker run --rm ai-chat-demo pytest'
            }
        }
    }
}