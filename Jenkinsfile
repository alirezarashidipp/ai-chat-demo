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

        stage('Run Pytest Inside Docker') {
            steps {
                sh 'docker run --rm -e OPENAI_API_KEY=dummy-key ai-chat-demo pytest tests/'
            }
        }
    }
}