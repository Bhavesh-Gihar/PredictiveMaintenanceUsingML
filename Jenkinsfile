pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'mlopsimg'
        DOCKER_CONTAINER_NAME = 'mlopscontainer'
        FLASK_APP_PORT = '8001'
    }
    
    triggers {
        pollSCM('*/5 * * * *') // Poll SCM every 5 minutes
    }
    
    stages {
        stage('Fetch Code') {
            steps {
                // Fetch code from GitHub
                git branch: 'main', url: 'https://github.com/Bhavesh-Gihar/PredictiveMaintenanceUsingML'
            }
        }
        
        stage('Integration Pipeline') {
            steps {
                dir('mlOps') {
                    sh "pip install -r requirements.txt"
                    
                    script {
                        // Execute training pipeline script to train the ML model
                        def accuracy = sh(script: 'python3 integrationPipeline.py', returnStdout: true).trim()
                    
                        // // Store the accuracy in an environment variable
                        // env.ACCURACY = accuracy.toFloat()
                    }
                }
            }
        }
        
        stage('Build Deployment') {
            steps {
                dir('mlOps') {
                    script {
                        // Build Docker image
                        sh "sudo docker stop ${DOCKER_CONTAINER_NAME}"
                        sh "sudo docker rm ${DOCKER_CONTAINER_NAME}"
                        sh "sudo docker rmi ${DOCKER_IMAGE_NAME}"
                        sh "sudo docker build -t ${DOCKER_IMAGE_NAME} ."
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    sh "sudo docker run -d -p 8001:8001 --name ${DOCKER_CONTAINER_NAME} ${DOCKER_IMAGE_NAME}"
                }
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
    }
}
