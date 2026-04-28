pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ayushbhor04/expense-tracker"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/AyushBhor04/expense-tracker-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t expense-tracker .'
            }
        }

        stage('Tag Image') {
            steps {
                bat 'docker tag expense-tracker %DOCKER_IMAGE%:latest'
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker push %DOCKER_IMAGE%:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}