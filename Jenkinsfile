pipeline {
    agent any
    
    environment {
        DOCKER_HOST = 'your-docker-host-ip'
        DOCKER_REMOTE_DIR = '/path/to/remote/directory'
        DOCKER_IMAGE_NAME = 'flask-ml-api'
        DOCKER_CONTAINER_NAME = 'flask-ml-container'
        FLASK_APP_PORT = '5000'
    }
    
    triggers {
        pollSCM('H 0 * * *') // Poll SCM once a day
    }
    
    stages {
        stage('Build Data Pipeline') {
            steps {
                // Fetch code from GitHub
                git 'https://github.com/your-username/data-pipeline.git'
                // Build data pipeline
            }
        }
        
        stage('Build Training Pipeline') {
            steps {
                // Fetch code from GitHub
                git 'https://github.com/your-username/training-pipeline.git'
                // Build training pipeline
            }
        }
        
        stage('Build Testing Pipeline') {
            steps {
                // Fetch code from GitHub
                git 'https://github.com/your-username/testing-pipeline.git'
                // Build testing pipeline
            }
        }
        
        stage('Build Deploying Pipeline') {
            steps {
                // Fetch code from GitHub
                git 'https://github.com/your-username/deploying-pipeline.git'
                // Build deploying pipeline
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Fetch code from GitHub
                git 'https://github.com/your-username/flask-server.git'
                // Build Docker image
                sh "docker build -t ${DOCKER_IMAGE_NAME} ."
            }
        }
        
        stage('Deploy') {
            steps {
                // Push Docker image to Docker host
                sh "docker save ${DOCKER_IMAGE_NAME} | ssh -i ${SSH_KEY} ${DOCKER_HOST} 'docker load'"
                
                // Run Docker container
                sh "ssh -i ${SSH_KEY} ${DOCKER_HOST} 'docker run -d --name ${DOCKER_CONTAINER_NAME} -p ${FLASK_APP_PORT}:5000 ${DOCKER_IMAGE_NAME}'"
            }
        }
    }
    
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
        cleanup {
            // Clean up resources (optional)
            // sh "ssh -i ${SSH_KEY} ${DOCKER_HOST} 'docker stop ${DOCKER_CONTAINER_NAME} && docker rm ${DOCKER_CONTAINER_NAME}'"
        }
    }
}
