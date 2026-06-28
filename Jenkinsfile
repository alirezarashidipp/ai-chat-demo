pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    python3 --version || true
                    pip3 --version || true
                    echo "Jenkins simple pipeline is running"
                '''
            }
        }
    }
}