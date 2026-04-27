pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ayushbhor04/expense-tracker"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/AyushBhor04/expense-tracker-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t expense-tracker .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag expense-tracker $DOCKER_IMAGE'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
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
